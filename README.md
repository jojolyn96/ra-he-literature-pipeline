# RA–Hydrogen Embrittlement Literature Pipeline

## Overview
This repository provides a reproducible pipeline for:
- Identifying relevant literature on hydrogen embrittlement
- Filtering papers based on retained austenite relevance
- Building a structured dataset for RA vs crack initiation behavior

## Features
- Automated paper search (Semantic Scholar API)
- Keyword-based filtering and ranking
- Semi-automated data extraction from PDFs
- Structured dataset generation (CSV)

## Installation

```bash
pip install -r requirements.txt

## Reproducibility

To recreate the dataset:

### Using just (recommended)


### Using make


This will:
1. Install dependencies
2. Query literature databases
3. Extract data from PDFs
4. Generate dataset files

## Requirements
- Python 3.10+
- just (https://github.com/casey/just)

Install just:
sudo apt install just
