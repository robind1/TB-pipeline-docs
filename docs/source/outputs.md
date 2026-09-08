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
