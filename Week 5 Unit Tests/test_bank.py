from bank import value

def test_uppercase():
    assert value("HELLO") == 0

def test_lowercase():
    assert value("hello") == 0

def test_mixedcase():
    assert value("HelLO") == 0

def test_onlyH():
    assert value("HelL") == 20

def test_noH():
    assert value("Whats up? ") == 100

def test_noinput():
    assert value("") == 100
