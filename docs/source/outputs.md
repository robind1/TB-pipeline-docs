# Outputs

## Output directory

```text
results/
├── pipeline_info/          execution report, timeline, trace, DAG, software_versions.yml
├── qc/fastqc/              FastQC reports (Illumina)
├── qc/nanoplot/            <id>_NanoStats.txt, <id>_NanoPlot-report.html (ONT)
├── qc/multiqc/             multiqc_report.html
├── qc/coverage/            who_targets.bed, who_positions.bed, <id>.coverage.json, mosdepth beds
├── variants/               <id>.filtered_variants.vcf.gz, <id>.annotated_variants.vcf.gz
├── lineage/                <id>.lineage.json
├── reports/                <id>.summary_report.txt
└── fhir/
    ├── genomic/            <id>.genomic.fhir.json                      (no patient data)
    ├── clinical/           clinical resources, clinical_summary.tsv    (personal data)
    ├── bundle/             <id>.bundle.fhir.json, link_summary.tsv     (personal data)
    ├── validation/         validation_summary.tsv, validation_<n>.json
    └── upload/             <id>.bundle.upload.json
```

## FHIR output layers

| Step | Output | Contains |
| --- | --- | --- |
| genomic (always) | `fhir/genomic/<id>.genomic.fhir.json` | DiagnosticReport; variant, susceptibility-panel, region-studied and lineage Observations; Device; Provenance. **No patient data**: the subject is the reference `Patient/<id>-patient`. |
| clinical (with `--patient_metadata`) | `fhir/clinical/` | Patient, Specimen, Encounter and ServiceRequest per sample; Organization, Practitioner and PractitionerRole once. **Personal data.** |
| link (with `--patient_metadata`) | `fhir/bundle/<id>.bundle.fhir.json` | One FHIR `transaction` per sample, with every reference resolved inside the bundle. **Personal data.** |

The genomic bundle is a FHIR `collection`. The codes in each resource are listed on
[FHIR standards](FHIR.md).

## Genomic bundle

### Variant Observation

One per detected variant, LOINC `69548-6` (Genetic variant assessment), with the Genomics
Reporting `variant` profile. Components:
- **Genomic DNA change (gHGVS)**, e.g. `NC_000962.3:g.761155C>T` (LOINC `81290-9`)
- **Variant exact start-end** (LOINC `81254-5`)
- **Gene studied** (LOINC `48018-6`), coded with the NCBI GeneID where one is verified
- **DNA change type** (LOINC `48019-4`), a Sequence Ontology term such as `missense_variant`
- **Medication assessed** (LOINC `51963-7`, SNOMED CT drug) and **clinical significance**
  (LOINC `53037-8`, the WHO grade): one pair **per drug**
- **WHO variant name**, e.g. `rpoB_p.Ser450Leu`:
  - `generic`: its own component, `who-variant-id`
  - `satusehat`: amino acid change (LOINC `48005-3`)
- **Genomic reference sequence** (LOINC `48013-7`)
- **Allelic read depth** (LOINC `82121-5`) and **allele frequency** (LOINC `81258-6`)
- **Variant call quality (QUAL)** and **mapping quality (MQ)**, `variant-quality` and
  `mapping-quality`

```{note}
**Per-drug grading.** The WHO catalogue grades each (variant, drug) pair separately. A variant
graded for several drugs carries a medication / clinical-significance pair for each, so a
*pepQ* loss-of-function variant can be *Assoc w R* for bedaquiline and *Uncertain significance*
for clofazimine in the same Observation.
```

### Drug susceptibility panel

