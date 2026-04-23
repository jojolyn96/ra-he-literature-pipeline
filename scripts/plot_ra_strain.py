import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv("data/ra_strain_dataset.csv")

# Clean data
df = df.dropna(subset=["RA_percent", "Strain"])
df["RA_percent"] = pd.to_numeric(df["RA_percent"], errors="coerce")
df["Strain"] = pd.to_numeric(df["Strain"], errors="coerce")
df = df.dropna()

# --- Create figure ---
plt.figure(figsize=(6, 5))

# Scatter plot
plt.scatter(df["Strain"], df["RA_percent"], alpha=0.7)

# --- Regression line ---
if len(df) > 2:
    x = df["Strain"]
    y = df["RA_percent"]

    coeffs = np.polyfit(x, y, 1)
    trend = np.poly1d(coeffs)

    # sort for clean line
    idx = np.argsort(x)
    plt.plot(x.iloc[idx], trend(x.iloc[idx]))

# Labels
plt.xlabel("Strain (%)", fontsize=12)
plt.ylabel("Retained Austenite (%)", fontsize=12)
plt.title("Retained Austenite vs Strain (Literature Data)", fontsize=13)

# Improve layout
plt.tight_layout()

# Save high-quality figure
plt.savefig("data/ra_vs_strain.png", dpi=300)

print("Saved publication-quality plot to data/ra_vs_strain.png")
