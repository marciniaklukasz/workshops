from collections import __getattr__


class Produkt:
    def __init__(self, id, typ, cena):
        self.id = id
        self.typ = typ
        self.cena = cena

    def print_info(self):
        print (f"Produkt {self.typ} {self.id} {self.cena} PLN")

    def __str__(self):
        return f'Produkt o type {self.typ}, o numerze {self.id} w cenie {self.cena} PLN'


a = Produkt('1', 'Woda', '2.99')
b = Produkt('2', 'Piwo', '7.99')
c = Produkt('3', 'Snaki', '1.99')

a.print_info()
print(a)


