PY ?= $(if $(wildcard .venv/bin/python),.venv/bin/python,python)
DATA ?= data
TARGET ?= https://example.com

.PHONY: help validate test dossier scan active scan-smb hunt secrets mcp jar vibe deps sbom bgp run ingest watch infra image netcheck re deep llms github dashboard forums experts tools methods all

help:
	@echo "make validate   check schema, links and prose"
	@echo "make test       run the regression suite"
	@echo "make dossier    rebuild examples/dossier.md"
	@echo "make scan TARGET=url-or-path      passive scan"
	@echo "make active TARGET=url            ownership gated active scan"
	@echo "make scan-smb TARGET=url          one-page SMB report"
	@echo "make hunt TARGET=repo             bug hunt, sandbox optional: SANDBOX=1"
	@echo "make secrets TARGET=dir           secret scan with history"
	@echo "make mcp TARGET=dir               MCP config linter"
	@echo "make jar TARGET=file-or-dir       Minecraft plugin triage"
	@echo "make vibe TARGET=dir              Supabase/RLS and client secret checks"
	@echo "make deps TARGET=dir              dependency and OSV match"
	@echo "make sbom TARGET=dir              CycloneDX SBOM"
	@echo "make bgp PREFIX=203.0.113.0/24     passive BGP and RPKI posture"
	@echo "make run TARGET=url-or-dir        run installed specialist tools"
	@echo "make infra TARGET=dir             IaC, K8s and Docker review"
	@echo "make image TARGET=image           container image scan"
	@echo "make netcheck TARGET=dir          exported config audit"
	@echo "make watch TARGET=url             continuous watch"
	@echo "make deep TARGET=binary           scan plus capa, FLOSS and rizin"
	@echo "make re TARGET=binary             deep binary triage"
	@echo "make llms                         rebuild llms-full.txt"
	@echo "make github                       refresh the GitHub atlas"
	@echo "make dashboard                    start the local dashboard"

validate:
	$(PY) scripts/validate.py

test:
	$(PY) -m ruff check scripts tests
	$(PY) -m ruff format --check scripts tests
	$(PY) -m pyright
	$(PY) -m pytest -q

dossier:
	$(PY) scripts/build_dossier.py --data $(DATA) --out examples/dossier.md

scan:
	./beril scan --target $(TARGET)

active:
	./beril scan --target $(TARGET) --active --owned

scan-smb:
	./beril scan --target $(TARGET) --profile smb

hunt:
	./beril hunt --target $(TARGET) $(if $(SANDBOX),--sandbox,)

secrets:
	./beril secrets --target $(TARGET) --history

mcp:
	./beril mcp --target $(TARGET)

jar:
	./beril jar --target $(TARGET)

vibe:
	./beril vibe --target $(TARGET)

deps:
	./beril deps --target $(TARGET) --reachability

sbom:
	./beril sbom --target $(TARGET) --out scans/sbom.cdx.json --licenses scans/licenses.md

bgp:
	./beril bgp --prefix $(PREFIX)

run:
	./beril run --target $(TARGET)

infra:
	./beril infra --target $(TARGET)

image:
	./beril image --target $(TARGET)

netcheck:
	./beril netcheck --target $(TARGET)

watch:
	./beril watch --target $(TARGET)

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
