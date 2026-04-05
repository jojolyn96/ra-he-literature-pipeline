# Install dependencies
install:
    python3 -m venv venv
    . venv/bin/activate && pip install -r requirements.txt

# Run full pipeline
run:
    . venv/bin/activate && python main.py

# Process PDFs
extract:
    . venv/bin/activate && python scripts/process_pdfs.py

# Full pipeline (recommended entry point)
all: install run extract
