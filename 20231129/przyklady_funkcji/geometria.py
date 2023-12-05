import math
def pole_kwadratu(a):
    return a * a


def pole_prostokata(a, b):
    return a * b


def obwod_kwadratu(a):
    return 4 * a


def obwod_prostokata(a, b):
    return 2 * a + 2 * b

def pole_kola(r):
    return math.pi * r ** 2

def obwod_kola(r):
    return 2 * math.pi * r
def poprawny_trojkat (boka,bokb,bokc):
    '''
    Funkcja sprawdza poprawnosc trojkata
    '''
    return boka + bokb > bokc and bokb + bokc > boka and boka + bokc > bokb


def pole_trojkata(boka, bokb, bokc):
    if not poprawny_trojkat(boka,bokb,bokc):
        raise ValueError(f'Z bokow {boka}, {bokb}, {bokc} nie da sie ulozyc trojkata!')

def obw_trojkata(boka, bokb, bokc):
    p = int ((boka + bokb + bokc))
    return p



'''

print(f'Pole kwadratu o boku 5 to:', pole_kwadratu(5))
print(f'Pole kwadratu o boku 7.5 to:', pole_kwadratu(7.5))
print(f'Pole kwadratu o boku 6.44 to:', pole_kwadratu(6.44))
print(f'Pole kwadratu o boku 5.43 to:', pole_kwadratu(5.43))
'''