from twttr import shorten

def test_uppercase():
    assert shorten("03.07.2022: IM FINE, THANKS FOR ASKING") == "03.07.2022: M FN, THNKS FR SKNG"

def test_lowercase():
    assert shorten("03.07.2022: im fine, thanks for asking") == "03.07.2022: m fn, thnks fr skng"

def test_mixedcase():
    assert shorten("03.07.2022: Im FiNE, tHAnKs For ASKing") == "03.07.2022: m FN, tHnKs Fr SKng"

def test_onlyvowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("AeIU") == ""

def test_NOvowels():
    assert shorten("m FN, tHnKs Fr SKng") == "m FN, tHnKs Fr SKng"
