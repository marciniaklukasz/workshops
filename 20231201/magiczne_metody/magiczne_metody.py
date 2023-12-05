class Liczba:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return f'[{self.x}]'

    def __repr__(self):
        return f'Liczba({self.x})'

    def __add__(self, other):
        return Liczba(self.x + other.x)


liczba1 = Liczba(3)
liczba2 = Liczba(5)
liczba3 = Liczba(7)
suma = liczba1 + liczba2
print(repr(liczba1),liczba2,liczba3, suma)