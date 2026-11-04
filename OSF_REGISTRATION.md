# Scion — Rethinking Source Control for Agentic Software Engineering

---

**Registration DOI:** [10.17605/OSF.IO/T2WNC](https://doi.org/10.17605/OSF.IO/T2WNC)
**Registration Type:** OSF Preregistration
**Registry:** OSF Registries
**Date Created:** Nov 4, 2026, 5:37 AM
**Date Registered:** Nov 4, 2026, 5:37 AM
**Associated Project:** [https://osf.io/gvnhs](https://osf.io/gvnhs)
**Internet Archive:** [https://archive.org/details/osf-registrations-t2wnc-v1](https://archive.org/details/osf-registrations-t2wnc-v1)
**License:** CC-By Attribution 4.0 International
**Contributor:** Samir Baladi

---

## Data / Analytic Code / Materials / Papers / Supplements

The following files were attached to this registration:

- `Rethinking_Source_Control.pdf` (50.6 kB)
- `README.md` (14.6 kB)

---

## Overview

### Research questions or hypotheses

RQ: What architectural, data-model, and infrastructure changes become necessary — and which remain optional design choices — when source control must support a substantial fraction of changes originating from parallel, autonomous agents rather than sequential human authorship?

The study decomposes this question into five independent axes, each examined separately:

Axis 01 — Workload Transformation: What changes in change volume, generation rate, parallelism, and merge frequency under agentic authorship?

Axis 02 — Repository Architecture: Does source control shift from a fully distributed repository model toward horizontally scaled, server-backed services?

Axis 03 — Data Architecture: What changes in changesets, write-ahead logs, content addressing, and derived data become necessary?

Axis 04 — Execution Infrastructure: What changes in sparse and virtualized checkouts, tiered caching, and server-side APIs become necessary?

Axis 05 — Governance and Security: What changes in intent-based review, directory-level IAM, post-merge testing, and concurrent-conflict handling become necessary?

Two open research questions are identified as unresolved by the published material:

OQ1: What is the latency cost of on-demand derived-data computation (blame, path history) under high concurrent load, and is there an implicit tradeoff between the simplicity of the base data model and the latency of history-dependent queries?

OQ2: What is the scope of "functional decentralization" in Scion? Does the claim of operating without full cross-server coordination apply only to the changeset-creation path, while reference updates, merges, and history computation continue to depend on coordinated server-side processing?

### Foreknowledge of data or evidence

Analyses in this plan have been conducted already. At least some of the analyses described in this analysis plan have been conducted by the authors making this a retrospective registration.

### Explanation of foreknowledge and managing unintended influences

This is a retrospective registration. The architectural and structural analyses (Layers A and B) were conducted prior to this OSF registration. The empirical evaluation layer (Layer C) is proposed but not executed.

To mitigate risks of unintended influences:

1. The research question is reframed to avoid presupposing a verdict: it does not ask "is Scion better than Git?", but "what architectural changes become necessary?"

2. The analysis is organized around five independent axes, each of which can be examined separately rather than collapsed into a single judgment.

3. Three methodological corrections are applied as binding constraints on all other claims:
   - Scion does not eliminate merge conflicts (it shifts them to post-merge testing).
   - Scion is not unconditionally lock-free (CAS is used for ref updates).
   - Derived data is an architectural decision, not a storage optimization.

4. All operational figures attributed to Anthropic (30,000+ merges/day, >99% cache hit rate, ~200× infrastructure reduction, ~100× checkout speedup, 25% CI improvement) are explicitly flagged as self-reported, not independently verified.

5. The empirical evaluation (Layer C) is explicitly scoped as a proposed, unexecuted protocol. No claims in the paper are presented as results from that protocol.

The purpose of this registration is to document the architectural analysis and the proposed empirical protocol transparently, not to claim a pre-registered confirmatory study.

---

## Research Design

### Study type

Descriptive study: Describing some features of a dataset or sample, but typically not for the purposes of informing a causal effect.

### Intention for causal interpretation

No causal relationship inferred: This study is not intended to inform a causal relationship.

### Blinding of experimental treatments

No blinding is involved.

### Additional blinding during research or analysis

Not applicable. This is a position paper with a proposed empirical evaluation protocol. No human subjects, no treatment assignment, and no blinding procedures are involved.

### Study design

The study is a position paper with a three-layer research protocol.

Layer A — Architectural Analysis: Synthesizes the architectural descriptions of Git, Scion, Piper, and Sapling/Mononoke from their published documentation. No new measurements are collected.

Layer B — Structural Analysis: Examines data models, storage, concurrency, consistency, and scalability. It identifies which architectural properties are responsive to agentic workload characteristics.

Layer C — Empirical Evaluation: A proposed, unexecuted protocol for reproducible, controlled tests. Candidate measurements include checkout latency (sparse vs. full-clone), merge throughput and conflict-detection timing, history-query latency (on-demand vs. eager derived data), cache-hit rate per tier, and failure-isolation behavior.

The five axes (workload, repository, data, execution, governance) are examined independently rather than collapsed into a single comparison. Two methodological corrections are treated as binding constraints: Scion does not eliminate merge conflicts, and its lock-free claim applies specifically to changeset creation.

No randomization, no counterbalancing, and no within-subject or between-subject comparisons are involved. The empirical layer (Layer C), if executed, would compare systems under controlled workload conditions, but this comparison has not been performed.

**Attached:** `Rethinking_Source_Control.pdf`, `README.md`

### Randomization

Not applicable. This is a position paper with a proposed empirical protocol. No randomization of subjects, tasks, or conditions is performed. The proposed Layer C protocol would use synthetic workload generation with fixed seeds for reproducibility, but no experiments have been executed.

---

## Sampling

### Data collection procedures

This study does not collect new empirical data. It synthesizes and analyzes published architectural descriptions.

Data sources:
1. Anthropic (2026). Redesigning Source Control at Anthropic. Anthropic Research, published October 13, 2026 (updated October 15, 2026). https://www.anthropic.com/research/redesigning-source-control — the sole source for all Scion-specific architectural and operational claims.
2. Potvin, R., & Levenberg, J. (2016). Why Google Stores Billions of Lines of Code in a Single Repository. Communications of the ACM, 59(7), 78–87. — comparator system (Piper).
3. Corbett, J. C., Dean, J., Epstein, M., et al. (2013). Spanner: Google's Globally-Distributed Database. ACM Transactions on Computer Systems, 31(3), Article 8. — background on the authoritative server tier.
4. Sapling SCM. (n.d.). Sapling: A Scalable, User-Friendly Source Control System. Meta Platforms. https://sapling-scm.com/ — comparator system.
5. Meta Platforms. (n.d.). Sapling / Mononoke Source Repository. GitHub. https://github.com/facebook/sapling — comparator system.
6. Chacon, S., & Straub, B. (2014). Pro Git (2nd ed.). Apress. https://git-scm.com/book — baseline system (Git).

Inclusion criteria: Publicly accessible architectural descriptions and documentation of source-control systems (Scion, Piper, Sapling/Mononoke, Git). All references are cited in the manuscript.

Exclusion criteria: Internal design documents or source code not publicly available (Scion is not public at the time of writing). No independent benchmarking data is available.

No human subjects are involved. No sampling frame, recruiting, or geographic scope applies.

Expected duration: Not applicable (document analysis only).

### Sample size

Unit of analysis: Published architectural description (not individual observations).

Sample sizes:
- Primary source for Scion: 1 (Anthropic 2026 disclosure).
- Comparator systems: 3 (Piper, Sapling/Mononoke, Git).
- Total systems compared: 4 (Scion, Piper, Sapling/Mononoke, Git).
- Methodological corrections applied: 3.
- Open research questions identified: 2.
- Proposed empirical measurements (Layer C, not executed): 5 (checkout latency, merge throughput, history-query latency, cache-hit rate, failure isolation).

No conditions, treatments, or clusters are involved. The sample size is determined by the number of publicly documented systems available for architectural comparison, not by statistical power.

### Sample size rationale

No power analysis was performed. The sample size is determined by the scope of the published material:
- Scion is documented in a single public disclosure (Anthropic 2026).
- Piper, Sapling/Mononoke, and Git are selected as comparator systems because each represents a distinct architectural approach to large-scale source control.

The analysis is qualitative and architectural, not statistical. A larger sample of systems would not change the central architectural findings, because the object of study is the set of architectural properties (changeset model, derived data, tiered distribution), not a population of systems.

A larger empirical benchmark (Layer C) is proposed in the manuscript as future work.

### Starting and stopping rules

Starting rule: Document analysis begins with the publication of Anthropic's October 2026 disclosure. There is no pilot phase.

Stopping rule: The analysis terminates when all five axes (workload, repository, data, execution, governance) have been examined and the two open research questions have been identified. No sequential testing or early stopping is involved.

The proposed empirical evaluation (Layer C) has not been executed. If executed in the future, its starting and stopping rules would be specified in a separate preregistration.

---

## Variables

### Manipulated variables

None. This is a position paper with a proposed empirical evaluation protocol. No variables are manipulated by the researcher. The analysis examines published architectural descriptions; it does not assign conditions, treatments, or arms.

The proposed Layer C protocol (not executed) would compare systems under controlled workload conditions, but this comparison has not been performed.

### Measured variables

This manuscript does not report empirical measurements. The variables below are analytical constructs drawn from the published material.

Scion-specific architectural properties (from Anthropic 2026):
1. Changeset model — write-ahead log, content-addressed blobs, reduced refs.
2. Derived-data mechanism — server-side computation of blame, path history, commit-graph traversal.
3. Three-tier distribution — daemon, regional cache, authoritative server.
4. Operational figures (self-reported by Anthropic, not independently verified):
   - Merge throughput (>30,000 merges/day).
   - Cache-hit rate (>99% at every tier).
   - Infrastructure footprint (~200× reduction vs. prior Git-mirroring approach).
   - Checkout speedup (~100×).
   - CI improvement (25%).

Structural comparison variables (Git vs. Scion, seven departures):
5. Topology — distributed vs. client-server.
6. Connectivity — offline-first vs. always-online.
7. Checkout — full clones vs. sparse/virtualized.
8. Object storage — packfiles vs. content-addressed objects.
9. Commit locus — client-side vs. server-side changesets.
10. Reference model — repository refs vs. reduced refs.
11. Operational model — repository maintenance vs. horizontally scalable services.

Methodological corrections (binding constraints):
12. Merge-conflict handling — not eliminated, shifted to post-merge/pre-release testing.
13. Lock-free claim — applies to changeset creation, not to reference updates (which use CAS).
14. Derived data — architectural decision, not storage optimization.

Five axes (analytical framework):
15. Workload transformation.
16. Repository architecture.
17. Data architecture.
18. Execution infrastructure.
19. Governance and security.

Two open research questions:
20. OQ1 — Latency cost of on-demand derived-data computation.
21. OQ2 — Scope of functional decentralization.

No covariates, no subsetting variables, and no exclusion criteria are involved. All variables are qualitative or architectural.

### Indices

No composite indices or derived variables are constructed.

The paper reports qualitative architectural distinctions, not numerical scores. The five axes are treated as independent analytical categories, not combined into a single index.

If the proposed Layer C protocol were executed, candidate measurements would include:
- Checkout latency (as a function of repository size, sparse vs. full-clone).
- Merge throughput and conflict-detection timing.
- History-query latency (on-demand vs. eager derived data).
- Cache-hit rate per tier (daemon, regional cache, authoritative server).
- Failure-isolation behavior (effect of a simulated regional-cache outage on authoritative-server load).

None of these measurements have been collected for this manuscript.

The only numerical quantities reported are Anthropic's own published operational figures, which are explicitly flagged as self-reported and not independently verified. They are not combined into any index.

---

## Analysis Plan

### Statistical models

No statistical model is used. This is a position paper with a proposed empirical evaluation protocol.

The analysis is architectural and conceptual, not statistical. It decomposes the research question into five independent axes and examines each axis separately. No ANOVA, regression, SEM, or mixed-effects model is estimated.

If the proposed Layer C protocol were executed, it would use controlled comparisons (e.g., checkout latency under sparse vs. full-clone configurations; merge throughput under synthetically generated agentic workload patterns). These would be pre-registered with specified models, but no such models are estimated in this manuscript.

No interactions, subgroup analyses, pairwise contrasts, follow-up tests, positive controls, negative controls, manipulation checks, convergence criteria, or tests of model assumptions are used, because no statistical model is estimated.

### Transformations

No transformations are applied. No coding scheme, centering, recoding, logging, winsorizing, or other data transformation is performed.

The analysis works with qualitative architectural distinctions (e.g., "distributed vs. client-server," "packfiles vs. content-addressed objects") and with Anthropic's own published operational figures. These figures are reported as published, without transformation, and are explicitly flagged as self-reported.

### Inference criteria

No p-values, Bayes factors, or model fit indices are used. The analysis is qualitative and architectural, not inferential.

Inferences are supported by:
1. Direct citation of the published architectural descriptions (Anthropic 2026; Potvin & Levenberg 2016; Corbett et al. 2013; Sapling SCM; Meta Platforms; Chacon & Straub 2014).
2. Explicit distinction between (a) architectural claims reported in the source material, (b) structural inferences drawn from distributed-systems principles, and (c) self-reported operational figures that have not been independently verified.

No one-tailed or two-tailed tests are used. No multiple-comparison correction is applied, because no hypothesis tests are performed.

The methodological corrections (merge conflicts, lock-free scope, derived data) are treated as binding constraints on all other claims, not as hypothesis tests. They are supported by direct reading of the source material.

### Data inclusion and exclusion

Inclusion criteria:
- Publicly accessible architectural descriptions of source-control systems (Scion, Piper, Sapling/Mononoke, Git).
- Published documentation of each system's own design.
- Anthropic's October 2026 disclosure as the sole source for all Scion-specific claims.

Exclusion criteria:
- Internal design documents or source code not publicly available (Scion is not public at the time of writing).
- Independent benchmark data (none is available for Scion).
- Any claim that cannot be traced to a published source.

No outliers are removed. No observations are excluded. All cited sources are included in the reference list.

### Missing data

Not applicable. No empirical dataset is used, so no missing data arises.

Scion's source code and internal design documents are not publicly available. This absence is stated explicitly as a limitation of the manuscript, not treated as missing data to be imputed.

### Other planned analysis

The manuscript proposes a future empirical evaluation (Layer C). If executed, it would include:

1. Checkout latency as a function of repository size, under sparse/virtualized versus full-clone configurations.
2. Merge throughput and conflict-detection timing under synthetically generated agentic workload patterns (high parallelism, short-lived branches, high change frequency).
3. History-query latency (blame, path history) under on-demand versus eager derived-data computation, at varying history depth and concurrent load.
4. Cache-hit rate at each tier (daemon, regional cache, authoritative server) under controlled request-mix scenarios.
5. Failure-isolation behavior: the effect of a simulated regional-cache outage on authoritative-server load.

A synthetic agentic-workload generator is proposed, parameterized by change rate, parallelism, change size distribution, and merge-conflict injection rate.

This protocol has not been executed. It is presented as proposed future work, not as analysis performed for this manuscript.

---

## Other

### Context and additional information

CONTEXT

This is a retrospective registration. The architectural and structural analyses (Layers A and B) were conducted and the manuscript was written prior to this OSF registration. The empirical evaluation (Layer C) is proposed but not executed.

PURPOSE

The purpose of this registration is to document the architectural analysis and the proposed empirical protocol transparently. It is not a pre-registered confirmatory study.

PUBLISHED RESOURCES

- Zenodo DOI: 10.5281/zenodo.23934465
- Figshare DOI: 10.6084/m9.figshare.34908594
- PyPI: https://pypi.org/project/rethinking-source-control/
- Website: https://scion-claude.netlify.app
- GitHub: https://github.com/gitdeeper15/Scion
- GitLab: https://gitlab.com/gitdeeper15/Scion
- Codeberg: https://codeberg.org/gitdeeper15/Scion
- Bitbucket: https://bitbucket.org/gitdeeper15/Scion
- ORCID: https://orcid.org/0009-0003-8903-0029

WHAT THIS REGISTRATION PRE-REGISTERS

- The primary research question.
- The five independent axes (workload, repository, data, execution, governance).
- The three-layer research protocol (A: Architectural Analysis; B: Structural Analysis; C: Empirical Evaluation, proposed).
- The seven structural departures from Git.
- The three methodological corrections (merge conflicts, lock-free scope, derived data).
- The two open research questions (latency cost, functional decentralization).

WHAT THIS REGISTRATION DOES NOT INCLUDE

- Independent benchmarking of Scion (the system is not public).
- Empirical results from Layer C (the protocol is proposed, not executed).
- Human evaluation or multi-judge consensus.

SCOPE OF THE CLAIMS

All operational figures attributed to Scion (30,000+ merges/day, >99% cache hit rate, ~200× infrastructure reduction, ~100× checkout speedup, 25% CI improvement) are Anthropic's own published figures. They are not independently verified and are flagged as such throughout the manuscript.

The manuscript is a position paper. It offers an architectural analysis and a proposed empirical protocol, not empirical findings.

PRIMARY SOURCE

Anthropic. (2026). Redesigning Source Control at Anthropic. Published October 13, 2026 (updated October 15, 2026). https://www.anthropic.com/research/redesigning-source-control

This is the sole source for all Scion-specific architectural and operational claims.

COMPARATOR SYSTEMS

- Piper (Google) — Potvin & Levenberg (2016).
- Spanner (Google) — Corbett et al. (2013).
- Sapling/Mononoke (Meta) — Sapling SCM; Meta Platforms.
- Git — Chacon & Straub (2014).

References 2, 3, and 6 describe prior, independently published systems used for architectural comparison. They are not descriptions of Scion.

ETHICS

This study does not involve human subjects. No personal data is collected. All cited sources are public.

PROTOCOL INTEGRITY

The protocol is frozen at registration. Any change after registration will be documented as a protocol amendment with explicit rationale.

NEXT RESEARCH STAGE

Execution of the Layer C evaluation protocol against publicly accessible comparator systems (Git with virtualized-checkout extensions, Sapling/Mononoke), and preregistration of confirmatory measurements prior to data collection.

---

## Metadata

### Contributors
Samir Baladi

### Resource type
No resource type

### Description

Scion is a position paper and proposed empirical evaluation protocol examining the architectural transformation required when source control systems serve parallel, agentic workloads rather than human-paced collaborative development.

The paper treats Anthropic's October 2026 disclosure of Scion (an internal source-control system) not as a product announcement, but as a case study motivating a broader architectural question: what structural transformations become necessary when code production shifts from a human-paced, sequential activity to a parallel activity driven by autonomous agents?

The analysis is organized around five axes: workload characteristics, repository architecture, data architecture, execution infrastructure, and governance/security.

The paper proposes a three-layer design:
- Layer A (Architectural Analysis): What source control must do differently under agentic workloads.
- Layer B (Structural Analysis): How the five axes interact and constrain each other.
- Layer C (Empirical Evaluation): A proposed, unexecuted protocol for future benchmarking.

Three critical corrections are built into the analysis as binding constraints:
1. Scion did not eliminate merge conflicts; it shifted them to post-merge/pre-release testing.
2. Scion is not unconditionally lock-free; changeset creation avoids full coordination, but ref updates still use CAS.
3. Derived data is treated as an architectural decision, not a storage optimization.

Two open research questions are posed:
1. What is the latency cost of on-demand derived-data computation?
2. What is the scope of "functional decentralization" in practice?

All operational figures attributed to Anthropic are explicitly flagged as self-reported, not independently verified.

Resources:
- Zenodo DOI: 10.5281/zenodo.23934465
- Figshare DOI: 10.6084/m9.figshare.34908594
- PyPI: https://pypi.org/project/rethinking-source-control/
- Website: https://scion-claude.netlify.app
- GitHub: https://github.com/gitdeeper15/Scion

License: MIT (code) + CC-BY-4.0 (manuscript, figures, documentation).

Author: Samir Baladi (ORCID: 0009-0003-8903-0029)

### Registration Type
OSF Preregistration

### Registry
OSF Registries

### Associated project
https://osf.io/gvnhs

### Date Created
Nov 4, 2026, 5:37 AM

### Date registered
Nov 4, 2026, 5:37 AM

### Subjects
- Software Engineering
- Computer Sciences
- Physical Sciences and Mathematics

### Tags
- agentic software engineering
- changesets
- derived data
- distributed systems
- git
- repository architecture
- scalability
- scion
- source control

### Affiliated Institutions
No affiliated institutions

### Funder Names
No information

### Language
No language

### Associated project
https://osf.io/gvnhs

### Internet Archive link
https://archive.org/details/osf-registrations-t2wnc-v1

### License
CC-By Attribution 4.0 International

### Registration DOI
10.17605/OSF.IO/T2WNC

---

## Citations

### APA
Baladi, S. (2026, November 4). Scion — Rethinking Source Control for Agentic Software Engineering. OSF. https://doi.org/10.17605/OSF.IO/T2WNC

### MLA
Baladi, Samir. "Scion — Rethinking Source Control for Agentic Software Engineering." OSF, 4 Nov. 2026. Web.

### Chicago
Baladi, Samir. 2026. "Scion — Rethinking Source Control for Agentic Software Engineering." OSF. November 4. doi:10.17605/OSF.IO/T2WNC.

### BibTeX

```bibtex
@misc{baladi2026scion_osf,
  author       = {Baladi, Samir},
  title        = {{Scion} --- Rethinking Source Control for Agentic
                  Software Engineering},
  year         = {2026},
  month        = nov,
  day          = {4},
  publisher    = {OSF},
  doi          = {10.17605/OSF.IO/T2WNC},
  url          = {https://doi.org/10.17605/OSF.IO/T2WNC},
  note         = {OSF Preregistration}
}
```

---

Source: Center for Open Science · OSF Registries
Retrieved: 2026-11-04
