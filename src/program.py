# GOAL: use sample_project as a package
#
# in folder src (where setup.py lies):
#   - pip install --upgrade .

from sample_project.main import call_func1
from sample_project.main import call_func2

call_func1(1)
call_func2()
