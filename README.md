
# nlp-05-web-documents-custom

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)
[![CI](https://github.com/ajerineg-coder/nlp-05-web-documents-custom/actions/workflows/ci-python-zensical.yml/badge.svg)](https://github.com/ajerineg-coder/nlp-05-web-documents-custom/actions/workflows/ci-python-zensical.yml)
[![Documentation](https://img.shields.io/badge/docs-site-blue?logo=github)](https://ajerineg-coder.github.io/nlp-05-web-documents-custom/)

[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> Acquire, validate, and transform HTML web documents using Python.

## Project Overview

Author: Addie Gemmell

Date: November 2026

Fifth project in the Web Mining and Applied NLP course.

This project focuses on acquiring and extracting information from HTML web documents using Python.

The goal is to retrieve a web page, validate its structure, extract relevant information, and save the results for further analysis.

I am interested in exploring how web document extraction can be applied to financial fraud research and how unstructured information can be transformed into useful data for analysis.

This project builds on the EVTL pipeline introduced in Module 4, using HTML documents rather than JSON API responses.

The project is configured in [pyproject.toml](pyproject.toml).

## Data

The original example retrieves an academic paper's abstract page from [arXiv](https://arxiv.org/abs/2602.20021).

The source document contains information such as:

- Paper title.
- Authors.
- Abstract.
- Subject categories.
- Submission information.
- arXiv identifier.

For my customized project, I plan to explore academic research related to financial fraud detection.

The pipeline preserves the original HTML and produces a structured CSV dataset containing extracted metadata.

## Approach

The project uses a modular Python pipeline to acquire, validate, transform, and save HTML data.

The pipeline has four stages:

- **Extract** - retrieve HTML from a web page.
- **Validate** - verify that required HTML elements exist.
- **Transform** - extract text and metadata into a structured dataset.
- **Load** - save the processed data to a CSV file.

The project uses Requests for HTTP acquisition, BeautifulSoup for HTML parsing, and Pandas for tabular data processing.

The Transform stage also calculates derived fields such as abstract word count and number of authors.

Important project components include:

- [pyproject.toml](pyproject.toml) - project configuration.
- [src/nlp/pipeline_web_html.py](src/nlp/pipeline_web_html.py) - main EVTL pipeline.
- [src/nlp/config.py](src/nlp/config.py) - web page and path configuration.
- [src/nlp/stage01_extract.py](src/nlp/stage01_extract.py) - retrieve HTML.
- [src/nlp/stage02_validate.py](src/nlp/stage02_validate.py) - validate HTML structure.
- [src/nlp/stage03_transform.py](src/nlp/stage03_transform.py) - extract metadata and build a DataFrame.
- [src/nlp/stage04_load.py](src/nlp/stage04_load.py) - save processed results.
- [tests/](tests/) - automated tests.
- [.github/workflows/](.github/workflows/) - automated testing and documentation deployment.
- [docs/](docs/) - project documentation.
- [zensical.toml](zensical.toml) - documentation configuration.

## Run the Project

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/) to set up the project environment.

From a VS Code terminal in the project root:

```shell
uv run python -m nlp.pipeline_web_html
```

## Results

The pipeline is designed to retrieve an HTML document, validate its structure, extract information, and write the results to a CSV file.

The resulting dataset includes text, metadata, abstract word count, and author count.

Successful execution produces:

```shell
========================
Pipeline executed successfully!
========================
```

The following files are created:

- `project.log` - pipeline execution log.
- `data/raw/case_raw.html` - original HTML document.
- `data/processed/case_processed.csv` - extracted and transformed data.

## Verification

Run the automated tests:

```shell
uv run python -m pytest
```

## Project Documentation

The [hosted documentation site](https://ajerineg-coder.github.io/nlp-05-web-documents-custom/) is published using Zensical and GitHub Pages.

The documentation site presents the project data, methods, results, visualizations, interpretation, and conclusions.

## CI/CD and GitHub Actions

This project includes continuous integration and continuous deployment (CI/CD) to check project files and publish documentation.

GitHub Actions include:

- [CI: Python and Documentation Checks](https://github.com/ajerineg-coder/nlp-05-web-documents-custom/actions/workflows/ci-python-zensical.yml)
- [CD: Documentation Deployment](https://github.com/ajerineg-coder/nlp-05-web-documents-custom/actions/workflows/deploy-zensical.yml)

## Developer Reference

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/) for detailed instructions and troubleshooting.

### Initialize and Update the Python Environment

```shell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

### Set Up and Run Git Hooks

```shell
uvx prek install --force
uvx prek update --freeze --cooldown-days 7

git add -A
uvx prek run --all-files
uvx prek run --all-files
```

### Run Common Chores

```shell
uv run ruff check . --fix
uv run ruff format .

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git add-commit-push to GitHub

```shell
git add -A
git commit -m "describe your changes in quotes"
git push -u origin main
```

## Developer Notes

- Use the up and down arrows to scroll through previous terminal commands.
- Use Command + F to find text within a file on macOS.

## Developer Tools

- [uv](https://docs.astral.sh/uv/) - Python environments and dependencies.
- [Ruff](https://docs.astral.sh/ruff/) - Python linting and formatting.
- [ty](https://docs.astral.sh/ty/) - Python type checking.
- [pytest](https://docs.pytest.org/) - automated Python testing.
- [prek](https://prek.j178.dev/) - Git hooks and automated checks.
- [Zensical](https://zensical.org/) - project documentation.

## Acknowledgments

This project is based on the original [nlp-05-web-documents](https://github.com/denisecase/nlp-05-web-documents) project created by Dr. Denise Case.

## Links

- [Hosted Documentation](https://ajerineg-coder.github.io/nlp-05-web-documents-custom/)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [Citation](CITATION.cff)
- [License](LICENSE)

## D2: Technical Modification

I added a new column to count the sentences in the abstract. I wanted to see how many sentences were in the paper in addition to the word count.

I expected the DataFrame to increase from 8 to 9 columns. After running the project, it worked as expected and the new column was included.

This showed me how I can add more information to the existing pipeline without changing the rest of the process.

## D3: Custom Application

For my custom project, I chose a research paper about elder fraud and the challenges families face when trying to stop scams. I chose this topic because it relates to my work in fraud prevention.

I used Python and BeautifulSoup to collect information from the paper's arXiv webpage. I also used Pandas to organize the results and Matplotlib to create a chart comparing the abstract word counts.

The elder fraud paper had 220 words, 11 sentences, and 7 authors, compared to 177 words, 9 sentences, and 38 authors in the original paper.

The results showed that the elder fraud paper had a longer abstract despite having fewer authors. One limitation is that I only compared two papers, so I would need more data to identify any larger patterns.

### How to Run

Run the project using:

uv run python -m nlp.pipeline_web_html

To create the comparison chart, run:

uv run python src/create_chart.py

The chart and additional results are available in docs/index.md.
