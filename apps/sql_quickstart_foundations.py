# apps/sql_quickstart_foundations.py
"""
Marimo app: SQL QuickStart foundations

Features:
- Initialize a demo SQLite database from a seed SQL script.
- Select a "lesson" (SQL file) from sql/quickstart and run it.
- Preview the SQL and view results in an interactive table.

Run with:
    marimo run apps/sql_quickstart_foundations.py

Dependencies:
    - marimo
    - pandas
"""
import marimo as mo
from pathlib import Path
from src.db.foundations import run_query, load_sql, executescript_from_file, DEFAULT_DB_PATH

LESSONS = {
    "01_select_basics": "sql/quickstart/01_select_basics.sql",
    "02_where_order":  "sql/quickstart/02_where_order.sql",
    "03_joins":        "sql/quickstart/03_joins.sql",
    "04_group_by":     "sql/quickstart/04_group_by.sql",
}

SEED_SCRIPT = "sql/quickstart/00_seed.sql"

@mo.app()
def app():
    # --- Controls ---
    db_path = mo.ui.text(value=DEFAULT_DB_PATH, label="SQLite DB path")
    init_btn = mo.ui.button(label="Initialize demo DB (seed)", variant="solid")
    lesson = mo.ui.select(options=list(LESSONS.keys()), value="01_select_basics", label="Lesson")
    run_btn = mo.ui.button(label="Run SQL", variant="solid")

    status = mo.ui.text(label="Status", value="", disabled=True)
    table = mo.ui.table(data=lambda: [], height=300, page_size=10)

    # --- Derived SQL text ---
    @mo.memvar
    def sql_text():
        return load_sql(LESSONS[lesson.value])

    # --- Seed button behavior ---
    @init_btn.on_click
    def _(_e):
        try:
            executescript_from_file(SEED_SCRIPT, db_path=db_path.value)
            status.value = f"DB initialized with seed data → {db_path.value}"
            mo.toast.success(status.value)
        except Exception as ex:
            status.value = f"Seed error: {ex}"
            mo.toast.error(status.value)

    # --- Run button behavior ---
    @run_btn.on_click
    def _(_e):
        try:
            df = run_query(sql_text(), db_path=db_path.value)
            table.data = df
            status.value = f"OK: {len(df)} row(s)"
            mo.toast.success(status.value)
        except Exception as ex:
            status.value = f"Query error: {ex}"
            mo.toast.error(status.value)

    # --- Layout ---
    return mo.vstack([
        mo.md("# SQL QuickStart — Foundations"),
        mo.hstack([db_path, init_btn], gap=12),
        lesson,
        mo.md("**SQL Preview**"),
        mo.ui.code(lambda: sql_text(), language="sql"),
        mo.hstack([run_btn], gap=12),
        status,
        table,
    ], gap=12)
