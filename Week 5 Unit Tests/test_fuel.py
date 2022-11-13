from fuel import convert, gauge
import pytest

# test if ZeroDivisionError is raised
def test_exception1():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# Test if ValueError is raised
def test_exception2():
    with pytest.raises(ValueError):
        convert("a/b")

def test_exception3():
    with pytest.raises(ValueError):
        convert("2/1")

# Test a correct input
def test_corectinput():
    assert convert("1/2") == 50
# Test if function returns "E"
def test_empty():
    assert gauge(1) == "E"

# Test if function returns "F"
def test_full():
    assert gauge(99) == "F"

# Test a correct integer
def test_half():
    assert gauge(50) == "50%"
