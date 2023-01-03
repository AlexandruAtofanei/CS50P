import pytest
from project import authenticate, register_user, register_plate, register_passw, recover

'''
testing was done with the consideration that in database there is at least the folowing data for one user:
alex29!,nt08cfj,alex29!#
'''

def test_authenticate():
    with pytest.raises(ValueError):
        authenticate("mihai25","123321!")
    with pytest.raises(ValueError):
        authenticate("","")
    with pytest.raises(ValueError):
        authenticate("","")
    assert authenticate("alex29!", "alex29!#") == "alex29!"

def test_register_user():
    assert register_user("alex27!") == True
    assert register_user("alex29!") == False
    with pytest.raises(ValueError):
        register_user("aa")
    with pytest.raises(ValueError):
        register_user("Tom")
    with pytest.raises(ValueError):
        register_user("Tomas1)")
    with pytest.raises(ValueError):
        register_user("")

def test_register_plate():
    assert register_plate("nt08cfj") == False
    assert register_plate("nt09cfj") == True
    with pytest.raises(ValueError):
        register_plate("nt0cfj")
    with pytest.raises(ValueError):
        register_plate("0110cfj")
    with pytest.raises(ValueError):
        register_plate("aabbcc")
    with pytest.raises(ValueError):
        register_plate("")

def test_register_passw():
    assert register_passw("alex27!#") == True
    with pytest.raises(ValueError):
        register_passw("alex27!(")
    with pytest.raises(ValueError):
        register_passw("ale")
    with pytest.raises(ValueError):
        register_passw(" ")

def test_recover():
    assert recover("alex29!","nt08cfj") == "\nUser found, your password is: alex29!#\n"
    assert recover("mathew", "b08aaa") == "\nUsername or license plate number are not correct.\n"
    assert recover("", "") == "\nUsername or license plate number are not correct.\n"

