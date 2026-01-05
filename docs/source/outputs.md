# Data Processing

## Main Workflow
**File:** `main.nf`
The main workflow handles channel processing and parallel execution. It automatically detects input data types (Illumina, Nanopore, or VCF) and routes them to the dedicated sub-workflows. All inputs are processed concurrently.

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
    *   Model: r941_e81_sup_variant_g514
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

## Deeplex Excel Report Workflow
**File:** `deeplex.nf`
For processing Deeplex Myc-TB output files (Excel format)
1.  **Conversion**:
    *   Script: `xlsx_json_converter.py`
    *   Function: Parses Excel sheets ('Drug resistance variants', 'Uncharacterised variants', 'Phylo_Syn variants') to extract variant and lineage data.
    *   Mapping: Maps drugs to SNOMED CT and variants to HGVS nomenclature.
2.  **Clinical Data Merge**:
    *   Script: `merge_clinical_deeplex.py`
    *   Function: Merges observations with clinical metadata.
    *   **Resistance Classification**: Classifies samples (e.g., MDR-TB, XDR-TB) based on detected drug resistance profiles.

## FHIR Converter
Converts annotated variant calling data into HL7 FHIR R4 standard resources.
1.  **Input Parsing**: Reads annotated VCFs and Lineage JSON results.
2.  **Mapping**:
    *   **Drugs**: Mapped to SNOMED CT codes.
    *   **Variants**: Mapped to HGVS nomenclature.
    *   **Observations**: Uses LOINC codes.
3.  **Resource Creation**:
    *   Generates `Observation` resources for each detected variant and embeds WHO classification resistance data.
    *   Generates `DiagnosticReport` resource for the conclusion from all variants.

## Workflow Parameter 
`nextflow.config` defines all input files, directories, versioning, and specific tool parameters, relative to the base directory ($baseDir).
