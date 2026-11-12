# Known limitations

## Deletions without coordinates

The WHO catalogue grades some large deletions as named entries without genomic coordinates
(`pncA_deletion`, `katG_deletion`, `ethA_deletion` and others). TBtoFHIR matches variants by
coordinate, so these deletions cannot be detected, and some pyrazinamide resistance in particular
is invisible by construction.

The loss-of-function alleles that WHO does list with coordinates (the `*_LoF` entries and named
frameshift and stop-gained variants) are matched and graded with WHO's final grade. A frameshift or
stop codon that the catalogue does not list is not graded.

## Multi-nucleotide variants

Multi-nucleotide variants are dropped by the variant filter (`bcftools view -v snps,indels`).
GATK reports SNVs by default, but a submitted VCF with MNVs loses them.

## Coverage gate covers every catalogue gene

A drug is Susceptible only when **every** catalogue locus for that drug is adequately covered,
including genes that carry no resistance-associated variant. Poor coverage in such a gene makes
the drug Indeterminate. The region-studied Observations and the Indeterminate text name the loci
that blocked the call.

## Lineage without barcode evidence

The barcode's lineage-4 alleles equal the H37Rv reference, so they never appear in a VCF. When no
barcode SNP matches (lineage-4 samples, or poor coverage at the barcode sites), the classifier
reports the first lineage in the barcode file (`lineage4.2.2.1`) with 0 matched SNPs and
confidence `low`. Check `matched_snps` and `confidence` in `lineage/<id>.lineage.json`, or the
lineage Observation's components, before relying on the call.

## Allele frequency depends on the caller

Allele frequency is derived from `INFO/DP4`, `AF` or `AF1`. Callers that report allele depth only
in `FORMAT/AD` yield no frequency, so heteroresistance cannot be assessed for those inputs.

## Genes without an NCBI GeneID

45 WHO catalogue genes have no verified NCBI GeneID and are written as text only. Add verified
ids to `data/gene_ncbi_map.tsv`.
