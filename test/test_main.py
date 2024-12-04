from sample_project.main import call_func1
from sample_project.main import call_func2


def test_call_func1():
    result = call_func1(1)
    assert result == 2


def test_call_func2():
    result = call_func2()
    assert result == 11
