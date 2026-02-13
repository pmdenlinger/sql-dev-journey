# apps/index.py
"""
Marimo Launchpad: lists available apps and provides quick-launch links.
Run: python -m marimo run apps/index.py
"""

import marimo as mo

# Create the marimo app
app = mo.App()

@app.cell
def _():
    # Standard imports used below
    from pathlib import Path
    import marimo as mo
    return Path, mo

@app.cell
def _(Path, mo):
    # Discover marimo apps under apps/
    app_dir = Path(__file__).parent
    entries = [
        p for p in sorted(app_dir.glob("*.py"))
        if p.name not in {"index.py", "__init__.py"}
    ]

    rows = []
    for p in entries:
        name = p.stem
        cmd = f"marimo run apps/{p.name}"
        rows.append({
            "App": name,
            "Path": f"apps/{p.name}",
            "Launch command": cmd,
        })

    # UI
    table = mo.ui.table(rows, page_size=10)

    mo.vstack(
        [
            mo.md("# Marimo Apps — Launchpad"),
            mo.md(
                "Select an app below and copy the launch command, "
                "or run directly from your CLI."
            ),
            table,
            mo.md("---"),
            mo.md("Tip: run `marimo run apps/index.py` to open this launcher."),
        ],
        gap=12,
    )
    # Nothing to return; the UI above is the cell output

if __name__ == "__main__":
    app.run()