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

### Example: Variant Observation Resource

```json
    {
      "fullUrl": "urn:uuid:89fd1a4b-1c5e-453e-922e-0ddc90aca1e3",
      "resource": {
        "resourceType": "Observation",
        "id": "ERR2706911-obs-2",
        "meta": {
          "profile": [
            "http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/variant"
          ],
          "tag": [
            {
              "system": "http://terminology.kemkes.go.id/sp",
              "code": "genomics",
              "display": "Genomics"
            }
          ]
        },
        "text": {
          "status": "generated",
          "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Genomic variant at position 6798: G>C in gene gyrB (missense_variant) - p.Gly520Ala - Associated with Levofloxacin - WHO Classification: Not assoc w R</div>"
        },
        "status": "final",
        "category": [
          {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "laboratory",
                "display": "Laboratory"
              }
            ]
          },
          {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/v2-0074",
                "code": "GE",
                "display": "Genetics"
              }
            ]
          }
        ],
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "69548-6",
              "display": "Genetic variant assessment"
            }
          ]
        },
        "valueCodeableConcept": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "LA9633-4",
              "display": "Present"
            }
          ],
          "text": "Present"
        },
        "subject": {
          "reference": "Patient/ERR2706911-patient"
        },
        "specimen": {
          "reference": "Specimen/ERR2706911-specimen"
        },
        "effectiveDateTime": "2026-01-12T05:45:05.263815+00:00",
        "performer": [
          {
            "reference": "Organization/100007732"
          }
        ],
        "component": [
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "81290-9",
                  "display": "Genomic DNA change (gHGVS)"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "https://varnomen.hgvs.org",
                  "code": "NC_000962.3:g.6798G>C",
                  "display": "NC_000962.3:g.6798G>C"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://www.ncbi.nlm.nih.gov/refseq",
                  "code": "NC_000962.3"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "82121-5",
                  "display": "Allelic read depth"
                }
              ]
            },
            "valueQuantity": {
              "value": 197,
              "unit": "reads per base pair",
              "system": "http://unitsofmeasure.org",
              "code": "[1]"
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "48018-6",
                  "display": "Gene studied [ID]"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "https://www.ncbi.nlm.nih.gov/gene",
                  "code": "887081",
                  "display": "gyrB"
                }
              ],
              "text": "gyrB"
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "48019-4",
                  "display": "DNA change type"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://www.sequenceontology.org",
                  "code": "SO:0001583",
                  "display": "missense_variant"
                }
              ],
              "text": "missense_variant"
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "53037-8",
                  "display": "Genetic variation clinical significance [Imp]"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://terminology.kemkes.go.id/sp",
                  "code": "SP000481",
                  "display": "Not assoc w R"
                }
              ],
              "text": "Not assoc w R"
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "48005-3",
                  "display": "Amino acid change (pHGVS)"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "https://varnomen.hgvs.org",
                  "code": "NC_000962.3:p.(Gly520Ala)",
                  "display": "Gly520Ala"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "81254-5",
                  "display": "Variant exact start-end"
                }
              ]
            },
            "valueRange": {
              "low": {
                "value": 6798
              }
            }
          }
        ]
      },
      "request": {
        "method": "PUT",
        "url": "Observation/ERR2706911-obs-2"
      }
    }
```

### 2. Drug Susceptibility Panel Observation
A single summary observation (LOINC `89486-5`) reporting susceptibility status for specific drugs:
*   **Components**: Value for each drug (e.g., Rifampicin, Isoniazid, Bedaquiline).
*   **Values**: `Resistant` (LOINC `LA6676-6`) or `Susceptible` (LOINC `LA24225-7`).

### Example: Drug Susceptibility Panel Resource

