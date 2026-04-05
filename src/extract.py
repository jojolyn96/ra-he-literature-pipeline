import pdfplumber
import re

def extract_text_from_pdf(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except:
        return ""
    return text


def extract_properties(text):
    data = {}

    text_lower = text.lower()

    # --- Retained Austenite %
    ra_matches = re.findall(r"(\d+\.?\d*)\s*%\s*retained austenite", text_lower)
    if ra_matches:
        data["RA_percent"] = float(ra_matches[0])

    # --- Strain rate
    strain_match = re.search(r"strain rate.*?(\d+\.?\d*\s*e?-?\d*)", text_lower)
    if strain_match:
        data["Strain_rate"] = strain_match.group(1)

    # --- Test type
    if "slow strain rate" in text_lower or "ssrt" in text_lower:
        data["Test_type"] = "SSRT"
    elif "notched" in text_lower:
        data["Test_type"] = "Notched"

    # --- Hydrogen mention
    if "electrochemical charging" in text_lower:
        data["Hydrogen_condition"] = "electrochemical"

    # --- Morphology (simple heuristic)
    if "film-like" in text_lower:
        data["RA_morphology"] = "film"
    elif "blocky" in text_lower:
        data["RA_morphology"] = "blocky"

    return data
