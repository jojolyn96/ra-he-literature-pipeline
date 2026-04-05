import os
import sys

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
from src.extract import extract_text_from_pdf, extract_properties

PDF_FOLDER = "papers/"   # you will store PDFs here

rows = []

for file in os.listdir(PDF_FOLDER):
    if file.endswith(".pdf"):
        path = os.path.join(PDF_FOLDER, file)
        print(f"Processing {file}...")

        text = extract_text_from_pdf(path)
        data = extract_properties(text)

        print(f"Extracted data: {data}")

        data["Source"] = file
        rows.append(data)

df = pd.DataFrame(rows)
output_file = "data/extracted_data.csv"

if os.path.exists(output_file):
    existing_df = pd.read_csv(output_file)
    df = pd.concat([existing_df, df], ignore_index=True)

df.drop_duplicates(subset=["Source"], inplace=True)

df.to_csv(output_file, index=False)

print("Saved extracted_data.csv")
