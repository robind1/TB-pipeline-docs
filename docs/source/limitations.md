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

## Coverage gate works per gene

A drug is Susceptible only when every gene that carries a WHO grade 1-2 variant for it reaches
`--coverage_min_breadth` at `--coverage_min_depth`. The check is per gene so:
- for genes where only a few positions matter (for example `rrl`, `rrs`, `eis` or `embB`), a gap
  elsewhere in the gene can still make the drug Indeterminate;
- a gene can pass at 95% breadth while the missing bases include the resistance-determining codon.

Loss-of-function genes such as `Rv0678`, `pepQ`, `ddn` or `ethA` need the whole gene, so poor
coverage there correctly leaves the drug Indeterminate. The region-studied Observations and the
Indeterminate text name the loci that blocked the call.

## Lineage barcode

- The barcode (`data/2026-05-11_lineage.bed`) has no `lineage4.10`; isolates that newer barcodes
  call 4.10 are reported as one of the lineages it contains or as `lineage4`.
- Mixed-infection detection uses the barcode sites only: two strains of the same sublineage, or a
  minor strain below about 10%, are not flagged.
- For VCF input the classifier cannot see coverage, so it assumes a barcode site missing from a
  genome-wide VCF is the reference. Calls that depend on this are marked `reference_inferred`.

## Allele frequency depends on the caller

Allele frequency is derived from `INFO/DP4`, `AF` or `AF1`. Callers that report allele depth only
in `FORMAT/AD` yield no frequency, so heteroresistance cannot be assessed for those inputs.

## Genes without an NCBI GeneID

45 WHO catalogue genes have no verified NCBI GeneID and are written as text only. Add verified
ids to `data/gene_ncbi_map.tsv`.
