from palindrom import *
def test_kajak():
    assert palindrom("kajak") == True

def test_wujek():
    assert palindrom ("wujek") == False

def test_baba():
    assert palindrom ("baba") == False

