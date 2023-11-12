setup:
    pip install -r requirements.txt

test:
    python -m pytest

lint:
    flake8 data_processing.py

.PHONY: setup test lint
