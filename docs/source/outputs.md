# Output Files
The primary output is a **HL7 FHIR Bundle** containing genomic observations merged with clinical data.
```{image} _static/fhirgenomicsbundletb.png
:alt: TB FHIR Genomics Bundle
:width: 1200px
:align: center
```

## FHIR Genomic Bundle
### 1. Variant Observation Resources
Each detected variant generates an observation (LOINC `69548-6`) containing:
*   **Genomic Coordinates**: 
    *   **gHGVS**: Genomic DNA change (e.g., `NC_000962.3:g.761155C>T`) - LOINC `81290-9`.
    *   **pHGVS**: Amino acid change (e.g., `p.Ser315Thr`) - LOINC `48005-3`.
    *   **Exact Start-End**: Genomic position - LOINC `81254-5`.
*   **Gene Information**: The affected gene (e.g., *rpoB*) - LOINC `48018-6`.
*   **DNA Change Type**: Sequence Ontology term (e.g., *missense_variant*) - LOINC `48019-4`.
*   **Medication Assessed**: The drug the grade applies to - LOINC `51963-7` (SNOMED coded).
*   **Clinical Significance**: WHO classification (e.g., *Assoc w R*) - LOINC `53037-8`.
*   **Reference Sequence**: Genomic reference sequence ID - LOINC `48013-7`.
*   **Quality Metrics**:
    *   Allele Read Depth (DP) - LOINC `82121-5`.
    *   Sample variant allelic frequency - LOINC `81258-6`.
    *   Variant call quality (QUAL) and Mapping quality (MQ) - `tbd-codes-cs`.

```{note}
**Per-drug grading.** A variant graded against more than one drug carries a
`51963-7` / `53037-8` **pair for each drug**. The WHO catalogue grades each (variant, drug) pair
independently, so for example a `pepQ` loss-of-function variant is reported as *Assoc w R* for
Bedaquiline and *Uncertain significance* for Clofazimine within the same Observation.
```

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
*   **Values**: one of **three** states.

| State | LOINC | Meaning |
| :--- | :--- | :--- |
| **Resistant** | `LA6676-6` | A WHO group 1 or 2 variant was detected |
| **Susceptible** | `LA24225-7` | No such variant **and** every locus for that drug met the coverage threshold |
| **Indeterminate** | `LA9663-1` | No such variant, but coverage of the relevant loci could not be confirmed |

```{warning}
**Absence of a resistance mutation is not evidence of susceptibility.** `Susceptible` is only
emitted when the drug's resistance loci were demonstrably sequenced to the configured depth and
breadth; otherwise the result is `Indeterminate`. Indeterminate components carry a `text` value
naming the specific loci that blocked the call, for example:
*"Indeterminate - no resistance-associated mutation detected, but susceptibility cannot be
confirmed (insufficient coverage at: Rv0678)"*.
```

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

### 3. Region Studied Observation
Records which resistance loci were actually examined. This is the evidence behind a
negative result.

*   **Profile**: `http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/region-studied`
*   **Code**: LOINC `53041-0` (DNA region of interest panel)
*   **Granularity**: one Observation per gene.
*   **Components**:
    *   Gene studied - LOINC `48018-6`
    *   Genomic reference sequence ID - LOINC `48013-7`
    *   Mean depth - LOINC `82121-5`
    *   Fraction of bases at ≥ *N*× - `tbd-codes-cs` `coverage-breadth` (percent)

### Example: Region Studied Observation Resource

```json
    {
      "resourceType": "Observation",
      "id": "ERR2706911-region-rpoB",
      "meta": {
        "profile": [
          "http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/region-studied"
        ]
      },
      "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Region studied: rpoB (Rifampicin) - adequately covered: 98.6% of bases at >= 10x, mean depth 29.28x</div>"
      },
      "status": "final",
      "code": {
        "coding": [
          {
            "system": "http://loinc.org",
            "code": "53041-0",
            "display": "DNA region of interest panel"
          }
        ],
        "text": "Region studied: rpoB"
      },
      "component": [
        {
          "code": {
            "coding": [
              { "system": "http://loinc.org", "code": "48018-6", "display": "Gene studied [ID]" }
            ]
          },
          "valueCodeableConcept": {
            "coding": [
              { "system": "https://www.ncbi.nlm.nih.gov/gene", "code": "888164", "display": "rpoB" }
            ],
            "text": "rpoB"
          }
        },
        {
          "code": {
            "coding": [
              { "system": "http://loinc.org", "code": "82121-5", "display": "Allelic read depth" }
            ]
          },
          "valueQuantity": {
            "value": 29.28,
            "unit": "reads per base pair",
            "system": "http://unitsofmeasure.org",
            "code": "[1]"
          }
        },
        {
          "code": {
            "coding": [
              {
                "system": "http://hl7.org/fhir/uv/genomics-reporting/CodeSystem/tbd-codes-cs",
                "code": "coverage-breadth",
                "display": "Fraction of bases at >= 10x"
              }
            ],
            "text": "Fraction of bases at >= 10x"
          },
          "valueQuantity": {
            "value": 98.56,
            "unit": "%",
            "system": "http://unitsofmeasure.org",
            "code": "%"
          }
        }
      ]
    }
```

