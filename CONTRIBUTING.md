# Contributing to Scion

**Rethinking Source Control for Agentic Software Engineering: Architectural Transformation, Data Models, and Scalability Constraints in AI-Driven Development**

---

## Status

This project is a **position paper with a proposed empirical evaluation protocol** (`v1.0.0`). The manuscript is complete; the empirical evaluation (Layer C) is proposed but not executed.

Contributions at this stage are welcome in:

- **Layer C execution**: Running the proposed empirical evaluation protocol against publicly accessible comparator systems.
- **Comparative analysis**: Extending the architectural comparison to additional systems (e.g., Git with virtualized checkouts, Sapling/Mononoke).
- **Open questions**: Addressing OQ1 (latency cost of on-demand derived-data) and OQ2 (scope of functional decentralization).
- **Documentation**: Clarifying the manuscript, adding examples, or improving the five-axis framework.

**Not accepted at this stage:**

- New analyses that change the proposed architecture without justification.
- Changes to the research questions without a documented rationale.
- Rewriting the manuscript's conclusions.

For extensions, open an issue first to discuss scope.

---

## Reporting Issues

Open an issue with:

- A one-sentence description.
- The affected file (e.g., `README.md`, `PUBLICATION/Rethinking_Source_Control.pdf`).
- A minimal reproduction or screenshot.
- Expected vs. actual behavior.

---

## Submitting Changes

```bash
git checkout -b feature/short-description
# make changes
git commit -m "feat: short description"
git push origin feature/short-description
```

Then open a pull request. Each PR should address one concern.

---

Code Standards

Language Standard
Python PEP 8, black (88 chars), isort, flake8
Markdown markdownlint (MD013 disabled)
YAML yamllint

Reproducibility: every code change must be reproducible from the public data and the published Python package.

---

Data Provenance

All data and figures are original to this project. No third-party imagery was used. The two conceptual diagrams (three-tier Scion architecture, five-axis framework) were constructed from the architectural description in Anthropic's October 2026 disclosure.

---

Review Process

· All changes are reviewed by the maintainer (Samir Baladi).
· Changes to the manuscript, figures, or reported numbers require explicit documentation in CHANGELOG.md with rationale.

---

Contact

· Email: gitdeeper@gmail.com
· ORCID: https://orcid.org/0009-0003-8903-0029
· Zenodo DOI: https://doi.org/10.5281/zenodo.23934465
· Figshare DOI: https://doi.org/10.6084/m9.figshare.34908594
· PyPI: https://pypi.org/project/rethinking-source-control/
· Website: https://scion-claude.netlify.app

---

Thank you for helping improve the architectural analysis of agentic source control.
