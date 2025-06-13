import pdfplumber
import pandas as pd
from pathlib import Path

def extract_all_tables_with_pdfplumber(pdf_path: Path) -> dict[str, pd.DataFrame]:
    """
    Extract all tables on all pages of the PDF and return a dict of DataFrames.
    Keys will be 'page_{page_num}_table_{idx}'.
    """
    tables = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            # Extract tables via line detection
            raw_tables = page.extract_tables({
                'vertical_strategy': 'lines',
                'horizontal_strategy': 'lines'
            })
            # Fallback to text-based if none found
            if not raw_tables:
                raw_tables = [page.extract_table({
                    'vertical_strategy': 'text',
                    'horizontal_strategy': 'text'
                })]
            # Convert each raw table to DataFrame
            for idx, table in enumerate(raw_tables, start=1):
                if table and len(table) > 1:
                    header, *rows = table
                    df = pd.DataFrame(rows, columns=header)
                    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
                    key = f"page_{page_num}_table_{idx}"
                    tables[key] = df
    return tables

if __name__ == '__main__':
    root = Path(__file__).resolve().parent.parent  # project root
    pdf_file = root / 'data' / 'appendixd.pdf'
    excel_file = root / 'all_tables_output.xlsx'

    # Extract all tables
    df_dict = extract_all_tables_with_pdfplumber(pdf_file)
    print(f"Extracted {len(df_dict)} tables from {pdf_file.name}")

    # Write to Excel with one sheet per table
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        for sheet_name, df in df_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Written all tables to {excel_file}")
