from um import count
import pytest

def test_input():
    assert count("yummy") == 0
    assert count("i u mum u  m") == 0

def test_nospace():
    assert count("um") == 1
    assert count("um, can i... um...maybe... um.. u m go?") == 3

def test_space():
    assert count("  um    ") == 1

def test_case():
    assert count("Um, how you doing friendum?") == 1
    assert count("umm.. UM.. whats uM up??") == 2

def test_special_caracter():
    assert count("UM!!") == 1
    assert count("um!? ok? um.") == 2
