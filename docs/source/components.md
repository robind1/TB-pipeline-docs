# Data Processing

## Main Workflow
**File:** `main.nf`
The main workflow handles channel processing and parallel execution. It automatically detects input data types (Illumina, Nanopore, or pre-annotated VCF) and routes them to the dedicated sub-workflows. All inputs are processed concurrently.

## Nanopore (Long-Read) Workflow
**File:** `nanopore.nf`
For Oxford Nanopore Technologies (ONT) sequencing data
1.  **Quality Control**: 
    *   Tool: `FastQC`
    *   Metrics: Per-sample quality, GC content, per-base sequence quality, and N-content.
2.  **Trimming**
    * **Tool:** `Chopper`
    * **Function:** Filters reads based on average quality and minimum length.
    * **Parameters:** `min_q = 10`, `min_l = 500`.
3.  **Alignment**:
    *   Tool: `Minimap2`
    *   Reference: *M. tuberculosis* H37Rv (NC_000962.3).
4.  **Variant Calling**:
    *   Tool: `Medaka`
    *   Model: configurable via `params.medaka_model`; defaults to `'r941_e81_sup_variant_g514'` (R9.4.1).
        Set `medaka_model` =  `r1041_e82_400bps_sup_variant_v5.0.0` (R10.4.1)chemistry.
5.  **Filtering**:
    *   **Region Filter**: Excludes repetitive regions (PE/PPE genes).
    *   **Type Filter**: SNPs and Indels only.
    *   **Depth Filter**: Minimum coverage (DP) ≥ 5x.
    *   **Quality Filter**: Genotype Quality (GQ) ≥ 20.

## Illumina (Short-Read) Workflow
**File:** `illumina.nf`
For Illumina paired-end sequencing data
1.  **Quality Control**:
    *   Tool: `FastQC`
    *   Metrics: Per-sample quality, GC content, per-base sequence quality, and N-content.
2.  **Trimming**
    * **Tool:** `Trimmomatic`
    * **Function:** Quality trimming.
    * **Settings:** Leading/Trailing quality cutoff (3), Sliding Window quality cutoff (4:20), and minimum length (36 bp).
2.  **Alignment**:
    *   Tool: `BWA-MEM2`
    *   Reference: *M. tuberculosis* H37Rv (NC_000962.3).
3.  **Variant Calling**:
    *   Tool: `GATK HaplotypeCaller`
4.  **Filtering**:
    *   **Region Filter**: Excludes repetitive regions (PE/PPE genes).
    *   **Type Filter**: SNPs and Indels only.
    *   **Depth Filter**: Minimum coverage (DP) ≥ 5x.
    *   **Quality Filter**: Genotype Quality (GQ) ≥ 20.

## VCF Workflow
**File:** `vcf.nf`
For pre-annotated/raw variant files
1.  **Normalization**:
    *   Tool: `bcftools norm`
2.  **Filtering**:
    *   **Region Filter**: Excludes repetitive regions (PE/PPE genes).
    *   **Type Filter**: SNPs and Indels only.
    *   **Depth Filter**: Minimum coverage (DP) ≥ 5x.
    *   **Quality Filter**: Genotype Quality (GQ) ≥ 20.

## Coverage Assessment
**File:** `coverage.nf`
Determines, per drug, whether the resistance loci were actually sequenced. This is what allows a
"no resistance mutation detected" result to be distinguished.

1.  **Target Generation** (`scripts/make_who_targets.py`):
    *   Derives resistance loci directly from the WHO catalogue annotation table.
    *   Variant positions are clustered per gene (`--max-gap`, default 5000 bp).
    *   Each locus is padded by `promoter_padding` (default 200 bp), clamped to the contig length
        using the reference `.fai`, and the repetitive-region mask is subtracted.
    *   Output: `who_targets.bed`.
2.  **Depth Measurement**:
    *   Tool: `mosdepth` (`--by who_targets.bed --thresholds <min_depth>,30 --no-per-base`)
3.  **Assessability Summary** (`scripts/summarize_coverage.py`):
    *   Interval-level coverage is aggregated to genes as a length-weighted mean, so genes split
        by the repeat mask are reported as one locus.
    *   A gene is **adequate** when the fraction of bases at ≥ `coverage_min_depth` reaches
        `coverage_min_breadth`.
    *   A **drug is assessable only when every one of its catalogue loci is adequate**.
    *   Output: `<sample>.coverage.json`.

**VCF input:** pre-called VCFs carry no alignment, so no coverage can be derived. These samples
receive an explicit `coverage_assessed: false`, and every non-resistant
drug is reported as **Indeterminate** rather than Susceptible.

**Parameters:** `coverage_min_depth` (default 10), `coverage_min_breadth` (default 0.95),
`promoter_padding` (default 200).

## Variant Annotation
Tool: `bcftools`
Variants are matched with data from the WHO TB mutation database to assign drug resistance.
**Annotated Fields:**
*   `GENE`: The gene affected by the variant.
*   `DRUG`: Antibiotics associated with resistance.
*   `EFFECT`: Predicted molecular effect (e.g., missense, frameshift).
*   `WHO_CLASSIFICATION`: Confidence level of resistance association (e.g., "Assoc w R").

## Lineage Classification
Determines the *M. tuberculosis* lineage based on specific SNP barcodes.
1.  **SNP Extraction**:
    *   Extracts variants from the VCF that overlap with known lineage markers defined in the BED file.
2.  **Classification Algorithm**:
    *   **Scoring**: Calculates the percentage of matching SNPs for each lineage.
    *   **Confidence Thresholds**:
        *   **High**: Score ≥ 80% matching SNPs and matched >= 3.
        *   **Medium**: Score ≥ 60% matching SNPs and matched >= 2.
        *   **Low**: Does not meet criteria.

## FHIR Converter
Converts annotated variant calling data into HL7 FHIR R4 standard resources.
1.  **Input Parsing**: Reads annotated VCFs and Lineage JSON results.
2.  **Mapping**:
    *   **Drugs**: Mapped to SNOMED CT codes.
    *   **Variants**: Mapped to HGVS nomenclature.
    *   **Observations**: Uses LOINC codes.
3.  **Resource Creation**:
    *   Generates `Variant Observation`, `Drug Susceptibility Observation`, `Region Studied Observation`, and `Lineage Observation` resources and embeds WHO classification resistance data.
    *   Each variant carries one medication-assessed and clinical-significance component **pair per drug**.
    *   Generates `DiagnosticReport` resource for the conclusion from all variants (e.g., MDR-TB, XDR-TB), plus `Device` and `Provenance` recording the software that produced the calls.

## Upload to FHIR Server
**File:** `upload_fhir.nf`
For uploading FHIR Genomics bundle with clinical metadata. Must grant bearer token first using scripts/get_access_token.py and fill the clinical metadata on each metadata csv (patient, organization, and practitioner). 

## Workflow Parameter 
`nextflow.config` defines all input files, directories, versioning, and specific tool parameters, relative to the base directory ($baseDir).
