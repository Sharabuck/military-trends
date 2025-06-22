# Military Trends Project

This repository contains a Python-based ETL pipeline and analysis scripts for exploring military demographic trends, including:

- Extraction of historical DoD demographic tables (Table D-13) via `pdfplumber` and Camelot.
- Conversion of tables to Excel workbooks for reporting and Power BI ingestion.

## Project Structure
MILITARYTREND/
├── .venv/                       # Python virtual environment
├── MilitaryTrends/              # Solution folder
│   ├── data/                    # Source PDFs
│   │   └── appendixd.pdf
│   ├── src/                     # ETL and analysis scripts
│   │   └── main.py
│   ├── military_trends.db       # SQLite database
│   ├── all_tables_output.xlsx   # Raw Excel export
│   ├── all_tables_clean.xlsx    # Cleaned Excel export
│   ├── appendixd_d13.xlsx       # D-13 table export
│   ├── README.md                # This file
│   └── requirements.txt         # Dependencies
└── .gitignore                   # Ignored files


## Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/military-trends.git
   cd military-trends/MilitaryTrends/src

Create and activate a virtual environment:

python -m venv ../.venv
source ../.venv/bin/activate  # macOS/Linux
../.venv/Scripts/activate     # Windows

Install dependencies:

pip install -r ../requirements.txt

Ensure Ghostscript is installed and on your PATH for camelot-py[cv].
