# parametric_query_app.py
# A marimo app providing a parametric filter, interactive table selection, and a "Save to SQLite" button.
# Run with:  marimo run parametric_query_app.py

import marimo as mo

@mo.app()
def app():
    import pandas as pd
    import sqlite3

    # --- Parameters UI ---
    query_param = mo.ui.text(value="example", label="Query parameter (contains match)")

    # Example base dataframe; replace with your own query/load logic
    base_df = pd.DataFrame({
        "name": ["alpha", "beta", "gamma", "alphabet", "betamax"],
        "value": [1, 2, 3, 10, 20],
    })

    @mo.memvar
    def filtered_df():
        q = (query_param.value or "").strip()
        if not q:
            return base_df
        return base_df[base_df["name"].str.contains(q, case=False, na=False)].reset_index(drop=True)

    # --- Interactive table with multi-row selection ---
    table = mo.ui.table(
        data=lambda: filtered_df(),
        selection="multi",  # allows selecting multiple rows
        height=260,
        page_size=10,
    )

    save_btn = mo.ui.button(label="Save selection to SQLite", variant="solid")
    status_msg = mo.ui.text(label="Status", value="", disabled=True)

    @save_btn.on_click
    def _(_event):
        df = filtered_df()
        sel = table.value or []  # list of selected row indices
        if len(sel) == 0:
            status_msg.value = "No rows selected."
            mo.toast.info("Select one or more rows to save.")
            return
        sel_df = df.iloc[sel]
        with sqlite3.connect("output.db") as conn:
            sel_df.to_sql("selected_rows", conn, if_exists="replace", index=False)
        status_msg.value = f"Saved {len(sel_df)} row(s) to output.db:selected_rows"
        mo.toast.success(status_msg.value)

    layout = mo.vstack([
        mo.hstack([query_param]),
        mo.md("""
        **Instructions**
        1. Enter a query string to filter rows by `name` (case-insensitive contains).
        2. Select one or more rows in the table.
        3. Click **Save selection to SQLite** to write to `output.db` → table `selected_rows`.
        """),
        table,
        mo.hstack([save_btn]),
        status_msg,
    ], gap=12)

    return layout
