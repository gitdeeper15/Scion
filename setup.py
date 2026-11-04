#!/usr/bin/env python3
"""Setup script for Scion."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip()
        for line in fh
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="rethinking-source-control",
    version="1.0.0",
    author="Samir Baladi",
    author_email="gitdeeper@gmail.com",
    description="Rethinking Source Control for Agentic Software Engineering: Architectural Transformation, Data Models, and Scalability Constraints in AI-Driven Development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "docs.*", "PUBLICATION", "PUBLICATION.*", "EXPERIMENTS", "EXPERIMENTS.*"]),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Version Control",
        "Topic :: Scientific/Engineering",
    ],
    keywords="source control, version control, agentic software engineering, distributed systems, changesets, derived data, repository architecture, scalability, scion, git",
    project_urls={
        "Homepage": "https://github.com/gitdeeper15/Scion",
        "Zenodo": "https://doi.org/10.5281/zenodo.23934465",
        "Figshare": "https://doi.org/10.6084/m9.figshare.34908594",
    },
)
