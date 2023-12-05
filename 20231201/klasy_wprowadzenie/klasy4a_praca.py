from klasy4_praca import Pracownik


class PracownikPlus (Pracownik):
    def __init__(self, imie, nazwisko, stawka):
        super ().__init__ (imie, nazwisko, stawka)
        self.suma_premii = 0

    def premia(self, kwota_premii):
        self.suma_premii += kwota_premii

    def wyplata(self):
        try:
            return super ().wyplata () + self.suma_premii
        finally:
            self.suma_premii = 0



#albo

class PracownikPlus2(Pracownik):
    def premia(self,kwota_premii):
        self.kasa += kwota_premii
        print(PracownikPlus2.kasa(5))