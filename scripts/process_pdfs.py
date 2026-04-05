import sys
import os

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

        data["Source"] = file
        rows.append(data)

df = pd.DataFrame(rows)
df.to_csv("data/extracted_data.csv", index=False)

print("Saved extracted_data.csv")
