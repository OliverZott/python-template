from sample_project.package1.module1 import func1
from sample_project.package2.module2 import func2


def call_func1():
    func1()


def call_func2():
    func2()


# to run:
#   - cd sample_project
#   - > python main.py
if __name__ == "__main__":
    print("sample_project calles as main")
    func1()
    func2()
    call_func1()
    call_func2()
