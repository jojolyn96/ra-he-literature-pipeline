install:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

run:
	. venv/bin/activate && python main.py

extract:
	. venv/bin/activate && python scripts/process_pdfs.py

all: install run extract
