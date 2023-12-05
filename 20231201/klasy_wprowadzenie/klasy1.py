class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def przedstaw_sie(self):
        print(f"Czesc, jestem {self.imie} {self.nazwisko}")


a = Osoba('Lukasz','Marciniak')
b = Osoba('Adam','Kowalski')

print(a.imie, b.imie)


