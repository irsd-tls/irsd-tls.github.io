---
title: "Bioinformatics Research In Disease Genomics (BRIDGe)"
description: "Team 4"
menu: menu
weight: 80
layout: team
team: eq4
leader:
  - sarah.djebali
  - jean.monlong
image: images/eq4/banner_eq4.png
image_alt: "Team 4 IRSD"
tags: ["bioinformatics"]
---

**Keywords**: genomics, gene-enhancer relationship, structural variant, pangenome

## Research Program

The Bioinformatics Research In Disease Genomics (BRIDGe) team studies the **functional impact of genomic variations on diseases**. While the core of our research is hypothesis-free, our goal is to apply our methods and analyses primarily to digestive health conditions studied in the lab in order to leverage the lab’s expertise and validate our findings.

If many genome-wide association studies have identified thousands of variants associated with common diseases, two important problems hinder a thorough understanding of the biological mechanisms underlying these diseases and the development of new treatments: 1) the actual causal variants very often remain unknown, 2) the set of identified variants do not entirely explain the heritability of the disease. In reality, these two problems stem from the fact that 1) only small variants (SNPs) are tested for the association with the disease and that 2) the vast majority of associated variants are located in non-coding regulatory regions of the genome. For these reasons, we are focusing our efforts on:

- Extending association studies to longer and more complex variants, Structural Variants (SVs such as duplications, deletions, insertions, translocations) using pangenomic approaches
- Deriving cell-type-specific functional genomic annotations and incorporate them into disease studies
- Integrating structural variants and functional annotation to improve the molecular diagnosis in rare genetic disease studies.


*Keywords*: Genomics, Gene-Enhancer relationship, Structural Variants, Pangenome.

## Members

{{< people-list >}}

### Former members

{{< former-people-list >}}

## Tools and Methods

- Transcriptome sequencing nalysis (RNA-seq, miRNA-seq)
- 3D DNA conformation analysis (Hi-C, promoter capture Hi-C)
- Integrative multi-omics methods (e.g. mixOmics)
- Genome sequencing analysis from short-read (Illumina) or long-read (Oxford Nanopore) data
- Sequencing data analysis using human pangenomes (pangenome construction, read alignment, variant calling)
- Genome-wide association tests (GWAS)
- Rare disease variant calling from long-read data (phased de novo assembly, structural variants, annotation), including for complex regions (e.g. RCCX module)


Members of the team contributed to several public softwares, some of them highlighted below:

- **ChimPipe** {{< github "https://github.com/Chimera-tools/ChimPipe" >}}: a tool to detect novel chimeric transcripts and fusion genes from RNA-seq data ([*Rodríguez-Martín et al. BMC Genomics 2017*](https://doi.org/10.1186/s12864-016-3404-9)).
- **TAGADA** {{< github "https://github.com/FAANG/analysis-TAGADA" >}}: a comprehensice RNA-Seq pipeline, including modules to create novel transcript annotation, and quantify genes and transcripts expression ([*Kurylo, Guyomar, Foissac et Djebali. NAR Genomics and Bioinformatics 2023*](https://academic.oup.com/nargab/article/5/4/lqad089/7318076)).
- **PaintorPipe** {{< github "https://github.com/sdjebali/PaintorPipe" >}}: a pipeline to perform fine-mapping analysis of GWAS results using diverse functionnal annotations ([*Gerber et al. Bioinformatics Advances 2024*](https://academic.oup.com/bioinformaticsadvances/article/4/1/vbad188/7486556)).
- **sveval** {{< github "https://github.com/jmonlong/sveval" >}}: R package to manipulate and benchmark structural variants ([*Hickey, Heller, Monlong et al. Genome Biology 2020*](https://link.springer.com/article/10.1186/s13059-020-1941-7)).
- **vg** {{< github "https://github.com/vgteam/vg" >}}: variation graph toolkit to manipulate pangenomes and analyze sequencing data. Includes the fast read mapper *Giraffe* ([*Sirén, Monlong, Chang, Novak, Eizenga et al. Science 2021*](https://doi.org/10.1126/science.abg8871)).
- **Minigraph-Cactus** {{< github "https://github.com/ComparativeGenomicsToolkit/cactus/blob/master/doc/pangenome.md" >}}: pangenome construction pipeline from high-quality genome assemblies ([*Hickey, Monlong et al. Nature Biotechnology 2024*](https://doi.org/10.1038/s41587-023-01793-w)).
- **Parakit** {{< github "https://github.com/jmonlong/parakit" >}}: a pangenome-based tool to characterize the complex RCCX module from long-read data ([*Monlong et al. medRxiv 2025*](https://www.medrxiv.org/content/10.1101/2025.02.07.25321404v1)).


## Recruitment

We are actively looking to expand and welcome new researchers in genomics and bioinformatics to join our team. Some projects could benefit from new expertise: advanced statistical skills to help with variant imputation, single-cell transcriptomics to enrich our cell-specific characterization of gene regulation, or machine learning to assist in the prediction of functional elements in the genome or functional non-coding variants. Complementary research could also include approaches that would benefit from integrating more variants (e.g. structural variants) or variants with better functional annotation (e.g. in cell-specific regulatory regions), for example developing finer evolutionary metrics or polygenic risk scores. Don’t hesitate to reach out to Sarah and Jean if you are interested in joining the team!

## Selected publications

{{< team-publications >}}
