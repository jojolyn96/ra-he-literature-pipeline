# Install dependencies
install:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

# Run paper search
run:
	. venv/bin/activate && python main.py

# Process PDFs
extract:
	. venv/bin/activate && python scripts/process_pdfs.py

# Build RA vs strain dataset
ra_dataset:
	. venv/bin/activate && python scripts/build_ra_strain_dataset.py

plot:
	. venv/bin/activate && python scripts/plot_ra_strain.py

search:
	. venv/bin/activate && python main.py
# Full pipeline
all: extract ra_dataset plot

