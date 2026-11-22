PY ?= python
DATA ?= data
TARGET ?= https://example.com

.PHONY: help validate dossier scan deep re llms forums experts tools methods all

help:
	@echo "make validate   check schema, links and prose"
	@echo "make dossier    rebuild examples/dossier.md"
	@echo "make scan TARGET=url-or-path   read-only scan"
	@echo "make deep TARGET=binary          scan plus capa, FLOSS and rizin"
	@echo "make re TARGET=binary            deep binary triage"
	@echo "make llms                        rebuild llms-full.txt"
	@echo "make github                      refresh the GitHub atlas"
	@echo "make dashboard                   start the local dashboard"
	@echo "make forums     refresh forum and report leads"
	@echo "make experts    refresh expert profiles"
	@echo "make tools      refresh the canonical tool shelf"
	@echo "make methods    refresh method and research leads"

validate:
	$(PY) scripts/validate.py

dossier:
	$(PY) scripts/build_dossier.py --data $(DATA) --out examples/dossier.md

scan:
	./beril scan --target $(TARGET)

deep:
	./beril scan --target $(TARGET) --deep

re:
	./beril re --target $(TARGET) --capa --floss --rizin

llms:
	$(PY) scripts/build_llms.py

github:
	GITHUB_TOKEN=$$(gh auth token) $(PY) scripts/github_sweep.py --out data/github_atlas.jsonl

dashboard:
	./beril dashboard

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
