import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo






    return (mo,)


@app.cell
def _(mo):
    def setup_sqlite():
        mo.sql("INSTALL sqlite;")
        mo.sql("LOAD sqlite;")
        mo.sql("""
            ATTACH OR REPLACE '/Users/pauldenlinger/Desktop/sTunes.db'
              AS sqlite_db (TYPE sqlite, READ_ONLY FALSE);
        """)

    setup_sqlite()
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SHOW DATABASES;
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT schema_name, table_name
        FROM duckdb_tables()
        WHERE database_name = 'sqlite_db';
        """
    )
    return


if __name__ == "__main__":
    app.run()
