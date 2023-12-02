from sample_project.package1.module1 import func1


def func2():
    print("From module2-func2...")
    func1()


# to run:
#   - cd sample_project
#   - > python -m package2.module2
# This command tells Python to run module2.py as a script, and the -m flag allows Python to import the package2 package correctly.
if __name__ == "__main__":
    func2()
