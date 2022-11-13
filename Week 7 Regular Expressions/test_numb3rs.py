from numb3rs import validate

def test_correct():
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True
    assert validate("0.0.0.0") == True
def test_incorect():
    assert validate("255.255.512.255") == False
    assert validate("1.2.3.1000") == False
def test_input():
    assert validate("") == False
    assert validate("512.512.512.512.512.512") == False
    assert validate("0.0.1") == False
def test_non_numeric():
    assert validate("cat") == False
    assert validate("cat.dog.0.1") == False
