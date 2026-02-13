# Use the project-local virtualenv's Python
PYTHON := /Users/pauldenlinger/Desktop/Github-Repositories/sql-dev-journey/.venv/bin/python

.PHONY: run index seed test diag

# Launch the marimo apps index (UI launcher)
index:
	$(PYTHON) -m marimo run apps/index.py

# Launch the SQL quickstart marimo app
run:
	$(PYTHON) -m marimo run apps/sql_quickstart_foundations.py

# Seed the SQLite database
seed:
	$(PYTHON) -c "from src.db.foundations import executescript_from_file; \
	executescript_from_file('src/db/sql/00_seed.sql')" && \
	echo "Seeded SQLite at $${DB_PATH:-output.db}"

# Run tests quietly (via the venv)
test:
	$(PYTHON) -m pytest -q

# Diagnostics: show Python and marimo info
diag:
	@echo "python: $(PYTHON)"
	@$(PYTHON) -V
	@echo "marimo bin: $$(command -v marimo || true)"
	@$(PYTHON) -m marimo --version || true
	@$(PYTHON) -c "import sys; print('sys.executable =', sys.executable)"
	@$(PYTHON) -c "import shutil; print('which marimo =', shutil.which('marimo'))"
	@$(PYTHON) -c "import importlib.util; print('marimo importable =', importlib.util.find_spec('marimo') is not None)"
