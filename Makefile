PY ?= python
DATA ?= data

.PHONY: help validate dossier forums experts tools methods all

help:
	@echo "make validate   check schema, links and prose"
	@echo "make dossier    rebuild examples/dossier.md"
	@echo "make forums     refresh forum and report leads"
	@echo "make experts    refresh expert profiles"
	@echo "make tools      refresh the canonical tool shelf"
	@echo "make methods    refresh method and research leads"

validate:
	$(PY) scripts/validate.py

dossier:
	$(PY) scripts/build_dossier.py --data $(DATA) --out examples/dossier.md

forums:
	$(PY) scripts/harvest.py forums --limit 20

experts:
	$(PY) scripts/harvest.py experts --limit 40

tools:
	$(PY) scripts/harvest.py tools --sources canonical --limit 60

methods:
	$(PY) scripts/harvest.py methods --limit 20

all:
	$(PY) scripts/harvest.py all --out-dir $(DATA) --limit 30
