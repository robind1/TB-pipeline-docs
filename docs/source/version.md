# Version

## Pipeline version

**2.0.0**

## Software

| Tool | Version |
| --- | --- |
| FastQC | 0.12.1 |
| Trimmomatic | 0.39 |
| bwa-mem2 | 2.2.1 |
| minimap2 | 2.26 |
| samtools | 1.19.2 |
| GATK | 4.4.0.0 |
| medaka | 2.1.0 |
| chopper | 0.12.0 |
| NanoPlot | 1.48.0 (new in 2.0) |
| bcftools | 1.19 |
| mosdepth | 0.3.6 |
| MultiQC | 1.30 |
| HL7 FHIR validator | 6.5.26 |
| Python / Java | 3.12 / 21 |

The versions used in a run are collected in `pipeline_info/software_versions.yml`.

## Reference data

### Reference genome

- *Mycobacterium tuberculosis* H37Rv,
  [NC_000962.3](https://www.ncbi.nlm.nih.gov/nuccore/NC_000962.3) (`data/H37Rv.fasta`)
- Repeat mask: PE/PPE genes and insertion sequences (`data/repetitive_regions.bed`)

### WHO mutation catalogue

- [Catalogue of mutations in *Mycobacterium tuberculosis* complex and their association with drug
  resistance, 2nd edition](https://www.who.int/publications/i/item/9789240082410) (WHO, 2023),
  spreadsheet `WHO-UCN-TB-2023.xlsx`
  ([GTB-tbsequencing/mutation-catalogue-2023](https://github.com/GTB-tbsequencing/mutation-catalogue-2023))
- Annotation table `data/2026-11-12_annotation_table.tsv.gz`, built from the catalogue's
  **final** confidence grading

### Lineage barcode

- TBProfiler SNP barcode ([jodyphelan/TBProfiler](https://github.com/jodyphelan/TBProfiler)),
  `data/2026-05-11_lineage.bed`

## Changelog

See [CHANGELOG.md](https://github.com/oucru-id/tb-to-fhir-full/blob/2.0.0-dev/CHANGELOG.md).

## References

1. World Health Organization (2023). *Catalogue of mutations in Mycobacterium tuberculosis complex
   and their association with drug resistance, 2nd ed.*
   [WHO publication](https://www.who.int/publications/i/item/9789240082410).
2. Phelan, J. E., et al. (2019). *Integrating informatics tools and portable sequencing technology
   for rapid detection of resistance to anti-tuberculous drugs*.
   [Genome Medicine](https://link.springer.com/article/10.1186/s13073-019-0650-x).
3. Napier, G., et al. (2020). *Robust barcoding and identification of Mycobacterium tuberculosis
   lineages for epidemiological and clinical studies*.
   [Genome Medicine](https://link.springer.com/article/10.1186/s13073-020-00817-3).
4. Di Tommaso, P., et al. (2017). *Nextflow enables reproducible computational workflows*.
   [Nature Biotechnology](https://www.nature.com/articles/nbt.3820).
5. Li, H., et al. (2009). *The Sequence Alignment/Map format and SAMtools*.
   [Bioinformatics](https://academic.oup.com/bioinformatics/article/25/16/2078/204688).
6. HL7 International. *Genomics Reporting Implementation Guide 3.0.0*.
   [hl7.org](https://hl7.org/fhir/uv/genomics-reporting/STU3/).
