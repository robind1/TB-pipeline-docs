# Version

## Pipeline Version
* **Current Version:** 1.2.0

## Software Dependencies
The pipeline integrates several bioinformatics tools. Specific versions used in your run are automatically captured in the `software_versions.yml`.

## Reference Data
### TB Reference Genome
*   **Strain**: *Mycobacterium tuberculosis* H37Rv
*   **Accession**: [NC_000962.3](https://www.ncbi.nlm.nih.gov/nuccore/NC_000962.3)
*   **Description**: The standard reference genome used for coordinate mapping and variant calling.

### Mutation Catalogue
*   **Source**: WHO-UCN-TB-2023 Mutation Catalogue
*   **Version**: May 2024 Update
*   **Repository**: [GTB-tbsequencing/mutation-catalogue-2023](https://github.com/GTB-tbsequencing/mutation-catalogue-2023)

### Lineage Barcodes
*   **Source**: TBProfiler SNP Panel
*   **Repository**: [jodyphelan/TBProfiler](https://github.com/jodyphelan/TBProfiler)
*   **Description**: A curated set of SNPs used for phylogenetic lineage and sub-lineage classification.

## References
1.  World Health Organization. (2023). *Catalogue of mutations in Mycobacterium tuberculosis complex and their association with drug resistance, 2nd ed*. [WHO Publication](https://www.who.int/publications/i/item/9789240082410)
2.  Phelan, J. E., et al. (2019). *Integrating informatics tools and portable sequencing technology for rapid detection of resistance to anti-tuberculous drugs*. [Genome Medicine](https://link.springer.com/article/10.1186/s13073-019-0650-x).
3.  Di Tommaso, P., et al. (2017). *Nextflow enables reproducible computational workflows*. [Nature Biotechnology](https://www.nature.com/articles/nbt.3820).


