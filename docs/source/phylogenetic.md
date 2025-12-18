# FHIR Phylogenetic Analysis

## Overview
The [phylogenetic analysis pipeline](https://github.com/oucru-id/tb-phylo-analysis) does not process sequencing data. Instead, it processes FHIR JSON bundle files. The core logic transforms the variant observations into a comparative genomic analysis to get evolutionary relationships.

```{image} _static/tbphyloflow.png
:alt: Phylogenetic Analysis Architecture Diagram
:width: 700px
:align: center
```

## Data Processing
### 1. FHIR Data Ingestion & Parsing
The pipeline iterates through input FHIR JSON bundle. For each file, it extracts:

*   **Metadata:**
    *   **Patient ID:** Extracted from `Patient` resources.
    *   **Geolocation:** Latitude and Longitude extracted from `Patient` address extensions.
    *   **Conclusion:** Extracted from `DiagnosticReport` resources.
*   **Genomic Variants:**
    *   The script scans `Observation` resources for LOINC code `69548-6` (Genetic variant).
    *   It parses specific components (LOINC `81254-5`) for genomic position and HGVS strings (e.g., `g.7654A>T`) to identify the alternative allele.

### 2. Pseudo-Sequence Mapping
Common analysis pipelines utilize consensus genomes, but this pipeline builds **pseudo-sequences** based on the all variants found in the FHIR JSON bundle.
1.  **Variant Union:** The script identifies every unique genomic position where *at least one* sample in the dataset has a variant.
2.  **Sequence Generation:** For every sample, a sequence string is generated corresponding to these sorted positions:
    *   If the sample has a variant at position $P$, the **Alternative** allele is used.
    *   If the sample has no record for position $P$, the **Reference** allele (from the reference FASTA) is used.
    *   If the position exceeds the reference length, 'N' is used.

The output is a Multiple Sequence Alignment (MSA) of variable sites (SNPs) relative to the MTB H37Rv reference genome (NC_000962.3).

## Algorithm
### Distance Matrix Calculation
*   **Metric:** Hamming Distance (SNP Distance).
*   **Calculation:** For every pair of samples, the distance is the count of positions in their pseudo-sequences where the nucleotides differ.
*   **Output:** Matrix with `snp-dists` format.

### Phylogenetic Tree Inference
1.  **Distance Calculation:** The `Bio.Phylo` computes the distance matrix from the MSA.
2.  **Tree Construction:** The **Neighbor Joining (NJ)** method is used.
3.  **Output:** The resulting tree is saved in **Newick (.nwk)** format.

## Tools & Libraries
| Library | Purpose |
| :--- | :--- |
| **Biopython** (`Bio`) | Reading FASTA references (`SeqIO`), handling sequences (`SeqRecord`), creating alignments (`MultipleSeqAlignment`), and Neighbor Joining algorithm (`Phylo`). |
| **Python Standard Library** | `json` for parsing FHIR, `re` for regex parsing of HGVS strings, `csv` for matrix output. |

## Outputs
1.  **`distance_matrix.tsv`**: Representing the number of SNP differences between every pair of samples.
2.  **`phylo_tree.nwk`**
3.  **`metadata.tsv`**: Sample metadata including Patient ID, Geolocation, and Lineage/Conclusion.
4.  **Visualization:** png rendering of the phylogenetic tree (circular, rectangular, and unrooted), heatmap of SNP distances, histogram of SNP distances, and violin plot.

```{image} _static/phylo_tree_rectangular.png
:alt: Rectangular phylogenetic tree TB example
:width: 1200px
:align: center
```
Example of a phylogenetic tree generated from the pipeline. Data used: [Afro-TB](https://bioinformatics.um6p.ma/AfroTB/), [Gómez-González et al. 2022](https://doi.org/10.1093/bib/bbac256), [Thorpe et al. 2024](https://doi.org/10.1038/s41598-024-55865-1)
