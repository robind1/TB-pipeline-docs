# Installation

## Requirements

- [Nextflow](https://www.nextflow.io/) **25.04 or later**, with Java 17 or later. On 26.04, use
  **26.04.2 or later**.
- **One** of the following to provide the tools:

| Profile | Provides the tools via |
| --- | --- |
| `-profile docker` (or `podman`) | pinned [BioContainers](https://biocontainers.pro/) images |
| `-profile singularity` (or `apptainer`) | the same images, e.g. on HPC |
| `-profile conda` (or `mamba`) | pinned bioconda / conda-forge packages |
| none | tools already on `PATH` (see [Running without a profile](#running-without-a-profile)) |

Images are pulled only for the processes that run; for example, Illumina-only runs never download
medaka.

Install Nextflow:

```bash
curl -s https://get.nextflow.io | bash
./nextflow -version
```

## Get the pipeline

Run it straight from GitHub:

```bash
nextflow run oucru-id/tb-to-fhir-full -r 2.0.2 -profile docker --input samplesheet.csv --outdir results
```

Or clone it and run the local copy:

```bash
git clone -b 2.0.2 https://github.com/oucru-id/tb-to-fhir-full.git
cd tb-to-fhir-full
nextflow run . -profile docker --input samplesheet.csv --outdir results
```

## Check the installation

Three test profiles use data bundled with the pipeline:

```bash
nextflow run . -profile test_stub -stub-run      # wiring only, no tools needed
nextflow run . -profile test_vcf,docker          # end to end on synthetic VCFs
nextflow run . -profile test,docker              # Illumina path on a 10 MB public subset (ERR1873531, MDR-TB)
```

The `test` run should end with an MDR-TB conclusion for ERR1873531 in
`results/fhir/genomic/ERR1873531.genomic.fhir.json`.

## Running without a profile

Without a profile, these tools must be on `PATH`:
- for all runs: `bcftools`, `samtools`, `tabix`/`bgzip`, Python 3 (standard library only) and
  Java 17 or later
- for Illumina input: `bwa-mem2`, GATK 4 (`gatk`), `trimmomatic`, `fastqc`, `multiqc`,
  `mosdepth`
- for ONT input: `minimap2`, `medaka`, `chopper`, `NanoPlot`, `multiqc`, `mosdepth`

If you have only the Debian/Ubuntu `trimmomatic.jar`, pass
`--trimmomatic_jar /usr/share/java/trimmomatic.jar`.

## Notes for container runs

- The Python image has no `openpyxl`, so give `.xlsx` clinical metadata as CSV, or use
  `-profile conda`.
- The FHIR validator downloads its IG packages (about 50 MB) into the task directory on each run.
  Without containers it caches them in `~/.fhir`.

## Uploading to a FHIR server

Upload is optional and runs only when `--fhir_server_url` is given. It sends only linked bundles
(which need [clinical metadata](clinical_metadata.md)) that passed validation. Credentials are
[Nextflow secrets](https://docs.seqera.io/nextflow/secrets/):

```bash
nextflow secrets set TBFHIR_CLIENT_ID     '<client id>'
nextflow secrets set TBFHIR_CLIENT_SECRET '<client secret>'

nextflow run . -profile docker --input samplesheet.csv \
  --patient_metadata site/patients.csv \
  --organization_metadata site/organization.csv \
  --practitioner_metadata site/practitioner.csv \
  --fhir_profile satusehat \
  --fhir_server_url https://<server>/fhir \
  --fhir_auth_url https://<sso>/realms/<realm>
```

- To also send an `X-Api-Key` header, set the `TBFHIR_API_KEY` secret and add
  `--fhir_upload_api_key`.
- `--bundle_request_method POST` sends server-assigned-id transactions (with `ifNoneExist` on
  NIK). `--external_refs` maps samples to Patients that already exist on the server.
- For SATUSEHAT, test against the sandbox first.

The pipeline fetches its own token from `--fhir_auth_url`. The scripts in `tools/satusehat/`
(`get_access_token.py`, `get_patient_by_nik.py`) are only for manual checks. They keep tokens in
`$TBFHIR_HOME` (default `~/.tbfhir`).