```json
    {
      "fullUrl": "urn:uuid:02058040-0799-4258-9517-3b1df746c031",
      "resource": {
        "resourceType": "Observation",
        "id": "ERR2706911-susceptibility-panel",
        "meta": {
          "profile": [
            "http://hl7.org/fhir/StructureDefinition/Observation"
          ]
        },
        "text": {
          "status": "generated",
          "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Mycobacterial susceptibility panel for ERR2706911</div>"
        },
        "status": "final",
        "category": [
          {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "laboratory",
                "display": "Laboratory"
              }
            ]
          },
          {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/v2-0074",
                "code": "GE",
                "display": "Genetics"
              }
            ]
          }
        ],
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "89486-5",
              "display": "Mycobacterial susceptibility panel Qualitative by Genotype method"
            }
          ]
        },
        "subject": {
          "reference": "Patient/ERR2706911-patient"
        },
        "specimen": {
          "reference": "Specimen/ERR2706911-specimen"
        },
        "effectiveDateTime": "2026-01-12T05:45:05.277192+00:00",
        "performer": [
          {
            "reference": "Organization/100007732"
          }
        ],
        "component": [
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "89489-9",
                  "display": "rifAMPin [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "89488-1",
                  "display": "Isoniazid [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA6676-6",
                  "display": "Resistant"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "89491-5",
                  "display": "Ethambutol [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "92242-7",
                  "display": "Pyrazinamide [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "96112-8",
                  "display": "Moxifloxacin [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "20629-2",
                  "display": "levoFLOXacin [Susceptibility]"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "96107-8",
                  "display": "Bedaquiline [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "96109-4",
                  "display": "Delamanid [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "93850-6",
                  "display": "Pretomanid [Susceptibility]"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "96114-4",
                  "display": "Streptomycin [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "89484-0",
                  "display": "Amikacin [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "89482-4",
                  "display": "Kanamycin [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "89483-2",
                  "display": "Capreomycin [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "96108-6",
                  "display": "Clofazimine [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "96110-2",
                  "display": "Ethionamide [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "96111-0",
                  "display": "Linezolid [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "103959-3",
                  "display": "cycloSERINE [Susceptibility] by Genotype method"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "LA24225-7",
                  "display": "Susceptible"
                }
              ]
            }
          }
        ]
      },
      "request": {
        "method": "PUT",
        "url": "Observation/ERR2706911-susceptibility-panel"
      }
    }
```

### 3. Lineage Observation
Classifies the TB strain (LOINC `614-8`) using `http://tb-lineage.org` codes (e.g., Lineage 1, Lineage 2).

### Example: Lineage Observation Resource

```json
    {
      "fullUrl": "urn:uuid:ceedc1e1-aab3-4235-be9c-54470f0ab612",
      "resource": {
        "resourceType": "Observation",
        "id": "ERR2706911-lineage",
        "meta": {
          "profile": [
            "http://hl7.org/fhir/StructureDefinition/Observation"
          ],
          "tag": [
            {
              "system": "http://terminology.kemkes.go.id/sp",
              "code": "genomics",
              "display": "Genomics"
            }
          ]
        },
        "text": {
          "status": "generated",
          "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Mycobacterial Lineage: lineage4.7 (Euro-American)</div>"
        },
        "status": "final",
        "category": [
          {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "laboratory",
                "display": "Laboratory"
              }
            ]
          },
          {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/v2-0074",
                "code": "GE",
                "display": "Genetics"
              }
            ]
          }
        ],
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "614-8",
              "display": "Mycobacterial strain [Type] in Isolate by Mycobacterial subtyping"
            }
          ]
        },
        "valueCodeableConcept": {
          "coding": [
            {
              "system": "http://tb-lineage.org",
              "code": "lineage4.7",
              "display": "TB Lineage lineage4.7"
            }
          ],
          "text": "Lineage lineage4.7"
        },
        "subject": {
          "reference": "Patient/ERR2706911-patient"
        },
        "specimen": {
          "reference": "Specimen/ERR2706911-specimen"
        },
        "effectiveDateTime": "2026-01-12T05:45:05.277209+00:00",
        "performer": [
          {
            "reference": "Organization/100007732"
          }
        ]
      },
      "request": {
        "method": "PUT",
        "url": "Observation/ERR2706911-lineage"
      }
    }
  ]
}
```

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

### Example: DiagnosticReport conclusion code

```json
 ],
        "conclusion": "HR-TB (Isoniazid-resistant tuberculosis). Detected resistance genes: katG. Detected drug resistance: isoniazid  by genotype method. TB Lineage lineage4.7 detected. Reference genome: NC_000962.3",
        "conclusionCode": [
          {
            "text": "HR-TB",
            "coding": [
              {
                "system": "http://snomed.info/sct",
                "code": "414546009",
                "display": "Isoniazid resistant tuberculosis"
              }
            ]
          },
          {
            "text": "Lineage lineage4.7"
          }
        ],
        "presentedForm": [
          {
            "contentType": "text/html",
            "language": "en-US",
            "title": "TB Genomic Analysis Report",
            "data": "PGRpdiB4bWxucz0iaHR0cDovL3d3dy5......"
          }
        ]
      },
      "request": {
        "method": "PUT",
        "url": "DiagnosticReport/ERR2706911-genomic-report"
      }
    }
```

## Output Directory Structure

```bash
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
