# Scion — Complete Inventory

**Version:** 1.0.0
**Release Date:** 2026-11-04
**Series:** Scion-01
**Author:** Samir Baladi
**Email:** gitdeeper@gmail.com
**ORCID:** 0009-0003-8903-0029
**License:** MIT (code) · CC-BY-4.0 (docs, manuscript, figures)
**Status:** Published · Position paper · No empirical results
**DOI (Zenodo):** 10.5281/zenodo.23934465
**DOI (OSF Registration):** 10.17605/OSF.IO/T2WNC
**DOI (Figshare):** 10.6084/m9.figshare.34908594
**OSF Project:** osf.io/gvnhs

---

## Repository Links

| Platform | URL | Role |
|----------|-----|------|
| GitHub | https://github.com/gitdeeper15/Scion | Primary |
| GitLab | https://gitlab.com/gitdeeper15/Scion | Mirror |
| Codeberg | https://codeberg.org/gitdeeper15/Scion | Mirror |
| Bitbucket | https://bitbucket.org/gitdeeper15/Scion | Mirror |
| PyPI | https://pypi.org/project/rethinking-source-control | Python package |
| Zenodo | https://doi.org/10.5281/zenodo.23934465 | DOI (manuscript archive) |
| OSF Registration | https://doi.org/10.17605/OSF.IO/T2WNC | Pre-registration |
| OSF Project | https://osf.io/gvnhs | Associated project |
| Internet Archive | https://archive.org/details/osf-registrations-t2wnc-v1 | Permanent copy |
| Figshare | https://doi.org/10.6084/m9.figshare.34908594 | Secondary archive |
| Website | https://scion-claude.netlify.app | Live documentation |
| ORCID | https://orcid.org/0009-0003-8903-0029 | Identity |
| GitHub Release | https://github.com/gitdeeper15/Scion/releases/tag/v1.0.0 | v1.0.0 |

---

## Root Files

| File | Purpose |
|------|---------|
| `.gitignore` | Git ignore rules |
| `AUTHORS.md` | Contributors |
| `CHANGELOG.md` | Version history |
| `CITATION.cff` | Citation metadata |
| `CONTRIBUTING.md` | Contribution guidelines |
| `INVENTORY.md` | Complete inventory |
| `LICENSE` | MIT + CC-BY-4.0 |
| `MANIFEST.in` | sdist manifest |
| `OSF_REGISTRATION.md` | OSF registration record |
| `README.md` | Main documentation |
| `VERSION` | 1.0.0 |
| `pyproject.toml` | Python config |
| `requirements.txt` | Python deps |
| `setup.cfg` | Setup config |
| `setup.py` | Package setup |

---

## Directories

| Directory | Purpose |
|-----------|---------|
| `PUBLICATION/` | Manuscript, figures, Netlify |
| `DATA/` | Data (references) |
| `ANALYSIS/` | Analysis notes |
| `REPORTS/` | Governance/audit |
| `EXTERNAL_REVIEW/` | Review records |
| `VALIDATION/` | Validation checks |
| `docs/` | Iteration log + documentation |
| `tests/` | Test suite |

---

## Five Axes

| Axis | Focus |
|------|-------|
| 01 — Workload Transformation | Change volume, generation rate, parallelism |
| 02 — Repository Architecture | Distributed → server-backed services |
| 03 — Data Architecture | Changesets, WAL, content addressing, derived data |
| 04 — Execution Infrastructure | Sparse checkouts, tiered caching, server-side APIs |
| 05 — Governance & Security | Intent-based review, directory-level IAM, post-merge testing |

---

## Three-Layer Protocol

| Layer | Focus | Status |
|-------|-------|--------|
| A — Architectural Analysis | Git, Scion, Piper, Sapling/Mononoke | Presented (Section 5) |
| B — Structural Analysis | Data, storage, concurrency, consistency, scalability | Presented (Section 6) |
| C — Empirical Evaluation | Reproducible, controlled tests | Proposed, not executed (Section 9) |

---

## Seven Structural Departures from Git

| Property | Traditional Git | Scion |
|----------|----------------|-------|
| Topology | Distributed | Client-server |
| Connectivity | Offline-first | Always-online |
| Checkout | Full repository clones | Sparse / virtualized |
| Object storage | Packfiles | Content-addressed objects |
| Commit locus | Client-side | Server-side changesets |
| Reference model | Repository refs | Reduced refs |
| Operational model | Repository maintenance | Horizontally scalable services |

---

## Methodological Corrections

1. **Scion does not eliminate merge conflicts.** It shifts conflict detection to post-merge/pre-release testing.
2. **Scion is not unconditionally lock-free.** Changeset creation avoids full coordination, but reference updates use CAS (compare-and-swap).
3. **Derived data is an architectural decision, not a storage optimization.** It separates the write path (changeset log) from the read path (derived structures).

---

## Open Research Questions

| ID | Question |
|----|----------|
| OQ1 | What is the latency cost of on-demand derived-data computation (blame, path history) under high concurrent load? |
| OQ2 | What is the scope of "functional decentralization"? Does it apply only to the changeset-creation path, while reference updates, merges, and history computation continue to depend on coordinated server-side processing? |

---

## Dependencies

### Python (runtime)

- `requests >= 2.28.0`

### Python (dev)

- `pytest >= 7.0.0`
- `pytest-cov >= 4.0.0`
- `black >= 23.0.0`
- `flake8 >= 6.0.0`
- `isort >= 5.12.0`
- `build`
- `twine`

### External APIs

- None (position paper; no API calls).

---

## Completion Summary

```

Project: Scion — Rethinking Source Control for Agentic Software Engineering v1.0.0
Status: Published · Position paper · No empirical results
Axes: 5 (Workload, Repository, Data, Execution, Governance)
Layers: 3 (A, B, C)
Structural departures: 7
Methodological corrections: 3
Open questions: 2
Empirical evaluation: Proposed, not executed
Causal claims: None (position paper)
License: MIT (code) + CC-BY-4.0 (manuscript, figures, docs)

```

---

## Citation

```bibtex
@article{baladi2026scion,
  author       = {Baladi, Samir},
  title        = {Rethinking Source Control for Agentic Software Engineering:
                  Architectural Transformation, Data Models, and
                  Scalability Constraints in AI-Driven Development},
  year         = {2026},
  month        = nov,
  version      = {1.0.0},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23934465},
  url          = {https://doi.org/10.5281/zenodo.23934465},
  note         = {Ronin Institute / Rite of Renaissance. Position paper with proposed empirical evaluation protocol.}
}
```

---

Generated: 2026-11-04
Inventory Version: 1.0.0
Series: Scion-01
