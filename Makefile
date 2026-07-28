.PHONY: build test clean

VENV ?= .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

build:
	test -d $(VENV) || python3 -m venv $(VENV)
	$(PIP) install -q -r requirements.txt
	$(PYTHON) -m compileall -q src

test:
	$(PYTHON) -m pytest -q

clean:
	rm -rf $(VENV) .pytest_cache __pycache__ src/**/__pycache__ tests/**/__pycache__
