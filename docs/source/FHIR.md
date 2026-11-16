# FHIR standards

TBtoFHIR writes HL7 FHIR R4 that conforms to the
[Genomics Reporting IG 3.0.0](https://hl7.org/fhir/uv/genomics-reporting/STU3/). Two output
profiles are available, chosen with `--fhir_profile`:

- **`generic`** (default): HL7 Genomics Reporting only.
- **`satusehat`**: conforming to the Indonesian Ministry of Health SATUSEHAT platform (Kemkes
  profiles, NIK identifiers, Kemkes extensions and codings).

## Profiles

Genomics Reporting profiles are under
`http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/`, and Kemkes profiles under
`https://fhir.kemkes.go.id/r4/StructureDefinition/`.

| Resource | `generic` | `satusehat` |
| --- | --- | --- |
| Variant Observation | Genomics Reporting `variant` | same |
| Susceptibility panel, Lineage Observation | base `Observation` | base `Observation` |
| Region-studied Observation | no profile declared | Genomics Reporting `region-studied` |
| DiagnosticReport | Genomics Reporting `genomic-report` | Genomics Reporting `genomics-report` |
| Patient, Specimen, Encounter, ServiceRequest, Organization, Practitioner, PractitionerRole | base FHIR R4 | Kemkes profile of the same name |
| Bundle | base FHIR R4 | Kemkes `Bundle` |

## LOINC codes

| Code | Display | Used in |
| --- | --- | --- |
| `69548-6` | Genetic variant assessment | Variant Observation (value `LA9633-4` Present) |
| `89486-5` | Mycobacterial susceptibility panel | Susceptibility panel Observation |
| `53041-0` | DNA region of interest panel | Region-studied Observation |
| `614-8` | Mycobacterial strain [Type] | Lineage Observation |
| `51969-4` | Genetic analysis report | DiagnosticReport (`generic`) |
| `81247-9` | Master HL7 genetic variant reporting panel | DiagnosticReport (`satusehat`; second coding in `generic`) |
| `81290-9` | Genomic DNA change (gHGVS) | Variant component |
| `81254-5` | Variant exact start-end | Variant component |
| `48018-6` | Gene studied [ID] | Variant and region-studied component |
| `48019-4` | DNA change type | Variant component (Sequence Ontology term) |
| `51963-7` | Medication assessed [Identifier] | Variant component, one per drug |
| `53037-8` | Genetic variation clinical significance [Imp] | Variant component (WHO grade), one per drug |
| `48005-3` | Amino acid change (pHGVS) | Variant component (`satusehat` only) |
| `48013-7` | Genomic reference sequence ID | Variant component |
| `82121-5` | Allelic read depth | Variant component; mean depth in region-studied |
| `81258-6` | Sample variant allelic frequency [NFr] | Variant component |

## Susceptibility result codes

`valueCodeableConcept` of each drug component in the susceptibility panel:

| Code | Display | Meaning |
| --- | --- | --- |
| `LA6676-6` | Resistant | A variant graded *Assoc w R* or *Assoc w R - Interim* was detected |
| `LA24225-7` | Susceptible | No such variant **and** coverage was confirmed at every locus that carries a grade 1-2 variant for that drug |
| `LA9663-1` | Indeterminate | No such variant, but coverage of those loci could not be confirmed |

## Drug susceptibility codes

The panel has one component per drug. The same drugs are coded with SNOMED CT as *Medication
assessed* on the variant Observations.

| Drug | Panel component (LOINC) | Medication assessed (SNOMED CT) |
| --- | --- | --- |
| Rifampicin | `89489-9` rifAMPin [Susceptibility] by Genotype method | `29175007` |
| Isoniazid | `89488-1` Isoniazid [Susceptibility] by Genotype method | `81335000` |
| Ethambutol | `89491-5` Ethambutol [Susceptibility] by Genotype method | `24450004` |
| Pyrazinamide | `92242-7` Pyrazinamide [Susceptibility] by Genotype method | `13592004` |
| Moxifloxacin | `96112-8` Moxifloxacin [Susceptibility] by Genotype method | `371296007` |
| Levofloxacin | `20629-2` levoFLOXacin [Susceptibility] | `96087006` |
| Bedaquiline | `96107-8` Bedaquiline [Susceptibility] by Genotype method | `714087008` |
| Delamanid | `96109-4` Delamanid [Susceptibility] by Genotype method | `714098009` |
| Pretomanid | `93850-6` Pretomanid [Susceptibility] | `789321008` |
| Streptomycin | `96114-4` Streptomycin [Susceptibility] by Genotype method | `40877002` |
| Amikacin | `89484-0` Amikacin [Susceptibility] by Genotype method | `48836000` |
| Kanamycin | `89482-4` Kanamycin [Susceptibility] by Genotype method | `71451001` |
| Capreomycin | `89483-2` Capreomycin [Susceptibility] by Genotype method | `14170004` |
| Clofazimine | `96108-6` Clofazimine [Susceptibility] by Genotype method | `72924009` |
| Ethionamide | `96110-2` Ethionamide [Susceptibility] by Genotype method | `414148003` |
| Linezolid | `96111-0` Linezolid [Susceptibility] by Genotype method | `125695009` |
| Cycloserine | `103959-3` cycloSERINE [Susceptibility] by Genotype method | `51334008` |

## WHO grade codes

The clinical-significance component (LOINC `53037-8`) carries the WHO final grade:

| WHO grade | `generic` | `satusehat` |
| --- | --- | --- |
| 1) Assoc w R | `who-catalogue-grade` `1` | `SP000478` (`http://terminology.kemkes.go.id/sp`) |
| 2) Assoc w R - Interim | `who-catalogue-grade` `2` | `SP000479` |
| 3) Uncertain significance | `who-catalogue-grade` `3` | LOINC `LA26333-7` |
| 4) Not assoc w R - Interim | `who-catalogue-grade` `4` | `SP000480` |
| 5) Not assoc w R | `who-catalogue-grade` `5` | `SP000481` |

