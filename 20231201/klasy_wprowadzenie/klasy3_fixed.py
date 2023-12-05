# Tu mamy "normalne klasy", bez żadnych sztuczek technicznych.

class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __str__(self):
        return f'{self.imie} {self.nazwisko} ({self.wiek} lat)'

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat')

    def jest_pelnoletnia(self):
        return self.wiek >= 18


class Sklep:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.cennik = {}
        self.kasa = 0

    def zdefiniuj_produkt(self, produkt, cena):
        # informację o produkcie zapamiętujemy w słowniku "cennik", który został utworzony w init
        self.cennik[produkt] = cena

    def sprzedaj(self, produkt, klient, sztuk=1):
        if produkt not in self.cennik:
            print("Nie ma takiego produktu w naszej ofercie.")
        elif produkt in {'piwo'} and not klient.jest_pelnoletnia():
            print(f'Osobom niepełnoletnim nie sprzedajemy {produkt}.')
        else:
            koszt = self.cennik[produkt] * sztuk
            print(f'Kliencie {klient.imie}, za swoje zakupy płacisz {koszt}')
            self.kasa += koszt


# W tym przykładzie używamy klasy od razu w tym samym pliku,
# ale w praktyce częściej w jednym pliku definiuje się klasę, a w innym importuje i korzysta.

ala = Osoba('Ala', 'Kowalska', 30)
bartek = Osoba(imie='Bartek', nazwisko='Malinowski', wiek=15)
print(ala)
print(bartek)

print('\nOsoby się przedstawiają:')
ala.przedstaw_sie()
if ala.jest_pelnoletnia():
    print(f'{ala.imie} jest osobą pełnoletnią')
else:
    print(f'{ala.imie} jest osobą niepełnoletnią')
bartek.przedstaw_sie()
if bartek.jest_pelnoletnia():
    print(f'{bartek.imie} jest osobą pełnoletnią')
else:
    print(f'{bartek.imie} jest osobą niepełnoletnią')
print()

zabka = Sklep(nazwa='Żabka')
zabka.zdefiniuj_produkt('cola', 6)
zabka.zdefiniuj_produkt('piwo', 7.50)
print('Produkty dostępne w Żabce:', zabka.cennik)

zabka.sprzedaj('sok', ala)
