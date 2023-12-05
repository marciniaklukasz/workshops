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


class Student(Osoba):
    pass


class Sklep:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.cennik = {}
        self.kasa = 0

    def zdefiniuj_produkt(self, produkt, cena):
        self.cennik[produkt] = cena

    def sprzedaj(self, produkt, klient, sztuk=1):
        if produkt not in self.cennik:
            print(f'Nieznany produkt: {produkt}')
        elif produkt in {'piwo'} and not klient.jest_pelnoletnia():
            print(f'Osobom niepełnoletnim nie sprzedajemy {produkt}')
        else:
            koszt = self.cennik[produkt] * sztuk
            print(f'Kliencie {klient.imie}, za swoje zakupy płacisz {koszt}')
            self.kasa += koszt


osoba = Osoba('Ala', 'Kowalska', 40)
student = Student('Bartek', 'Nowakowski', 20)

print('osoba:', osoba, 'typu', type(osoba))
print('student:', student, type(student))
osoba.przedstaw_sie()
student.przedstaw_sie()
