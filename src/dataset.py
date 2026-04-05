import pandas as pd

def initialize_dataset():
    columns = [
        "Paper_ID", "Alloy_System", "RA_percent", "RA_morphology",
        "Test_type", "Hydrogen_condition", "Strain_rate",
        "Fracture_strain_H", "Fracture_strain_noH",
        "HE_index", "Source"
    ]
    return pd.DataFrame(columns=columns)

def compute_he_index(eps_h, eps_noh):
    if eps_h is not None and eps_noh is not None:
        return (eps_noh - eps_h) / eps_noh
    return None

def add_entry(df, entry):
    entry["HE_index"] = compute_he_index(
        entry.get("Fracture_strain_H"),
        entry.get("Fracture_strain_noH")
    )
    return pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