One Observation, LOINC `89486-5`, with a component per drug (17 drugs; see
[FHIR standards](FHIR.md#drug-susceptibility-codes)). Each drug has one of **three** values:

| State | LOINC | Meaning |
| --- | --- | --- |
| **Resistant** | `LA6676-6` | A variant graded *Assoc w R* or *Assoc w R - Interim* (WHO group 1 or 2) was detected |
| **Susceptible** | `LA24225-7` | No such variant **and** every gating locus for that drug met the coverage threshold |
| **Indeterminate** | `LA9663-1` | No such variant, but coverage of the gating loci was not confirmed |

```{warning}
**Absence of a resistance mutation is not evidence of susceptibility.** `Susceptible` is only
reported when the drug's gating loci, the genes that carry a WHO grade 1-2 variant for it, were
sequenced to the configured depth and breadth (loss-of-function loci) or to the configured depth
at every graded position (the others; see
[Coverage assessment](components.md#coverage-assessment)).
Otherwise the result is `Indeterminate`. An Indeterminate component names the loci that blocked
the call, and the position for a position-gated locus.
```

### Region-studied Observations

One per gene, LOINC `53041-0` (DNA region of interest panel). They record which resistance loci
were examined, which is the evidence behind a negative result. Components:
- **Gene studied** (LOINC `48018-6`)
- **Mean depth** (LOINC `82121-5`)
- **Fraction of bases at ≥ *N*×**, `coverage-breadth` (percent)

```{note}
Breadth is a **gene-level** summary. A gene may read 96% covered while the missing 4% includes
the resistance-determining codon. For position-gated loci the susceptible call checks the graded
positions themselves; their counts are in `qc/coverage/<id>.coverage.json`
(`graded_positions_at_min_depth`). Per-base detail is in the mosdepth files in `qc/coverage/`.
```

### Lineage Observation

LOINC `614-8`. The value is the lineage from the barcode classifier, e.g. `lineage4.3.3`, coded in
the project `mtb-lineage` CodeSystem (`satusehat` adds a `http://tb-lineage.org` coding). When the
lineage is `unknown`, the Observation is left out. Components:

| Component | Value |
| --- | --- |
| `lineage-family` | e.g. *Euro-American* |
| `lineage-confidence` | *high*, *medium* or *low* |
| `lineage-score` | mean allele fraction of the called lineage's barcode markers, 0.0–1.0 |
| `barcode-snps-matched` | barcode markers of the called lineage that are present |
| `barcode-snps-total` | barcode markers of the called lineage |

`lineage/<id>.lineage.json` holds more detail: the path from main lineage to the call
(`lineage_path`), the evidence used (`pileup` or `vcf`), `possible_mixed_infection` with the
`minor_lineages` seen at 10-50% allele fraction, `ambiguous_sublineages`, and a `reason` when the
lineage is `unknown`.

### DiagnosticReport

- **Profile and code**:
  - `generic`: `genomic-report`, LOINC `51969-4` (Genetic analysis report), with `81247-9` as a
    second coding
  - `satusehat`: `genomics-report`, LOINC `81247-9`
- **Conclusion**: the resistance classification (below) and the lineage, as text and as
  `conclusionCode`. Drugs that could not be assessed are named.
- **presentedForm**: an HTML report, base64-encoded.
- **performer**: the Organization given by `--performer_org_id`, if any.

### Device and Provenance

- **Device**: TBtoFHIR, its version, source repository and filter settings, SNOMED CT
  `706689003` (Application program software).
- **Provenance**: one per sample, targeting the DiagnosticReport and every Observation it rests
  on, with the software as `assembler` and the performing Organization as `performer`.

## Clinical resources and linked bundle

With `--patient_metadata`, the clinical step adds Patient, Specimen, Encounter and
ServiceRequest per sample, and Organization, Practitioner and PractitionerRole. With
`--fhir_profile satusehat` they carry the Kemkes profiles, NIK identifiers and Kemkes extensions.

The link step writes one FHIR `transaction` per sample in `fhir/bundle/`, joining the genomic
report to the ServiceRequest, Encounter, Organization and Practitioner. See
[Clinical metadata](clinical_metadata.md#what-the-link-step-adds).

## Drug resistance classification

The DiagnosticReport conclusion is the first class that applies, in this order:

| Classification | Criteria |
| --- | --- |
| **No resistance detected** | No resistance variant, and **all** drug groups were assessable |
| **No resistance detected - partial** | No resistance variant, but some drugs could not be assessed |
| **Indeterminate** | No resistance variant, and no drug could be assessed |
| **Drug-resistant - rifampicin not assessable** | Resistance detected, but rifampicin could not be assessed, so RR/MDR/pre-XDR/XDR cannot be decided |
| **XDR-TB** | MDR or RR, plus fluoroquinolone resistance, plus Group A drug resistance |
| **Pre-XDR-TB** | MDR or RR, plus fluoroquinolone resistance |
| **MDR-TB** | Resistance to both isoniazid and rifampicin |
| **RR-TB** | Rifampicin resistance without isoniazid resistance |
| **HR-TB** | Isoniazid resistance, rifampicin **assessed and susceptible** |
| **Streptomycin-, Ethionamide-, Pyrazinamide-, Ethambutol- or Ciprofloxacin-resistant TB** | Resistance to that drug (group) only |
| **Drug-resistant** | Any other resistance combination |

```{warning}
The classes that depend on rifampicin (RR, MDR, pre-XDR, XDR) are only asserted when rifampicin
itself was assessable. An Indeterminate rifampicin blocks the classification instead of falling
through to a lower class. "Sensitive" is never reported.
```
