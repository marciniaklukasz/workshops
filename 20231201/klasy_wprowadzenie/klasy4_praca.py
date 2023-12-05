class Pracownik:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.suma_godzin = 0
        self.suma_nadgodzin = 0

    def praca(self, godziny):
        if godziny > 8:
            self.suma_godzin += 8
            self.suma_nadgodzin += godziny - 8
        else:
            self.suma_godzin += godziny

    def wyplata(self):
        return self.suma_godzin * self.stawka + self.suma_nadgodzin * self.stawka * 2


p = Pracownik ('Jan', 'Kowalski', 100)
p.praca (10)
print ("Przelew dla Ciebie: ", p.wyplata ())

