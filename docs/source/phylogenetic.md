# FHIR Federated Phylogenetic Analysis

## Overview
The [phylogenetic analysis pipeline](https://github.com/oucru-id/tb-phylo-analysis) does not process raw sequencing reads (FASTQ). Instead, it processes FHIR JSON bundle files containing variant observations. The core logic transforms these variant observations into comparative genomic analyses to infer evolutionary relationships.

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
    *   It parses specific components gHGVS strings to identify the alternative allele.

### 2. Pseudo-Sequence Mapping
Common analysis pipelines utilize consensus genomes, but this pipeline builds **pseudo-sequences** based on the all variants found in the FHIR JSON bundle.
1.  **Variant Union:** The script identifies every gHGVS where *at least one* sample in the dataset has a variant.
2.  **Sequence Generation:** For every sample, a sequence string is generated corresponding to these sorted positions:
    *   If the sample has a variant at position $P$, the **Alternative** allele is used.
    *   If the sample has no record for position $P$, the **Reference** allele (from the reference FASTA) is used.
    *   If the position exceeds the reference length, 'N' is used.

The output is a Multiple Sequence Alignment (MSA) of variable sites (SNPs) relative to the MTB H37Rv reference genome (NC_000962.3).

## Algorithms

### Standard Analysis (Local)
*   **Distance Matrix:** 
    *   **Metric:** Hamming Distance (SNP Distance) calculated from SNP Pseudo-Sequences.
    *   **Output:** Matrix in `snp-dists` format.
*   **Phylogenetic Tree:** 
    *   **Method:** Neighbor Joining (NJ) using `Bio.Phylo` on the distance matrix.
    *   **Output:** Newick (`.nwk`) format.

### Federated Analytics (Nextstrain/Augur)
The pipeline integrates **Nextstrain Augur** to generate files suitable for federated analytics and visualization.

1.  **Tree Inference (`augur tree`):** Constructs a tree from the full consensus genomes (rebuild from pseudo-sequences).
2.  **Refinement (`augur refine`):** Optimizes branch lengths.
3.  **Trait Inference (`augur traits`):** Reconstructs ancestral states for metadata fields like Lineage.
4.  **Export (`augur export`):** Packages the tree, metadata, and ancestral states into a single JSON (`tb_analysis.json`) for visualization in Auspice.

## Tools & Libraries
| Library | Purpose |
| :--- | :--- |
| **Biopython** (`Bio`) | Parsing references, alignment (`MultipleSeqAlignment`), Neighbor Joining (`Phylo`), and reading/writing sequences (`SeqIO`). |
| **Augur** | Nextstrain bioinformatics toolkit for phylogenetic inference and Auspice export. |
| **Python Std Lib** | `json` for parsing FHIR, `re` for regex parsing of HGVS strings, `csv` for matrix output. |

## Outputs
1.  **`phylo/distance_matrix.tsv`**: SNP differences count between samples.
2.  **`phylo/phylo_tree.nwk`**: Neighbor-joining tree from local analysis.
3.  **`nextstrain_build/tb_analysis.json`**: Auspice-compatible JSON for federated visualization.
4.  **`visualization/`**: Static plots (Circular, Rectangular, Unrooted trees) and statistical graphs (Heatmap, Histograms).

```{image} _static/phylo_tree_rectangular.png
:alt: Rectangular phylogenetic tree TB example
:width: 1200px
:align: center
```
Example of a phylogenetic tree generated from the pipeline. Data used: [Afro-TB](https://bioinformatics.um6p.ma/AfroTB/), [Gómez-González et al. 2022](https://doi.org/10.1093/bib/bbac256), [Thorpe et al. 2024](https://doi.org/10.1038/s41598-024-55865-1)
