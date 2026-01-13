# FHIR Standards

## Profiles Used

| Resource | Profile URL |
| :--- | :--- |
| **Patient** | `https://fhir.kemkes.go.id/r4/StructureDefinition/Patient` |
| **Specimen** | `https://fhir.kemkes.go.id/r4/StructureDefinition/Specimen` |
| **Organization** | `https://fhir.kemkes.go.id/r4/StructureDefinition/Organization` |
| **Practitioner** | `https://fhir.kemkes.go.id/r4/StructureDefinition/Practitioner` |
| **DiagnosticReport**| `http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/genomics-report` |

## Standard Terminologies

### LOINC Codes (Sputum & Genomics)

| Code | Display Name | Usage |
| :--- | :--- | :--- |
| **69548-6** | Genetic variant assessment | Observation (Variant) |
| **89486-5** | Mycobacterial susceptibility panel | Observation (Panel) |
| **81247-9** | Master HL7 genetic variant reporting panel | DiagnosticReport |
| **81290-9** | Genomic DNA change (gHGVS) | Variant Component |
| **48005-3** | Amino acid change (pHGVS) | Variant Component |
| **48018-6** | Gene studied [ID] | Variant Component |
| **48019-4** | DNA change type | Variant Component (SO terms) |
| **53037-8** | Genetic variation clinical significance [Imp] | Variant Component (WHO Class) |
| **81254-5** | Variant exact start-end | Variant Component |
| **82121-5** | Allelic read depth | Variant Component |
| **614-8** | Mycobacterial strain [Type] | Lineage Observation |

### LOINC Codes (Drug Susceptibility)
Used within the Susceptibility Panel Observation.

| Code | Display Name |
| :--- | :--- |
| **89489-9** | Rifampin [Susceptibility] by Genotype method |
| **89488-1** | Isoniazid [Susceptibility] by Genotype method |
| **92242-7** | Pyrazinamide [Susceptibility] by Genotype method |
| **89491-5** | Ethambutol [Susceptibility] by Genotype method |
| **96112-8** | Moxifloxacin [Susceptibility] by Genotype method |
| **20629-2** | levoFLOXacin [Susceptibility] |
| **96107-8** | Bedaquiline [Susceptibility] by Genotype method |
| **96111-0** | Linezolid [Susceptibility] by Genotype method |
| **96114-4** | Streptomycin [Susceptibility] by Genotype method |
| **89484-0** | Amikacin [Susceptibility] by Genotype method |

### Sequence Ontology (SO)
Used for **48019-4** (DNA change type).

| Code | Display Name |
| :--- | :--- |
| **SO:0001583** | missense_variant |
| **SO:0001819** | synonymous_variant |
| **SO:0001587** | stop_gained |
| **SO:0001578** | stop_lost |
| **SO:0001589** | frameshift_variant |
| **SO:0001821** | inframe_insertion |
| **SO:0001822** | inframe_deletion |
| **SO:0001629** | splice_site_variant |
| **SO:0001631** | upstream_gene_variant |
| **SO:0001632** | downstream_gene_variant |
| **SO:0001628** | intergenic_variant |
| **SO:0001627** | intron_variant |
| **SO:0001623** | 5_prime_UTR_variant |
| **SO:0001624** | 3_prime_UTR_variant |
| **SO:0002012** | start_lost |
| **SO:0001567** | stop_retained_variant |
| **SO:0001818** | protein_altering_variant |
| **SO:0001580** | coding_sequence_variant |
| **SO:0001619** | non_coding_transcript_variant |
| **SO:0001566** | regulatory_region_variant |

**WHO Classification**
| Code | Display Name | Usage |
| :--- | :--- | :--- |
| **LA26333-7** | http://loinc.org | Uncertain significance |
| **SP000478** | http://terminology.kemkes.go.id/sp | Assoc w R |
| **SP000479** | http://terminology.kemkes.go.id/sp | Assoc w R - Interim |
| **SP000481** | http://terminology.kemkes.go.id/sp | Not assoc w R |

### Clinical Conclusion Codes
Used in `DiagnosticReport.conclusionCode`.

| Diagnosis | Code | System |
| :--- | :--- | :--- |
| **Sensitive** | **TB-SO** | `https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type` |
| **RR-TB** | **415345001** | `http://snomed.info/sct` (Rifampicin resistant tuberculosis) |
| **HR-TB** | **414546009** | `http://snomed.info/sct` (Isoniazid resistant tuberculosis) |
| **MDR-TB** | **423092005** | `http://snomed.info/sct` (Multidrug resistant tuberculosis) |
| **Pre-XDR-TB** | **OV000435** | `http://terminology.kemkes.go.id/CodeSystem/clinical-term` |
| **XDR-TB** | **710106005** | `http://snomed.info/sct` (Extensively drug resistant tuberculosis) |
