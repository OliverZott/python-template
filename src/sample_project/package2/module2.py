from sample_project.package1.module1 import func1


def func2() -> int:
    print("Inside module2-func2, calling func1(10) from module1: ")
    return func1(10)


# to run:
#   - change code to use second import statement
#   - cd sample_project
#   - > python -m package2.module2
# This command tells Python to run module2.py as a script, and the -m flag allows Python to import the package2 package correctly.
if __name__ == "__main__":
    print("module2 calles as main")
    func2()
