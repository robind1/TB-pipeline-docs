# FHIR Federated Phylogenetic Analysis

## Overview
The local [phylogenetic analysis pipeline](https://github.com/oucru-id/tb-phylo-analysis-local) does not process raw sequencing reads (FASTQ). Instead, it processes FHIR JSON bundle files containing variant observations. The core logic transforms these variant observations into comparative genomic analyses to infer evolutionary relationships. The pooled coefficient (distance matrix) from each local pipeline could be sent and used to build a global model phylogenetic tree using [global phylogenetic analysis pipeline](https://github.com/oucru-id/global-model-federated-tb).

```{image} _static/Example1-1.png
:alt: Federated concept
:width: 1000px
:align: center
```

## Data Processing (Local pipeline)

```{image} _static/local_pipeline.png
:alt: Local Phylogenetic Analysis Architecture Diagram
:width: 800px
:align: center
```

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

## Tools & Libraries
| Library | Purpose |
| :--- | :--- |
| **Biopython** (`Bio`) | Parsing references, alignment (`MultipleSeqAlignment`), Neighbor Joining (`Phylo`), and reading/writing sequences (`SeqIO`). |
| **Python Std Lib** | `json` for parsing FHIR, `re` for regex parsing of HGVS strings, `csv` for matrix output. |

## Outputs
1.  **`phylo/distance_matrix.tsv`**: SNP differences count between samples.
2.  **`phylo/phylo_tree.nwk`**: Neighbor-joining tree from local analysis.
3.  **`visualization/`**: Static plots (Circular, Rectangular, Unrooted trees) and statistical graphs (Heatmap, Histograms).

## Data Processing (Global pipeline)
This pipeline serves as the aggregation node for the federated analysis. The central node integrates distance matrices and phylogenetic trees from local sites to reconstruct a global phylogenetic tree while preserving data privacy.

```{image} _static/global_pipeline.png
:alt: Local Phylogenetic Analysis Architecture Diagram
:width: 800px
:align: center
```

### 1. Federated Matrix Merging
Reconstruction of a global distance matrix from local matrices using **Anchor**.

*   **Anchor Normalization:** 
    *   The pipeline identifies anchors present across multiple sites (specified in `nextflow.config`).
    *   Calculates correction factors to align sequencing or pipeline-specific batch effects.
*   **Matrix Completion (Imputation):** 
    *   Since distinct labs do not share data directly, the distance between Patient $A_i$ (Lab A) and Patient $B_j$ (Lab B) is unknown.
    *   The pipeline imputes these missing values based on relationships to shared anchors.
    *   **Algorithms:** 
        *   **SoftImpute:** Matrix completion using iterative soft-thresholding of SVD decomposition.

### 2. Topology-Constrained Tree Merging
Constructs a global phylogeny that respects locally resolved topology (inspired by **TreeMerge**).

*   **Input:** Local Newick (`.nwk`) trees and the imputed global distance matrix.
*   **Algorithm:** Constrained Neighbor Joining (NJ).
    *   Local trees act as topological constraints (sub-trees), preserving high-confidence local clusters.
    *   The algorithm resolves relationships between sites using the imputed global matrix values.
*   **Rooting:** 
    *   **Primary:** Outgroup rooting (Default: Lineage 5).
    *   **Fallback:** Midpoint rooting if the outgroup is absent.

### 3. Visualization & Analytics
Generates actionable epidemiological reports. Code implementation found in `scripts/visualize_results.py`.

*   **Transmission Networks:** HTML graphs showing transmission clusters defined by SNP thresholds (12 SNPs).
*   **Phylogenetic Trees:** Rectangular, Circular, and Unrooted layouts.
*   **Statistical Plots:** 
    *   SNP distance distribution histograms and violin plots.
    *   Distance heatmaps.

## Outputs
| Directory | File | Description |
| :--- | :--- | :--- |
| `federated/` | `global_distance_matrix.tsv` | Fully imputed N x N SNP distance matrix. |
| `federated/` | `global_tree.nwk` | Merged phylogenetic tree in Newick format. |
| `visualization/` | `transmission_network.html` | Network graph of outbreak clusters. |
| `visualization/` | `phylo_tree_*.png` | Static tree visualizations (Circular, Rectangular, Unrooted). |
| `visualization/` | `stats_*.png` | Histograms, Heatmaps, and Violin plots of genetic distances. |

```{image} _static/federatedapproach.png
:alt: Rectangular phylogenetic tree TB example local vs federated
:width: 1400px
:align: center
```
Example of a phylogenetic tree generated from the pipeline. Data used: [Afro-TB](https://bioinformatics.um6p.ma/AfroTB/), [Gómez-González et al. 2022](https://doi.org/10.1093/bib/bbac256), [Thorpe et al. 2024](https://doi.org/10.1038/s41598-024-55865-1), [Ghodousi et al. 2025](https://doi.org/10.1038/s41597-025-04966-1)
