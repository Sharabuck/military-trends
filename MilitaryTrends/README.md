# Military Trends Project

This repository contains a Python-based ETL pipeline and analysis scripts for exploring military demographic trends, including:

- Extraction of historical DoD demographic tables (Table D-13) via `pdfplumber` and Camelot.
- Storage of raw and cleaned data in SQLite (`military_trends.db`).
- Conversion of tables to Excel workbooks for reporting and Power BI ingestion.

## Project Structure
```
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
```


## Setup & Installation

1.  Clone the repository:
   ```bash
   git clone https://github.com/Sharabuck/military-trends.git
   cd military-trends/MilitaryTrends/src


## Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/military-trends.git
   cd military-trends/MilitaryTrends/src

2. Create and activate a virtual environment:
    python -m venv ../.venv
    source ../.venv/bin/activate  # macOS/Linux
    ../.venv/Scripts/activate     # Windows

3. Install dependencies:
    pip install -r ../requirements.txt

4. Ensure Ghostscript is installed and on your PATH for camelot-py[cv].

## Usage

Run the ETL and conversion scripts from the src/ folder:

python main.py

This will:

Extract tables from data/appendixd.pdf.

Generate Excel exports (all_tables_output.xlsx, all_tables_clean.xlsx, appendixd_d13.xlsx).

Populate the SQLite database military_trends.db

## License

This project is available under the MIT License.


*After adding this README.md, initialize your local Git repo (if not already), commit changes, and push to GitHub as described in the GitHub Integration steps above.*

## Dependencies

This project does not have any external dependencies. The `requirements.txt` file is included for future use if needed.