# Output Files
The primary output is the **HL7 FHIR** bundle and per-sample genomic reports.

## FHIR Genomic Bundle
### Observation Resources
Each detected variant generates an observation resource containing:
*   **Genomic Coordinates**: 
    *   **gHGVS**: Genomic DNA change (e.g., `NC_000962.3:g.761155C>T`)
    *   **pHGVS**: Amino acid change (e.g., `p.Ser315Thr`)
*   **Resistance Gene Information**: Identifies the affected gene (e.g., *rpoB*, *katG*, *inhA*).
*   **Drug Resistance Associations**: Links variants to specific drugs (e.g., Rifampicin, Isoniazid, Fluoroquinolones) using SNOMED CT codes.
*   **Lineage Information**: Links the classified TB lineage (e.g., Lineage 1: Indo-Oceanic, Lineage 2: East Asian/Beijing).
*   **Quality Metrics**: Includes Allele Read Depth (RD).
*   **Genome Position**: Includes the specific location of the variant detected (e.g., `761155`)

## Clinical Data Integration
Merges the FHIR Genomics Observations with patient, facility, and practitioner information to create a complete genomic diagnostic report document.
### DiagnosticReport Resource
*   **Conclusion**: A human-readable summary report.
*   **Presentation**: Contains a Base64 encoded HTML representation of the report.
*   **Links**: References the Patient, Specimen, and all Variant Observations.

## Drug Resistance Classification for DiagnosticReport
| Classification | Definition | Logic |
| :--- | :--- | :--- |
| **Sensitive** | No resistance detected | No mutations in resistance-associated genes |
| **RR-TB** | Rifampicin-resistant TB | Resistance to Rifampicin detected|
| **HR-TB** | Isoniazid-resistant TB | Resistance to Isoniazid detected |
| **MDR-TB** | Multidrug-resistant TB | Resistance to **both** Isoniazid and Rifampicin |
| **Pre-XDR-TB** | Pre-Extensively drug-resistant | MDR + resistance to either Fluoroquinolone **OR** second-line drug |
| **XDR-TB** | Extensively drug-resistant | MDR + resistance to Fluoroquinolone **AND** second-line drug |

## Output Structure
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
├── runningstat/
│   └── dag.html
│   └── execution.html
│   └── timeline.html
├── software_versions.yml
```
