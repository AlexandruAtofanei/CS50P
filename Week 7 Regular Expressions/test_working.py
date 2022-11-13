from working import convert
import pytest

def test_format():
    with pytest.raises(ValueError):
         convert("09:00 AM - 7:00 PM")

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

def test_no_input():
    with pytest.raises(ValueError):
         convert("")

def test_time_values():
    with pytest.raises(ValueError):
         convert("09:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
         convert("09:60 AM to 07:00 PM")
    with pytest.raises(ValueError):
         convert("13:34 AM to 13:00 PM")

def test_convert():
    assert convert("09:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 11:59 AM") == "00:00 to 11:59"
