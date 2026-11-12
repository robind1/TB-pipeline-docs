# Configuration

Every parameter is defined in
[`nextflow_schema.json`](https://github.com/oucru-id/tb-to-fhir-full/blob/2.0.0-dev/nextflow_schema.json)
and listed by `nextflow run . --help`. Values are checked against the schema before anything runs.

## Most used parameters

| Parameter | Default | Purpose |
| --- | --- | --- |
| `--input` | | samplesheet (see [Inputs](inputs.md)) |
| `--outdir` | `results` | output folder |
| `--fhir_profile` | `generic` | `generic` or `satusehat` (see [FHIR standards](FHIR.md)) |
| `--patient_metadata` | | enables the clinical and link steps |
| `--performer_org_id` | | performing laboratory, as the genomic report's performer |
| `--medaka_model` | | required for ONT input |
| `--coverage_min_depth` / `--coverage_min_breadth` | `10` / `0.95` | assessability threshold per locus |
| `--filter_min_depth` / `--filter_min_quality` | `5` / `20` | variant call filters |
| `--skip_fhir_validation` | `false` | skip the HL7 FHIR validator |
| `--max_cpus` / `--max_memory` / `--max_time` | `8` / `16 GB` / `24h` | cap on any single task |

## All parameters

### Input and output

| Parameter | Default | Description |
| --- | --- | --- |
| `input` | | Samplesheet CSV with columns `sample,platform,fastq_1,fastq_2,vcf`. |
| `reads_dir` | | Folder input: `<id>_1_illumina.fastq.gz` / `<id>_2_illumina.fastq.gz` and `<id>_ont.fastq.gz` files. |
| `vcf_dir` | | Folder input: `<id>.vcf` or `<id>.vcf.gz` files. |
| `outdir` | `results` | Output directory. (`--results_dir` was removed in 2.0.0.) |

### Reference data

| Parameter | Default | Description |
| --- | --- | --- |
| `reference` | `data/H37Rv.fasta` | H37Rv reference genome (NC_000962.3). |
| `annotation_table` | `data/2026-11-12_annotation_table.tsv.gz` | bgzipped, tabix-indexed WHO catalogue annotation table. The `.tbi` must sit next to it. |
| `annotation_header` | `data/2026-11-12_annotations_header.txt` | VCF header lines for the annotation table columns. |
| `lineage_barcode` | `data/2026-05-11_lineage.bed` | Lineage barcode SNP BED. |
| `repetitive_regions` | `data/repetitive_regions.bed` | Repetitive regions (PE/PPE, insertion sequences) excluded from variant calls. Point at `assets/NO_FILE` to disable masking. |
| `gene_map` | `data/gene_ncbi_map.tsv` | Gene to NCBI GeneID map, extending the built-in one. |

### Read processing

| Parameter | Default | Description |
| --- | --- | --- |
| `trimmomatic_jar` | | Path to `trimmomatic.jar` when the `trimmomatic` command is not on `PATH`. |
| `nanopore_min_q` | `10` | chopper minimum read quality. |
| `nanopore_min_l` | `500` | chopper minimum read length. |
| `medaka_model` | | medaka model; required for ONT input (e.g. `r1041_e82_400bps_sup_variant_v5.0.0`). |
| `medaka_batch_size` | `100` | medaka inference batch size. |

### Variant filters and coverage

| Parameter | Default | Description |
| --- | --- | --- |
| `filter_min_depth` | `5` | Minimum read depth (DP) of a variant call. |
| `filter_min_quality` | `20` | Minimum call quality: QUAL for Illumina (GATK), GQ for ONT (medaka), GQ or QUAL for VCF input. |
| `coverage_min_depth` | `10` | Depth at which a base of a resistance locus counts as covered. |
| `coverage_min_breadth` | `0.95` | Fraction of a locus that must be covered for a drug to be assessable (otherwise Indeterminate). |
| `promoter_padding` | `200` | Padding (bp) around catalogue variant clusters when building coverage targets. |

### FHIR output

| Parameter | Default | Description |
| --- | --- | --- |
| `fhir_profile` | `generic` | `generic`: HL7 Genomics Reporting IG 3.0.0 only. `satusehat`: adds Kemkes profiles, NIK identifiers and codings. |
| `performer_org_id` | | FHIR id of the performing laboratory Organization, used as performer in the genomic bundles. |
| `performer_org_name` | | Display name for the performing laboratory. |
| `identifier_system_base` | | Base URI for business identifiers in the generic profile (none are emitted if unset). |

### Clinical metadata (optional, contains personal data)

| Parameter | Default | Description |
| --- | --- | --- |
| `patient_metadata` | | Patient table (CSV or XLSX); see [Clinical metadata](clinical_metadata.md). |
| `organization_metadata` | | Performing organization (first row is used). |
| `practitioner_metadata` | | Responsible practitioner (first row is used). |
| `external_refs` | | JSON `{fhir_id: {"Patient": "<server id>", "Encounter": "<server id>"}}` for resources that already exist on the server. |
| `require_clinical` | `false` | Fail when a sample has no row in the patient table (default: warn, genomic bundle only). |
| `bundle_request_method` | `PUT` | `PUT` or `POST`. POST uses server-assigned ids and `ifNoneExist` on NIK (SATUSEHAT). |
| `publish_clinical` | `true` | Publish the clinical resources to `<outdir>/fhir/clinical`. |

### FHIR validation

| Parameter | Default | Description |
| --- | --- | --- |
| `skip_fhir_validation` | `false` | Do not run the HL7 FHIR validator. |
| `fhir_validator` | pinned HAPI FHIR core release | `validator_cli.jar`: a local path or a URL. |
| `fhir_ig` | `hl7.fhir.uv.genomics-reporting#3.0.0` | Implementation guide package to validate against. |
| `fhir_tx_server` | `n/a` | Terminology server for code validation; `n/a` validates offline and sends nothing. |
| `fail_on_validation_error` | `true` for generic, `false` for satusehat | Stop the run when a bundle has validation errors. |
| `fhir_validation_batch_size` | `50` | Files validated per validator process. |

### FHIR upload

| Parameter | Default | Description |
| --- | --- | --- |
| `fhir_server_url` | | FHIR server base URL. Upload runs only when this is set. |
| `fhir_auth_url` | | OAuth2/OIDC realm URL for the client-credentials token. |
| `fhir_upload_api_key` | `false` | Also send the `TBFHIR_API_KEY` secret as an `X-Api-Key` header. |

Credentials are Nextflow secrets; see [Installation](installation.md#uploading-to-a-fhir-server).

### Resource limits

| Parameter | Default | Description |
| --- | --- | --- |
| `max_cpus` | `8` | Most CPUs any task may request. |
| `max_memory` | `16 GB` | Most memory any task may request. |
| `max_time` | `24h` | Longest any task may run. |
| `trace_report_suffix` | start time | Suffix for the `pipeline_info` report file names. |

Tasks that run out of memory are retried with more memory, up to `--max_memory`.

## WHO annotation table

Drug resistance is graded with a table built from the WHO catalogue of mutations
(2nd edition, 2023, `WHO-UCN-TB-2023.xlsx`):
- The grade for each (variant, drug) pair is the catalogue's **final** confidence grading. This
  includes WHO's additional grading criteria: the loss-of-function rule, cross-resistance and
  WHO-endorsed assays.
- The table has **one row per allele**, with positionally aligned `DRUG` /
  `WHO_CLASSIFICATION` / `VARIANT_ID` arrays.

To rebuild it, put the WHO spreadsheet at `data/WHO-UCN-TB-2023.xlsx` and run:

```bash
tools/annotation/rebuild_annotation_table.sh      # builds, compresses, indexes and verifies
nextflow run . --annotation_table data/<prefix>_annotation_table.tsv.gz \
               --annotation_header data/<prefix>_annotations_header.txt
```
