from plates import is_valid

def test_lenght1():
    assert is_valid("CS50000") == False

def test_lenght2():
    assert is_valid("C") == False

def test_noinput():
    assert is_valid("") == False

def test_numbers1():
    assert is_valid("CS50P") == False

def test_numbers2():
    assert is_valid("12345") == False

def test_number0():
    assert is_valid("CS050") == False

def test_letters():
    assert is_valid("CSSOP") == True

def test_nonAlphaNum():
    assert is_valid("CS%)") == False

def test_correctInput():
    assert is_valid("CS50") == True
