# Pipeline components

The Nextflow code is split into one module per tool or step (`modules/local/`) and subworkflows
that chain them (`subworkflows/local/`). The diagram is on [Pipeline architecture](architecture.md).

## Main workflow

**File:** `workflows/tbfhir.nf`

Reads the samplesheet (or the input folders), checks the sample ids and routes each sample to the
branch for its platform. All samples run in parallel.

## Reference preparation

**File:** `subworkflows/local/prepare_reference.nf`

Indexes the H37Rv reference (NC_000962.3) **once per run**: `samtools faidx`, the GATK sequence
dictionary and, when there are Illumina samples, the bwa-mem2 index.

## Illumina (short-read) branch

**File:** `subworkflows/local/illumina.nf`

1. **Read QC**: FastQC.
2. **Trimming**: Trimmomatic, `LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:36`.
3. **Alignment**: bwa-mem2 with `-K 100000000`, so alignments do not depend on the number of
   CPUs.
4. **Variant calling**: GATK HaplotypeCaller. The Java heap is derived from the task memory.

## Nanopore (long-read) branch

**File:** `subworkflows/local/nanopore.nf`

1. **Read QC**: NanoPlot.
2. **Read filtering**: chopper, minimum read quality `--nanopore_min_q` (10) and minimum length
   `--nanopore_min_l` (500).
3. **Alignment**: minimap2.
4. **Variant calling**: medaka with the model given in `--medaka_model`.

## VCF input

**File:** `modules/local/vcf_normalize.nf`

VCFs are sorted and normalised with `bcftools norm` (multi-allelic records split, reference
alleles set from H37Rv where they disagree). They have no alignment, so coverage cannot be assessed (see
[Coverage assessment](#coverage-assessment)).

## Variant filtering

**File:** `modules/local/filter_variants.nf`

1. **Region filter**: removes calls in repetitive regions (PE/PPE genes, insertion sequences),
   unless `--repetitive_regions` points at `assets/NO_FILE`.
2. **Type filter**: SNPs and indels.
3. **Depth filter**: read depth (DP) ≥ `--filter_min_depth` (5).
4. **Quality filter**: ≥ `--filter_min_quality` (20), on a measure that depends on the platform:

| Platform | Quality measure |
| --- | --- |
| Illumina (GATK) | `QUAL`, the confidence that a variant is present |
| ONT (medaka) | `GQ` |
| VCF input | `FORMAT/GQ`, `INFO/GQ` or `QUAL`, whichever the file has |

## Variant annotation

**File:** `modules/local/annotate_variants.nf`

`bcftools annotate` matches each variant against the WHO annotation table (see
[Configuration](configuration.md#who-annotation-table)) and adds:

| Field | Content |
| --- | --- |
| `GENE` | the gene affected |
| `DRUG` | the drugs the variant is graded for |
| `EFFECT` | predicted effect, e.g. `missense_variant`, `frameshift_variant` |
| `WHO_CLASSIFICATION` | the WHO final grade, one per drug, e.g. `Assoc w R` |
| `VARIANT_ID` | the WHO catalogue variant name, one per drug, e.g. `rpoB_p.Ser450Leu` |

`DRUG`, `WHO_CLASSIFICATION` and `VARIANT_ID` are aligned lists, so a variant can be resistant to
one drug and uncertain for another.

## Coverage assessment

**File:** `subworkflows/local/coverage.nf`

Decides, per drug, whether the resistance loci were actually sequenced.

1. **Targets** (`bin/make_who_targets.py`):
   - Resistance loci come from the WHO annotation table.
   - Variant positions are clustered per gene (gaps up to 5000 bp).
   - Each locus is padded by `--promoter_padding` (200 bp), clamped to the contig, and the repeat
     mask is subtracted.
   - Output: `qc/coverage/who_targets.bed`.
2. **Depth**: `mosdepth --by who_targets.bed --thresholds … --no-per-base`.
3. **Assessability** (`bin/summarize_coverage.py`):
   - Coverage is aggregated per gene as a length-weighted mean, so a gene split by the repeat
     mask counts as one locus.
   - A gene is **adequate** when the fraction of bases at ≥ `--coverage_min_depth` (10) reaches
     `--coverage_min_breadth` (0.95).
   - A **drug is assessable only when every one of its loci is adequate**.
   - Output: `qc/coverage/<id>.coverage.json`.

VCF input has no alignment, so its coverage file says `coverage_assessed: false`, and every
non-resistant drug is reported Indeterminate.

## Lineage classification

**File:** `subworkflows/local/lineage.nf`

1. **Barcode SNPs**: variants at the lineage barcode positions are extracted from the filtered
   VCF.
2. **Classification** (`bin/lineage_classifier.py`): each lineage is scored by the share of its
   barcode SNPs that match. The confidence is:
   - **high**: score ≥ 0.8 and at least 3 SNPs matched
   - **medium**: score ≥ 0.6 and at least 2 SNPs matched
   - **low**: otherwise

## FHIR genomic step

**File:** `bin/tbfhir_genomic.py` (`modules/local/fhir_genomic.nf`)

Builds one bundle per sample, `fhir/genomic/<id>.genomic.fhir.json`, with no patient data:
- a variant Observation per annotated variant, with one medication / clinical-significance pair
  per drug
- the susceptibility panel: **Resistant** when a variant graded *Assoc w R* or *Assoc w R -
  Interim* (WHO group 1 or 2) is found for the drug, otherwise **Susceptible** or
  **Indeterminate** depending on coverage
- a region-studied Observation per gene, and the lineage Observation
- the DiagnosticReport with the resistance classification, plus Device and Provenance

## Sample report

**File:** `bin/generate_sample_report.py`

A plain-text summary per sample, `reports/<id>.summary_report.txt`.

## Clinical and link steps (optional)

**Files:** `bin/clinical_to_fhir.py`, `bin/link_fhir_bundle.py`

With `--patient_metadata`, the clinical step builds Patient, Specimen, Encounter and
ServiceRequest per sample, and Organization, Practitioner and PractitionerRole once. The link
step joins them with the genomic bundle into one FHIR `transaction` per sample. See
[Clinical metadata](clinical_metadata.md).

## FHIR validation

**Files:** `modules/local/fhir_validate.nf`

Every genomic and linked bundle is checked with the HL7 FHIR validator against
`hl7.fhir.uv.genomics-reporting#3.0.0` and the project CodeSystems:
- Validation runs offline by default (`--fhir_tx_server n/a`), so no codes are sent to a public
  terminology server. Checks that need a terminology server are reported as not performed.
- Files are validated in batches of `--fhir_validation_batch_size` (50).
- An error stops the run for `generic` and only warns for `satusehat`, whose Kemkes profiles the
  validator cannot resolve. Override with `--fail_on_validation_error true|false`.
- Results: `fhir/validation/validation_summary.tsv`.
- `--skip_fhir_validation` skips the step.

## Upload (optional)

**Files:** `bin/upload_fhir.py` (`modules/local/fhir_upload.nf`)

Runs only with `--fhir_server_url`. It sends linked bundles that passed validation, one at a
time, with a client-credentials token from `--fhir_auth_url`. A summary of the server's response
(HTTP status, and the status and location of each entry) is saved in
`fhir/upload/<id>.bundle.upload.json`. See
[Installation](installation.md#uploading-to-a-fhir-server).

## Run reports

- **MultiQC** collects FastQC and NanoPlot results into `qc/multiqc/multiqc_report.html`.
- **Nextflow reports** (execution report, timeline, trace, DAG) and
  `software_versions.yml`, with every tool version used, are in `pipeline_info/`.
