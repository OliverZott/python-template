# Example

Example for:

- installing/using a package [link](https://www.tutorialsteacher.com/python/python-package)
- running pytests
- logging (todo)

## Run `program.py`

- `pip install --upgrade .` ...in **src** folder (after each change in sample_project) to install sample_project package.
- `python .\programm.py` ...in **src** folder

## Run unit tests

### VS Code

- Via Integrated test view in pirmary side bar if python extension is installed
- Via `Pytest` launch configuration in debug view

### Terminal

- `pytest` or `pytest -pdb` (for debugging) in root dir

## Run specific Tasks

e.g.

- Debug:  `Python: Current File` in Debug View
- Run: `ctrl + shift + p` select `Tasks: Run Task` and use `Python: Current File`
