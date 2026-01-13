# Output Files
The primary output is a **HL7 FHIR Bundle** containing genomic observations merged with clinical data.

## FHIR Genomic Bundle
### 1. Variant Observation Resources
Each detected variant generates an observation (LOINC `69548-6`) containing:
*   **Genomic Coordinates**: 
    *   **gHGVS**: Genomic DNA change (e.g., `NC_000962.3:g.761155C>T`) - LOINC `81290-9`.
    *   **pHGVS**: Amino acid change (e.g., `p.Ser315Thr`) - LOINC `48005-3`.
    *   **Exact Start-End**: Genomic position - LOINC `81254-5`.
*   **Gene Information**: The affected gene (e.g., *rpoB*) - LOINC `48018-6`.
*   **DNA Change Type**: Sequence Ontology term (e.g., *missense_variant*) - LOINC `48019-4`.
*   **Clinical Significance**: WHO classification (e.g., *Assoc w R*) - LOINC `53037-8`.
*   **Quality Metrics**: Allele Read Depth (DP) - LOINC `82121-5`.

### 2. Drug Susceptibility Panel Observation
A single summary observation (LOINC `89486-5`) reporting susceptibility status for specific drugs:
*   **Components**: Value for each drug (e.g., Rifampicin, Isoniazid, Bedaquiline).
*   **Values**: `Resistant` (LOINC `LA6676-6`) or `Susceptible` (LOINC `LA24225-7`).

### 3. Lineage Observation
Classifies the TB strain (LOINC `614-8`) using `http://tb-lineage.org` codes (e.g., Lineage 1, Lineage 2).

## Clinical Data Integration & Reporting

### Generated Resources
*   **Patient**: uses `https://fhir.kemkes.go.id/r4/StructureDefinition/Patient` profile.
*   **Specimen**: Sputum sample details.
*   **ServiceRequest**: Order for genetic assessment.
*   **Organization**: Testing facility details.
*   **Practitioner & PractitionerRole**: Medical staff details.
*   **DiagnosticReport**: 
    *   **Code**: LOINC `81247-9` (Master HL7 genetic variant reporting panel).
    *   **Conclusion**: Text summary of resistance and lineage.
    *   **Presentation**: Base64 encoded HTML report.

## Drug Resistance Classification
The `DiagnosticReport` conclusion is derived using the following logic:

| Classification | Definition | Logic |
| :--- | :--- | :--- |
| **Sensitive** | No resistance detected | No mutations in resistance-associated genes |
| **RR-TB** | Rifampicin-resistant TB | Resistance to **Rifampicin** detected (without Isoniazid) |
| **HR-TB** | Isoniazid-resistant TB | Resistance to **Isoniazid** detected (without Rifampicin) |
| **MDR-TB** | Multidrug-resistant TB | Resistance to **both** Isoniazid and Rifampicin |
| **Pre-XDR-TB** | Pre-Extensively drug-resistant | (MDR or RR) + Resistance to **Fluoroquinolones** |
| **XDR-TB** | Extensively drug-resistant | (MDR or RR) + Resistance to **Fluoroquinolones** + **Group A** drugs (Bedaquiline or Linezolid) |
