# Python Project Template

This is just a template/skeleton for a plain python project. Provides basic structure and some useful tools, e.g.

- linter / formatter / type-checker with respective pre-commit hooks and configuration
- logging
- unit tests
- vs code launch/settings file

## Prerequisites

### Environment

Generate virtual environment and install packages.

```bash
# Create/activate/deactivate venv
python -m venv venv
.\venv\Scripts\activate
source venv/bin/activate
.\venv\Scripts\deactivate

# Install packages with activated env and check
python -m pip install --upgrade pip
pip install --upgrade -r ./requirements.txt 
pip list

# Freeze and Upgrade current packages  
pip freeze > pip_list.txt   
pip install --upgrade --force-reinstall -r requirements.txt
```

### .env file

Generate .env file if needed e.g. for data path.

- `DATA_BASE_PATH=c:/folder/folder/data/`

### VS Code Tools

Usefull extensions:

- ruff (linter, formatter)
- mypy (type annotation linter)
- autoDocstring - Python Docstring Generator
- Jupyter and Python plugins

Further:

- pytest
- coverage
- pre-commit

## ruff and mypy

Tools can be applied manualle in console or automatically in pipeline on commit/PR. Configuration for manual/local usage is done in **settings.json**. Configuration for pipeline/build-tool usage is done via **pyproject.toml**.

Use Ruff instead of flake8 (linter), black (formatter) and isort (import sorter) separately.

- in root foler: `python .\run_ruff.py`

- **ruff** (linter / formatter)
  - `ruff check .`   ...basic check (linter)
  - `ruff check --fix .` ...fix basic issues (linter)
  - `ruff format --diff .` (show diffs)
  - `ruff format --check .` (show files)
  - `ruff format .` (apply formatter)

- **mypy** (static type annotations)
  - `mypy --exclude venv .`

## Logging

- <https://docs.datalust.co/docs/using-python>