## Conclusion codes

`DiagnosticReport.conclusionCode` carries the resistance classification (see
[Outputs](outputs.md#drug-resistance-classification)) and the lineage as text.

| Classification | Code (both profiles) |
| --- | --- |
| **MDR-TB** | SNOMED CT `423092005` |
| **XDR-TB** | SNOMED CT `710106005` |
| **RR-TB** | SNOMED CT `415345001` |
| **HR-TB** | SNOMED CT `414546009` |
| **Streptomycin-resistant TB** | SNOMED CT `415622003` |
| **Ethionamide-resistant TB** | SNOMED CT `414149006` |
| **Pyrazinamide-resistant TB** | SNOMED CT `415222009` |
| **Ethambutol-resistant TB** | SNOMED CT `414146004` |
| **Ciprofloxacin-resistant TB** | SNOMED CT `413852006` |
| **Drug-resistant**, **Drug-resistant - rifampicin not assessable** | SNOMED CT `413556004` |

`satusehat` adds two Kemkes codes that have no SNOMED CT equivalent:

| Classification | `satusehat` code |
| --- | --- |
| **No resistance detected** | `TB-SO` Tuberkulosis Sensitif Obat (`https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type`) |
| **Pre-XDR-TB** | `OV000435` Pre-XDR (`http://terminology.kemkes.go.id/CodeSystem/clinical-term`) |

In `generic`, these two and **No resistance detected - partial** and **Indeterminate** are
reported as text only. `TB-SO` is reserved for **No resistance detected**, where every drug group
was assessable.

## Sequence Ontology

DNA change type (LOINC `48019-4`) uses Sequence Ontology terms:

| Code | Display |
| --- | --- |
| `SO:0001583` | missense_variant |
| `SO:0001819` | synonymous_variant |
| `SO:0001587` | stop_gained |
| `SO:0001578` | stop_lost |
| `SO:0001589` | frameshift_variant |
| `SO:0001821` | inframe_insertion |
| `SO:0001822` | inframe_deletion |
| `SO:0001629` | splice_site_variant |
| `SO:0001631` | upstream_gene_variant |
| `SO:0001632` | downstream_gene_variant |
| `SO:0001628` | intergenic_variant |
| `SO:0001627` | intron_variant |
| `SO:0001623` | 5_prime_UTR_variant |
| `SO:0001624` | 3_prime_UTR_variant |
| `SO:0002012` | start_lost |
| `SO:0001567` | stop_retained_variant |
| `SO:0001818` | protein_altering_variant |
| `SO:0001580` | coding_sequence_variant |
| `SO:0001619` | non_coding_transcript_variant |
| `SO:0001566` | regulatory_region_variant |
| `SO:0002054` | loss_of_function_variant |
| `SO:0001792` | non_coding_transcript_exon_variant |
| `SO:0001582` | initiator_codon_variant |
| `SO:0001879` | feature_ablation |
| `SO:0001906` | feature_truncation |
| `SO:0001826` | disruptive_inframe_deletion |
| `SO:0001824` | disruptive_inframe_insertion |
| `SO:0001574` | splice_acceptor_variant |
| `SO:0001575` | splice_donor_variant |
| `SO:0001630` | splice_region_variant |
| `SO:0001893` | transcript_ablation |
| `SO:0001637` | rRNA_gene_variant |

## Project CodeSystems

Concepts that no standard code covers use CodeSystems published by the project under
`http://terminology.spheres.id/CodeSystem/`. Their definitions are in `assets/fhir/` and are
loaded by the validator. Consumers that do not know them can ignore them safely.

| CodeSystem | Codes |
| --- | --- |
| `who-catalogue-grade` | `1` Assoc w R, `2` Assoc w R - Interim, `3` Uncertain significance, `4` Not assoc w R - Interim, `5` Not assoc w R |
| `tbfhir-observation-code` | `who-variant-id` WHO catalogue variant identifier, `variant-quality` QUAL, `mapping-quality` MQ, `coverage-breadth` fraction of bases at or above the minimum depth |
| `mtb-lineage` | lineage names, e.g. `lineage4.3` |
| `mtb-lineage-attribute` | `lineage-family`, `lineage-confidence`, `lineage-score`, `barcode-snps-matched`, `barcode-snps-total` |
| `pipeline-property` | `source-repository`, `filter-min-depth`, `filter-min-quality`, `coverage-min-depth`, `coverage-min-breadth` (Device properties) |

`satusehat` also adds the `http://tb-lineage.org` lineage coding as a second coding.

## Gene identifiers

Genes are coded with the NCBI GeneID (`https://www.ncbi.nlm.nih.gov/gene`). Genes without a
verified GeneID (45 WHO catalogue genes) are written as text only. Add verified ids to
`data/gene_ncbi_map.tsv`, or give a file with `--gene_map`.
