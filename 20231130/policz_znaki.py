from policz_znaki import *
napis = "<Ala> ma kota"
def policz_znaki(napis, znak_otwierajacy, znak_zamykajacy):
    wynik = 0
    poziom = 0
    czy_liczyc = False
    for znak in napis:
        if znak == znak_otwierajacy:
            poziom += 1
        elif znak == znak_zamykajacy:
            poziom -= 1
        elif poziom > 0:
            wynik += poziom
    return wynik


