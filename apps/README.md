# Apps Directory

This folder contains **marimo-based interactive applications** used across the repository. Each app is a pure-Python `.py` file runnable through marimo, providing reproducible, reactive data workflows.

## 📁 Structure
## 🧩 What belongs in `apps/`
Use this folder for:
- Interactive marimo apps
- Parameter-driven UIs
- Exploratory data tools
- Lightweight dashboards
- Compliance / governance visualizers

Do **not** place:
- Library code → use `src/`
- SQL files → use `sql/`
- Jupyter notebooks → use `notebooks/`

## 🚀 Running an app
From repo root:
```bash
marimo run apps/parametric_query_app.py
Apps automatically launch a reactive interface in your browser.
🧪 Developing new apps

Copy an existing file (e.g., parametric_query_app.py).
Rename appropriately.
Replace the data-loading block.
Add UI components with mo.ui.*.
Keep everything self-contained.

🤝 Conventions

One app per file
Snake_case filenames
Keep functions inside the app container (@mo.app())
Prefer pure-Python marimo patterns over Jupyter notebooks

📄 Current apps

parametric_query_app.py — parametric filter, interactive table, save-to-SQLite