```{note}
The breadth figure is a **gene-level summary**. A gene may read 96% covered while the missing 4%
happens to include the resistance-determining codon. Per-base detail is available in
`results/qc/*.regions.bed.gz` and `*.thresholds.bed.gz`.
```

### 4. Lineage Observation

| Component code | Value |
| :--- | :--- |
| `lineage-family` | e.g. *East-African-Indian* |
| `lineage-confidence` | e.g. *high* |
| `lineage-score` | 0.0 – 1.0 |
| `barcode-snps-matched` | Barcode SNPs matched |
| `barcode-snps-total` | Barcode SNPs examined |

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
    *   **Conclusion**: Text summary of resistance and lineage. Drugs that could not be assessed
        are named.
    *   **Presentation**: Base64 encoded HTML report.
*   **Device**: The pipeline that produced the calls (`TBtoFHIR`), its version, and the source
    repository. SNOMED `706689003` (Application program software).
*   **Provenance**: One per sample, targeting the `DiagnosticReport` and every Observation it
    rests on. Agents are the software (`assembler`) and the performing Organization (`performer`),
    with activity `CREATE`.

## Drug Resistance Classification
The `DiagnosticReport` conclusion is derived using the following logic order:

| Classification | Definition | Logic |
| :--- | :--- | :--- |
| **XDR-TB** | Extensively drug-resistant | (MDR or RR) + Resistance to **Fluoroquinolones** + **Group A** drugs |
| **Pre-XDR-TB** | Pre-Extensively drug-resistant | (MDR or RR) + Resistance to **Fluoroquinolones** |
| **MDR-TB** | Multidrug-resistant TB | Resistance to **both** Isoniazid and Rifampicin |
| **RR-TB** | Rifampicin-resistant TB | Resistance to **Rifampicin** detected (without Isoniazid) |
| **HR-TB** | Isoniazid-resistant TB | Resistance to **Isoniazid**, with Rifampicin **assessed and susceptible** |
| **Streptomycin mono-resistant** | Streptomycin-resistant TB | Resistance to **Streptomycin** only |
| **Ethionamide mono-resistant** | Ethionamide-resistant TB | Resistance to **Ethionamide** only |
| **Pyrazinamide mono-resistant** | Pyrazinamide-resistant TB | Resistance to **Pyrazinamide** only |
| **Ethambutol mono-resistant** | Ethambutol-resistant TB | Resistance to **Ethambutol** only |
| **Ciprofloxacin mono-resistant** | Ciprofloxacin-resistant TB | Resistance to **Ciprofloxacin** only (without other Fluoroquinolones) |
| **Drug-resistant** | Antibiotic resistant tuberculosis | Any other resistance combination not falling into above categories |
| **Drug-resistant – rifampicin not assessable** | Resistance present, class undetermined | Resistance detected, but Rifampicin could not be assessed, so RR/MDR/pre-XDR/XDR cannot be determined |
| **No resistance detected** | No resistance, fully assessed | No resistance variant, and **all** drug groups were assessable |
| **No resistance detected – partial** | No resistance, partly assessed | No resistance variant, but some drugs could not be assessed |
| **Indeterminate** | Nothing assessable | No resistance variant and **no** drug could be assessed |

```{warning}
The classifications that depend on Rifampicin (RR / MDR / Pre-XDR / XDR) are only asserted when
Rifampicin itself was assessable. An indeterminate Rifampicin blocks classification rather than
falling through to a lower class.

`Sensitive` is no longer emitted. The Kemkes `TB-SO` ("Tuberkulosis Sensitif Obat") coding is
reserved for **No resistance detected**, where every drug group was genuinely assessable.
```

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
│   └── who_targets.bed           
│   └── *.coverage.json            
│   └── *.regions.bed.gz         
│   └── *.thresholds.bed.gz       
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
