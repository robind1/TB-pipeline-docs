# Overview

[TBtoFHIR](https://github.com/oucru-id/tb-to-fhir-full) is a Nextflow-based workflow designed for the analysis of TB genomic data. It processes raw sequencing data (long-read or short-read) and pre-annotated VCF to identify drug resistance mutations based on the World Health Organization (WHO) database, TB lineages, and generates a FHIR-compliant genomics bundle. 

## Key Features
* **Multi-platform Support**: Processes raw reads and processed data from diverse platforms.
* **Drug Resistance Analysis**:  Identifies mutations associated with TB drug resistance based on WHO's latest [TB mutation database](https://github.com/GTB-tbsequencing/mutation-catalogue-2023/tree/main).
* **Lineage Classification**: Identifies TB lineages based on barcode SNPs.
* **FHIR Compliance**: Generates standardized genomics data exchange formats.
* **Clinical Integration**: Merges genomic data with clinical metadata.
* **Quality Control**: QC reporting with MultiQC.

## Key Outputs
* TB lineage classification
* FHIR genomics bundle (Observations, DiagnosticReport)
* Clinical summary reports
* Quality control metrics

## Directory Structure

```
tb-to-fhir-full
├── main.nf                             # Main workflow
├── nextflow.config                     # Configuration and parameters
├── workflows/
│   ├── illumina.nf                     # Illumina sub-workflow
│   ├── nanopore.nf                     # Nanopore sub-workflow
│   ├── vcf.nf                          # VCF sub-workflow
│   ├── lineage.nf                      # Lineage classification
│   ├── fhir.nf                         # FHIR variants generation
│   ├── validate_fhir.nf                # FHIR validation
│   ├── merge_clinical_data.nf          # Clinical metadata merge
│   ├── upload_fhir.nf                  # FHIR server upload
│   ├── report.nf                       # QC and sample report generation
│   └── utils.nf                        # Utility functions
├── scripts/
│   ├── annotated_to_fhir.py            # VCF-to-FHIR converter
│   ├── clinical_metadata_parser.py     # Patient/org/practitioner parser
│   ├── generate_sample_report.py       # Per-sample text report
│   ├── lineage_classifier.py           # SNP-barcode lineage classifier
│   ├── merge_clinical_fhir.py          # FHIR genomics + clinical data merger
│   ├── upload_fhir.py                  # FHIR uploader
│   ├── get_access_token.py             # Standalone token fetcher
│   ├── get_patient_by_nik.py           # Patient lookup by NIK
│   └── get_versions.py                 # Software version collector
├── data/
│   ├── NGS/                            # Input FASTQ files
│   ├── VCF/                            # Input VCF files
│   ├── H37Rv.fasta                     # Reference genome
│   ├── repetitive_regions.bed          # Exclusion regions
│   ├── *_lineage.bed                   # Lineage barcode SNPs
│   ├── *_annotation_table.tsv.gz       # WHO mutation annotation table
│   ├── patient_clinical_metadata.csv   # Patient metadata
│   ├── organization_metadata.csv       # Organization metadata
│   └── practitioner_metadata.csv       # Practitioner metadata

```
