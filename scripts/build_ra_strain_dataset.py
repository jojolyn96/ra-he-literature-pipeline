import os
import pandas as pd

CURVE_FOLDER = "curves_ra/"
OUTPUT_FILE = "data/ra_strain_dataset.csv"

all_data = []

for file in os.listdir(CURVE_FOLDER):
    if file.endswith(".csv"):
        path = os.path.join(CURVE_FOLDER, file)
        print(f"Processing {file}...")

        df = pd.read_csv(path)

        # --- Normalize column names ---
        df.columns = [c.lower().strip() for c in df.columns]

        # Try to identify columns
        ra_col = None
        strain_col = None

        for col in df.columns:
            if "ra" in col:
                ra_col = col
            if "strain" in col:
                strain_col = col

        if ra_col is None or strain_col is None:
            print(f"⚠️ Skipping {file} (columns not recognized)")
            continue

        temp_df = pd.DataFrame({
            "RA_percent": df[ra_col],
            "Strain": df[strain_col],
            "Source": file
        })

        all_data.append(temp_df)

# Combine all files
if all_data:
    final_df = pd.concat(all_data, ignore_index=True)

    # Remove NaNs
    final_df.dropna(inplace=True)

    final_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved {OUTPUT_FILE}")
else:
    print("No valid data found.")
