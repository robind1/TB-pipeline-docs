# Overview

This pipeline is a Nextflow-based workflow designed for the analysis of TB genomic data. It processes raw sequencing data (long-read or short-read), pre-annotated VCF, and Deeplex excel sheet to identify drug resistance mutations based on the World Health Organization (WHO) database, TB lineages, and generates a FHIR-compliant genomics bundle. 

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

