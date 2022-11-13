import pytest
from seasons import Birthdate, number_to_words


def test_invalid_date():
        with pytest.raises(SystemExit):
            Birthdate("")
        with pytest.raises(SystemExit):
            Birthdate("19-02-1988")
        with pytest.raises(SystemExit):
            Birthdate("2025-02-02")

def test_valid():
    assert str(Birthdate("2012-12-12")) == "5215680"
    assert str(Birthdate("2022-10-10")) == "47520"

def test_words():
    assert number_to_words(Birthdate("2012-12-12")) == "Five million, two hundred fifteen thousand, six hundred eighty minutes"
