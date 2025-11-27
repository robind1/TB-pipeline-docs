# Output Files

The pipeline generates a structured set of results organized by data type. The primary output is the **HL7 FHIR** bundle, which integrates resistance findings with clinical metadata.

## FHIR Genomic Observations

Converts annotated variants into standardized FHIR **Observation** resources.

### Observation Resources
Each detected variant generates a Observation resource containing:
*   **Genomic Coordinates**: 
    *   **gHGVS**: Genomic DNA change (e.g., `NC_000962.3:g.761155C>T`)
    *   **pHGVS**: Amino acid change (e.g., `Ser315Thr`)
*   **Resistance Gene Information**: Identifies the affected gene (e.g., *rpoB*, *katG*, *inhA*).
*   **Drug Resistance Associations**: Links variants to specific drugs (e.g., Rifampicin, Isoniazid, Fluoroquinolones) using SNOMED CT codes.
*   **Lineage Information**: Links the classified TB lineage (e.g., Lineage 1: Indo-Oceanic, Lineage 2: East Asian/Beijing).
*   **Quality Metrics**: Includes Allele Read Depth (RD) to indicate sequencing confidence.

## Clinical Data Integration

Merges the FHIR Genomics Observations with patient, facility, and practitioner information to create a complete genomic diagnostic report document.

### DiagnosticReport Resource
*   **Conclusion**: A human-readable summary.
*   **Presentation**: Contains a Base64 encoded HTML representation of the report.
*   **Links**: References the Patient, Specimen, and all Variant Observations.

## Drug Resistance Classification

| Classification | Definition | Logic |
| :--- | :--- | :--- |
| **Sensitive** | No resistance detected | No mutations in resistance-associated genes. |
| **RR-TB** | Rifampicin-resistant TB | Resistance to Rifampicin detected (no Isoniazid). |
| **HR-TB** | Isoniazid-resistant TB | Resistance to Isoniazid detected (no Rifampicin). |
| **MDR-TB** | Multidrug-resistant TB | Resistance to **both** Isoniazid and Rifampicin. |
| **Pre-XDR-TB** | Pre-Extensively drug-resistant | MDR + Resistance to either Fluoroquinolone **OR** second-line drug. |
| **XDR-TB** | Extensively drug-resistant | MDR + Resistance to Fluoroquinolone **AND** second-line drug. |

## Output Directory Structure

```text
results/
├── qc/
│   └── multiqc_report.html       
├── lineage/
│   └── *.lineage.json            
├── fhir/
│   └── *.fhir.json              
├── fhir_merged/
│   └── *.merged.fhir.json
├── fhir_validated/
│   ├── *.validation.txt
├── reports/
│   └── *.summary_report.txt     
```