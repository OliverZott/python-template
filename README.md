# Python Project Template

A simple template/skeleton for a plain python project. It provides basic structure and some useful tools and sample-code like

- linter / formatter / type-checker
- vs code launch/tasks/settings file
- package installation example using **setuptools** package
- pytest example using **pytest** package
- github example pipeline to run unit tests

TODO:

- logging
- pre-commit hooks and configuration

## Prerequisites

### Environment

Generate virtual environment and install packages.

```bash
# Create/activate/deactivate venv
python -m venv venv
.\venv\Scripts\activate  # windows
source venv/bin/activate  # linux

# Install packages with activated env and check
python -m pip install --upgrade pip
pip install --upgrade -r ./requirements.txt 
pip list

# Freeze / Upgrade current packages  
pip freeze > pip_list.txt   
pip install --upgrade --force-reinstall -r requirements.txt
```

### VS Code Extensions

In VS Code extensions view use `@recommended` to install extensions defined in .extensions.json

### .env file

Generate .env file if needed e.g. for data path.

- `DATA_BASE_PATH=c:/folder/folder/data/`

## Tools

- ruff (linter, formatter)
- mypy (type annotation linter)
  - if **Extension** installed, add rule: Search for mypy in Settings and ad "Mypy-type-checker args": ``"python.linting.mypyArgs": [     "--ignore-missing-imports" ]``
- autoDocstring - Python Docstring Generator
- Jupyter and Python plugins

Further:

- pytest
- coverage
- pre-commit

### ruff and mypy

Tools can be applied manualle in console or automatically in pipeline on commit/PR. Configuration for manual/local usage is done in **settings.json**. Configuration for pipeline/build-tool usage is done via **pyproject.toml**.

Ruff instead of flake8 (linter), black (formatter) and isort (import sorter) separately.

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
