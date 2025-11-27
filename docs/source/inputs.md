# Input Requirements

The pipeline accepts three types of input data.

## 1. Illumina Reads
*   **Format**: Paired-end FASTQ files (`.fastq.gz`).
*   **Naming Convention**: `*_1_illumina.fastq.gz` and `*_2_illumina.fastq.gz`.
*   **Location**: Place in `data/NGS/`.

## 2. Nanopore Reads
*   **Format**: Single-end FASTQ files (`.fastq.gz`).
*   **Naming Convention**: `*_ont.fastq.gz`.
*   **Location**: Place in `data/NGS/`.

## 3. Raw VCFs
*   **Format**: VCF files (`.vcf` or `.vcf.gz`).
*   **Location**: Place in `data/VCF/`.
