# src/db/foundations.py
"""
Reusable database helpers for marimo apps and other modules.
- Uses SQLite by default (file path via DB_PATH env var or provided argument)
- Provides:
    - get_connection(db_path)
    - run_query(sql, params, db_path) -> pandas.DataFrame
    - exec_sql(sql, params, db_path) -> None
    - executescript_from_file(path, db_path) -> None
    - load_sql(path) -> str
"""
from __future__ import annotations
import os
import sqlite3
from pathlib import Path
from typing import Optional, Union
import pandas as pd

DEFAULT_DB_PATH = os.getenv("DB_PATH", "output.db")


def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    """Return a SQLite connection to the given database path (or default)."""
    return sqlite3.connect(db_path or DEFAULT_DB_PATH)


def run_query(sql: str, params: Union[tuple, dict, None] = None, db_path: Optional[str] = None) -> pd.DataFrame:
    """Run a SELECT query and return a DataFrame."""
    with get_connection(db_path) as conn:
        return pd.read_sql_query(sql, conn, params=params)


def exec_sql(sql: str, params: Union[tuple, dict, None] = None, db_path: Optional[str] = None) -> None:
    """Execute a single SQL statement (non-SELECT or DDL)."""
    with get_connection(db_path) as conn:
        cur = conn.cursor()
        if params is None:
            cur.execute(sql)
        else:
            cur.execute(sql, params)
        conn.commit()


def executescript_from_file(path: str, db_path: Optional[str] = None) -> None:
    """Execute a multi-statement SQL script from a file."""
    script = Path(path).read_text(encoding="utf-8")
    with get_connection(db_path) as conn:
        conn.executescript(script)


def load_sql(path: str) -> str:
    """Load a SQL file and return its text."""
    return Path(path).read_text(encoding="utf-8")
