# Inputs

Give the samples either in a samplesheet (recommended) or as folders with fixed file names.
The genome reference, WHO annotation table, lineage barcode and repeat mask ship with the
pipeline in `data/`.

## Samplesheet

A CSV with the columns `sample,platform,fastq_1,fastq_2,vcf`:

```text
sample,platform,fastq_1,fastq_2,vcf
TB0001,illumina,/data/TB0001_R1.fastq.gz,/data/TB0001_R2.fastq.gz,
TB0002,ont,/data/TB0002.fastq.gz,,
TB0003,vcf,,,/data/TB0003.vcf.gz
```

```bash
nextflow run oucru-id/tb-to-fhir-full -r v2.0.2 -profile docker \
  --input samplesheet.csv --outdir results
```

| `platform` | Needs |
| --- | --- |
| `illumina` | paired-end reads in `fastq_1` and `fastq_2` (`.fastq.gz`) |
| `ont` | one reads file in `fastq_1` (`.fastq.gz`), and `--medaka_model` |
| `vcf` | a VCF in `vcf` (`.vcf` or `.vcf.gz`) |

**Sample ids** may use letters, digits, `.`, `_` and `-`, start with a letter or digit, and be up
to 40 characters long. Each id must be unique, also after conversion to a FHIR id (`TB_1` and
`TB.1` both become `TB-1`).

```{warning}
Use laboratory accessions as sample ids. Sample ids appear in the genomic FHIR output, which is
meant to contain no patient data. The pipeline warns when a sample id looks like a national ID
number.
```

## Folders

```bash
nextflow run . -profile docker --reads_dir /data/NGS --vcf_dir /data/VCF
```

The files in the folders must be named:
- Illumina: `<id>_1_illumina.fastq.gz` and `<id>_2_illumina.fastq.gz`
- ONT: `<id>_ont.fastq.gz`
- VCF: `<id>.vcf` or `<id>.vcf.gz`

## Nanopore reads

ONT input needs `--medaka_model`, for example `r1041_e82_400bps_sup_variant_v5.0.0` for R10.4.1
chemistry. With the container profiles only the models bundled in the medaka image can be given by
name; see [Known limitations](limitations.md#medaka-models-in-containers).

## VCF input

```{warning}
**VCF input cannot produce susceptible calls.** A variant-only VCF records which variants were
*called*, never which regions were *callable*. Coverage therefore cannot be established, and every
non-resistant drug is reported **Indeterminate**. Resistance detection is unaffected. Use FASTQ
input if you need susceptibility results.
```

## Clinical metadata (optional)

Patient, organization and practitioner tables turn the genomic reports into linked FHIR bundles.
They hold personal data and are described in [Clinical metadata](clinical_metadata.md).
