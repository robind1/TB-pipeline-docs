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

## Coverage gate on loss-of-function loci

Loci whose graded variants for a drug include loss-of-function alleles (for example `katG`,
`ethA`, `pncA`, `Rv0678`, `pepQ` or `ddn`) are checked over the whole gene, because a frameshift or
stop codon anywhere in the gene can cause resistance. Such a locus passes at
`--coverage_min_breadth` (95%), so the missing bases can still include a graded codon such as
`katG` S315.

The other gating loci (for example `rpoB`, `rrs`, `eis` or `embB`) are checked at their WHO grade
1-2 positions only, so a gap elsewhere in those genes does not make the drug Indeterminate. A
variant outside those positions has no grade 1-2 for the drug and could not make it Resistant, so
the catalogue call loses nothing. The region-studied Observations and the Indeterminate text name
the loci, and for position-gated loci the positions, that blocked the call.

## Lineage barcode

- The barcode (`data/2026-05-11_lineage.bed`) has no `lineage4.10`; isolates that newer barcodes
  call 4.10 are reported as one of the lineages it contains or as `lineage4`.
- Mixed-infection detection uses the barcode sites only: two strains of the same sublineage, or a
  minor strain below about 10%, are not flagged.
- For VCF input the classifier cannot see coverage, so it assumes a barcode site missing from a
  genome-wide VCF is the reference. Calls that depend on this are marked `reference_inferred`.

## Medaka models in containers

The medaka 2.1.0 image bundles four models:
- `r1041_e82_400bps_sup_variant_v5.0.0`
- `r1041_e82_400bps_hac_variant_v5.0.0`
- `r1041_e82_400bps_sup_v5.2.0`
- `r1041_e82_400bps_hac_v5.2.0`

With `-profile docker`, `podman`, `singularity` or `apptainer`, any other model name makes
`MEDAKA_VARIANT` fail, because medaka cannot download the model into the read-only container.
For another model, download the model file beforehand, give its path in `--medaka_model`, and make
that folder visible in the container (with docker, for example,
`docker.runOptions = '-v /path/to/models:/path/to/models'`).

## Allele frequency depends on the caller

Allele frequency is derived from `INFO/DP4`, `AF` or `AF1`. Callers that report allele depth only
in `FORMAT/AD` yield no frequency, so heteroresistance cannot be assessed for those inputs.

## Genes without an NCBI GeneID

45 WHO catalogue genes have no verified NCBI GeneID and are written as text only. Add verified
ids to `data/gene_ncbi_map.tsv`.
