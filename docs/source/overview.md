# Overview

[TBtoFHIR](https://github.com/oucru-id/tb-to-fhir-full) is a Nextflow pipeline for
*Mycobacterium tuberculosis* genomic analysis from raw sequencing data or VCFs. It produces
WHO-catalogue drug-resistance calls, lineage and coverage QC, and reports them as HL7 FHIR R4
resources that conform to the
[Genomics Reporting IG 3.0.0](https://hl7.org/fhir/uv/genomics-reporting/STU3/).

## Key features

- **Multi-platform input**: Illumina paired-end reads, Oxford Nanopore reads, or VCFs, given in
  one samplesheet.
- **Per-drug WHO grading**: grades come from the final grading of the WHO mutation catalogue
  (2nd edition, 2023).
- **Coverage-gated susceptibility**: a drug is reported susceptible only when every locus that
  carries a WHO grade 1-2 (associated with resistance) variant for that drug was sequenced to the
  required depth. Loci whose graded variants for the drug include loss-of-function alleles need the required breadth over the whole locus;
  for the other loci every graded position must reach the required
  depth. Otherwise it is **Indeterminate**.
- **Lineage classification** from barcode SNPs, with confidence and SNP support.
- **QC**: FastQC (Illumina) or NanoPlot (ONT), MultiQC, and per-locus coverage over the WHO
  resistance targets.
- **Genomic FHIR without patient data, by default.** The genomic report refers to the patient by
  id only. Clinical resources are built in a separate, optional step and joined to the genomic
  report in a third step.
- **Two FHIR profiles**:
  - `generic` (default): plain HL7 Genomics Reporting.
  - `satusehat`: conforming to the Indonesian Ministry of Health SATUSEHAT platform (Kemkes
    profiles, NIK identifiers, Kemkes codings).

## What a run produces

For each sample:
- a drug-susceptibility panel (Resistant, Susceptible or Indeterminate for each drug)
- the lineage call
- per-locus coverage over the WHO resistance targets
- a FHIR genomic bundle (`fhir/genomic/<id>.genomic.fhir.json`) with no patient data
- with clinical metadata, a FHIR `transaction` bundle that links the genomic report to the
  patient, specimen and encounter

## Repository layout

```text
tb-to-fhir-full
├── main.nf                  entry point
├── workflows/tbfhir.nf      main workflow
├── subworkflows/local/      illumina, nanopore, prepare_reference, coverage, lineage, fhir
├── modules/local/           one process per tool or step
├── bin/                     Python steps (genomic, clinical, link, coverage, lineage, upload)
├── conf/                    resources, output layout, test profiles
├── assets/                  samplesheet schema, FHIR CodeSystems, metadata templates
├── data/                    reference genome, WHO annotation table, lineage barcode, masks
├── tools/annotation/        rebuild the WHO annotation table
├── tools/metadata_ui/       Streamlit editor for the clinical metadata table
├── tools/satusehat/         SATUSEHAT token and patient-lookup helpers
├── tests/                   pytest suite, synthetic fixtures, v1 equivalence goldens
├── nextflow.config          parameters and profiles
└── nextflow_schema.json     parameter schema
```
