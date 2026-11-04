"""Placeholder tests for Scion.

Scion is a position paper, not a software project.
These tests verify that the repository structure is correct.
"""

import os
import pytest


def test_readme_exists():
    """README.md must exist."""
    assert os.path.exists("README.md")


def test_license_exists():
    """LICENSE must exist."""
    assert os.path.exists("LICENSE")


def test_citation_exists():
    """CITATION.cff must exist."""
    assert os.path.exists("CITATION.cff")


def test_publication_exists():
    """PUBLICATION/ directory must exist."""
    assert os.path.isdir("PUBLICATION")


def test_pdf_exists():
    """The manuscript PDF must exist."""
    assert os.path.exists("PUBLICATION/Rethinking_Source_Control.pdf")


def test_figures_exist():
    """The two figures must exist."""
    assert os.path.isdir("PUBLICATION/figures")
