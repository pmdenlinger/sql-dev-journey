# tests/test_foundations.py
from pathlib import Path
from src.db.foundations import run_query, executescript_from_file

TEST_DB = "test_output.db"
SEED = "sql/quickstart/00_seed.sql"


def test_seed_and_select():
    # Ensure fresh test DB
    if Path(TEST_DB).exists():
        Path(TEST_DB).unlink()

    executescript_from_file(SEED, db_path=TEST_DB)
    df = run_query("SELECT COUNT(*) AS n FROM customers", db_path=TEST_DB)
    assert df.loc[0, "n"] >= 1
