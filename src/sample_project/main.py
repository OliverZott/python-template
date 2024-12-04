from sample_project.package1.module1 import func1
from sample_project.package2.module2 import func2


def call_func1(input: int) -> int:
    return func1(input)


def call_func2() -> int:
    return func2()


# to run:
#   - cd sample_project
#   - > python main.py
if __name__ == "__main__":
    print("sample_project calles as main")
    func1(1)
    func2()
    call_func1(1)
    call_func2()
