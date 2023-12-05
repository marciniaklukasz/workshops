from policz_znaki import *

def test_policz_znaki_jeden_tekst():
    wynik = policz_znaki('ala ma <kota> a kot ma ale')
    assert wynik == 4



def test_policz_znaki_dwa_tekst():
    wynik = policz_znaki('<ala> ma <kota> a kot ma ale')
    assert wynik == 7


def test_policz_znaki_dwa_tekst2():
    wynik = policz_znaki ('ala [kota [a kot]] ma [ale]', '[', ']')
    assert wynik == 18