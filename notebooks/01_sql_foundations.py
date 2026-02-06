import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### SQL Foundations

    This notebook establishes foundational SQL concepts using an existing SQLite database. The goal is to develop fluency in exploring schemas, writing clear queries, and interpreting results.

    The progression of topics reflects widely accepted SQL fundamentals commonly introduced in introductory SQL literature. The database is used as-is to establish baseline query patterns; all queries, commentary, and interpretations are original and adapted for legal, audit, and compliance reporting contexts.

    The database is treated as an external system under review, reflecting common real‑world scenarios in audit and compliance analysis.
    """)
    return


@app.cell
def _(DB_PATH, mo, result):
    _df = mo.sql(
        f"""
        # --- Environment & SQLite connection (read-only) ---
        # --- Database treated as an external system under review ---

        import sqlite3
        from pathlib import Path

        # Path to the external SQLite database (not versioned)
        DB_PATH = Path("data/raw/sTunes.db")

        # Defensive check: ensure the DB exists
        assert DB_PATH.exists(), f"Database not found at: {DB_PATH.resolve()}"

        # Open a read-only SQLite connection
        conn = sqlite3.connect(
            f"file:{DB_PATH.as_posix()}?mode=ro",
            uri=True
        )

        # Enable name-based column access (useful later)
        conn.row_factory = sqlite3.Row

        # Sanity check: verify database integrity
        result = conn.execute("PRAGMA integrity_check;").fetchone()[0]
        assert result == "ok", f"SQLite integrity check failed: {result}"

        result  # Should display 'ok'
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Next Steps

    This notebook establishes foundational SQL query patterns and schema reasoning.

    Subsequent sections build on this foundation by introducing:

    - Performance considerations and query planning
    - Large‑scale audit and log datasets
    - Compliance, defensibility, and Microsoft Purview / Entra reporting scenarios
    """)
    return


if __name__ == "__main__":
    app.run()
