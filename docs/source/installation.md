# Installation

## Prerequisites
To run this pipeline, you need the following installed on your system:

*   [Nextflow](https://www.nextflow.io/)
*   [Python](https://www.python.org/)
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
    git clone https://github.com/robind1/TB-mutation-pipeline.git
    cd tb-mutation-pipeline
    ```
2.  Install Nextflow:
    ```bash
    curl -s https://get.nextflow.io | bash
    ```
3.  Testing the Nextflow install:
    ```bash
    nextflow -v
    ```

