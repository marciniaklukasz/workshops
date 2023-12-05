class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __str__(self):
        return f'{self.imie} {self.nazwisko} ({self.wiek} lat)'

    def przedstaw_sie(self):
        print (f'Nazywam sie {self.imie} {self.nazwisko} i mam {self.wiek} lat :-)')

    def pelnoletnosc(self):
        return self.wiek >= 18


class Sklep:

    def __init__(self, nazwa_sklepu, branza, cennik):
        self.nazwa = nazwa_sklepu
        self.branza = branza
        self.cennik = {}

    def zdefiniuj_produkt(self, nazwa_produktu, cena, branza):
        self.cennik[nazwa_produktu] = cena

    def sprzedaj(self, nazwa_produktu, klient, sztuk=1):
        koszt = self.cennik[nazwa_produktu]
        print (f'Kliencie {klient.imie}, za swoje zakupy zapłacisz {koszt}')


a = Osoba ('Ala', 'Kowalska', 30)
b = Osoba ('Adam', 'Kowalski', 35)

print ('Osoby sie przedstawiaja:\n')
a.przedstaw_sie ()
if a.pelnoletnosc ():
    print (f'{a.imie} jest osoba pelnoletnia.')
b.przedstaw_sie ()


zabka = Sklep(nazwa_sklepu='Żabka')
zabka.zdefiniuj_produkt('cola',6)
zabka.zdefiniuj_produkt('piwo',7.5)
print('Produkty dostepne w Zabce: ', zabka.cennik)