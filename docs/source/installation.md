# Installation

## Prerequisites
To run this pipeline, you need the following installed on your system:

*   **Nextflow** (>=21.10.0)
*   **Java** (>=11)
*   **Docker**
*   **Python 3.9+**
*   [FastQC](https://github.com/s-andrews/FastQC)
*   [MultiQC](https://github.com/MultiQC/MultiQC)
*   [BWA-MEM2](https://github.com/bwa-mem2/bwa-mem2) 
*   [minimap2](https://github.com/lh3/minimap2)
*   [GATK](https://gatk.broadinstitute.org/hc/en-us) 
*   [Medaka](https://github.com/nanoporetech/medaka)
*   [bcftools](https://github.com/samtools/bcftools)
*   [samtools](https://github.com/samtools/samtools) 
*   [FHIR validator](https://github.com/hapifhir/org.hl7.fhir.validator-wrapper)

## Setup
1.  Clone the repository for local installation:
    ```bash
    git clone https://github.com/robind1/TBmutationpipeline.git
    cd tb-mutation-pipeline
    ```
2.  Installl Docker:
    ```bash
    curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh
    ```
3.  Installl Nextflow:
    ```bash
    curl -s https://get.nextflow.io | bash
    ```
4.  Testing the Nextflow install:
    ```bash
    nextflow -v
    ```