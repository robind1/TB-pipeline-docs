# FHIR Standards

## Profiles Used

| Resource | Profile URL |
| :--- | :--- |
| **Patient** | `https://fhir.kemkes.go.id/r4/StructureDefinition/Patient` |
| **Specimen** | `https://fhir.kemkes.go.id/r4/StructureDefinition/Specimen` |
| **Organization** | `https://fhir.kemkes.go.id/r4/StructureDefinition/Organization` |
| **Practitioner** | `https://fhir.kemkes.go.id/r4/StructureDefinition/Practitioner` |
| **DiagnosticReport**| `http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/genomics-report` |
| **Observation (Laboratory)**| `http://terminology.hl7.org/CodeSystem/observation-category` |
| **Observation (Genetics)**| `http://terminology.hl7.org/CodeSystem/v2-0074` |
| **Variant**| `http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/variant` |
| **Region Studied**| `http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/region-studied` |
| **Device** | `http://hl7.org/fhir/StructureDefinition/Device` |
| **Provenance** | `http://hl7.org/fhir/StructureDefinition/Provenance` |

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
| **82121-5** | Allelic read depth | Variant Component / Region Studied (mean depth) |
| **48013-7** | Genomic reference sequence ID | Variant Component / Region Studied |
| **81258-6** | Sample variant allelic frequency [NFr] | Variant Component |
| **51963-7** | Medication assessed [Identifier] | Variant Component |
| **53041-0** | DNA region of interest panel | Region Studied Observation |
| **614-8** | Mycobacterial strain [Type] | Lineage Observation |

### Susceptibility Result Codes
Used as `valueCodeableConcept` on each drug component of the Susceptibility Panel.

| Code | Display Name | Meaning |
| :--- | :--- | :--- |
| **LA6676-6** | Resistant | A WHO group 1 or 2 variant was detected |
| **LA24225-7** | Susceptible | No such variant **and** coverage of every locus for that drug was confirmed |
| **LA9663-1** | Indeterminate | No such variant, but coverage could not be confirmed |

### Genomics Reporting `tbd-codes-cs`
System: `http://hl7.org/fhir/uv/genomics-reporting/CodeSystem/tbd-codes-cs`

| Code | Display Name | Usage |
| :--- | :--- | :--- |
| **coverage-breadth** | Fraction of bases at >= *N*x | Region Studied Component (percent) |
| **variant-quality** | Variant call quality (QUAL) | Variant Component |
| **mapping-quality** | Mapping quality (MQ) | Variant Component |

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
| **SO:0002054** | loss_of_function_variant |
| **SO:0001792** | non_coding_transcript_exon_variant |
| **SO:0001582** | initiator_codon_variant |
| **SO:0001879** | feature_ablation |
| **SO:0001906** | feature_truncation |
| **SO:0001826** | disruptive_inframe_deletion |
| **SO:0001824** | disruptive_inframe_insertion |
| **SO:0001574** | splice_acceptor_variant |
| **SO:0001575** | splice_donor_variant |
| **SO:0001630** | splice_region_variant |
| **SO:0001893** | transcript_ablation |
| **SO:0001637** | rRNA_gene_variant |

**WHO Classification**
| Code | Display Name | Usage |
| :--- | :--- | :--- |
| **LA26333-7** | http://loinc.org | Uncertain significance |
| **SP000478** | http://terminology.kemkes.go.id/sp | Assoc w R |
| **SP000479** | http://terminology.kemkes.go.id/sp | Assoc w R - Interim |
| **SP000481** | http://terminology.kemkes.go.id/sp | Not assoc w R |
| **SP000480** | http://terminology.kemkes.go.id/sp | Not assoc w R - Interim |

### Clinical Conclusion Codes
Used in `DiagnosticReport.conclusionCode`.

| Diagnosis | Code | System |
| :--- | :--- | :--- |
| **No resistance detected** | **TB-SO** | `https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type` |
| **No resistance detected – partial** | *(uncoded)* | Neither drug-sensitive nor drug-resistant is true |
| **Indeterminate** | *(uncoded)* | No drug could be assessed |
| **Drug-resistant – rifampicin not assessable** | **413556004** | `http://snomed.info/sct` |
| **RR-TB** | **415345001** | `http://snomed.info/sct` |
| **HR-TB** | **414546009** | `http://snomed.info/sct` |
| **MDR-TB** | **423092005** | `http://snomed.info/sct` |
| **Pre-XDR-TB** | **OV000435** | `http://terminology.kemkes.go.id/CodeSystem/clinical-term` |
| **XDR-TB** | **710106005** | `http://snomed.info/sct` |
| **Streptomycin mono-resistant** | **415622003** | `http://snomed.info/sct` |
| **Ethionamide mono-resistant** | **414149006** | `http://snomed.info/sct` |
| **Pyrazinamide mono-resistant** | **415222009** | `http://snomed.info/sct` |
| **Ciprofloxacin mono-resistant** | **413852006** | `http://snomed.info/sct` |
| **Ethambutol mono-resistant** | **414146004** | `http://snomed.info/sct` |
| **Drug-resistant (Other)** | **413556004** | `http://snomed.info/sct` |

## Pipeline-Local Code Systems

These are published by the pipeline rather than by an external authority. They exist because no
standard code covers the concept; they are namespaced so downstream consumers can recognise and
ignore them safely.

### Lineage
`http://terminology.spheres.id/CodeSystem/mtb-lineage` Primary lineage coding
(e.g. `lineage4.7`). Replaces the previously used `http://tb-lineage.org`; that coding is retained as a **secondary** coding on the same
`valueCodeableConcept` for traceability.

### Lineage Attributes
`http://terminology.spheres.id/CodeSystem/mtb-lineage-attribute` — components on the Lineage
Observation.

| Code | Value type | Meaning |
| :--- | :--- | :--- |
| **lineage-family** | string | e.g. *East-African-Indian* |
| **lineage-confidence** | string | e.g. *high* |
| **lineage-score** | Quantity | Barcode match score, 0.0 – 1.0 |
| **barcode-snps-matched** | Quantity | Barcode SNPs matched |
| **barcode-snps-total** | Quantity | Barcode SNPs examined |

### Pipeline Properties
`http://terminology.spheres.id/CodeSystem/pipeline-property` — `Device.property` entries recording
the configuration that produced the calls.

| Code | Value type | Meaning |
| :--- | :--- | :--- |
| **source-repository** | CodeableConcept (text) | Pipeline source repository URL |
| **filter-min-depth** | Quantity | Variant-calling depth filter |
| **filter-min-quality** | Quantity | Variant-calling quality filter |
| **coverage-min-depth** | Quantity | Depth at which a base counts as covered |
| **coverage-min-breadth** | Quantity | Fraction of a locus that must reach that depth |

## Gene Identifiers

Genes are coded against `https://www.ncbi.nlm.nih.gov/gene` using the NCBI GeneID. Genes without a
verified GeneID are emitted as `valueCodeableConcept.text` **only**. Additional mappings can be
supplied via `data/gene_ncbi_map.tsv`.
