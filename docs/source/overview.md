# Overview

This pipeline is a Nextflow-based bioinformatics workflow designed for TB genomic analysis. It processes raw sequencing data (long-read or paired short-read) to identify drug resistance mutations based on World Health Organization (WHO) database, TB lineages, and generate FHIR-compliant genomics reports. 

It supports data ingestion from multiple sequencing technologies (Illumina and Oxford Nanopore) as well as raw VCF files. The pipeline also could ingest processed VCF files from EPI2-ME platform and Deeplex® Myc-TB platform (testing).

## Key Features
* **Multi-platform Support**: Processes raw reads and processed data from other platforms.
* **Drug Resistance Analysis**:  Identifies mutations associated with TB drug resistance based on WHO latest TB mutation database (https://github.com/GTB-tbsequencing/mutation-catalogue-2023/tree/main).
* **Lineage Classification**: Identifies TB lineages based on barcode SNPs.
* **FHIR Compliance**: Generates standardized genomics data exchange formats.
* **Clinical Integration**: Merges genomic data with clinical metadata.
* **Quality Control**: QC reporting with MultiQC.

## Key Outputs
* TB lineage classification results.
* FHIR-compliant genomic reports. 
* Clinical summary reports. 
* Quality control metrics. 