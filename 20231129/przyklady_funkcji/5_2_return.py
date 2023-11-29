'''def ile_sekund_do_konca_minuty():
    from datetime import datetime
    return 60 - datetime.now ().second
def ile_minut_do_konca_godziny():
    from datetime import datetime
    return 60 - datetime.now ().minute

def kwadrat(x):
    return x*x

print('Funkcje zdefiniowane, poczatek wlasciwego programu: \n')
print('Uruchomie teraz funkcje ile_sekund_do_konca_minuty poraz pierwszy')
ile_sekund_do_konca_minuty()

print("Uruchomie teraz funkcje zapisujac wynik do zmiennej.")
ile_sekund = ile_sekund_do_konca_minuty()
ile_minut = ile_minut_do_konca_godziny()
print(f'Wynik to:',ile_sekund)
print(f'Wynik to:',ile_minut)

wynik = kwadrat(5)
print(wynik)'''


def stawka_za_prace(stawka_podstawowa, dzien_tygodnia):
    if 1 <= dzien_tygodnia <= 5:
        return stawka_podstawowa
    if dzien_tygodnia == 6:
        return 1.5 * stawka_podstawowa
    if dzien_tygodnia == 7:
        return 2 * stawka_podstawowa
def dzielenie_z_reszta(x, y):
    return x // y, x % y

tupla = dzielenie_z_reszta(13, 5)
print(tupla, 'typu', type(tupla))
print('iloraz:', tupla[0], 'reszta:', tupla[1])

# "upacking":
a, b = dzielenie_z_reszta(77, 5)
print('iloraz:', a, 'reszta:', b)


print('Sroda: ', stawka_za_prace(20,3))
print('CZwartek: ', stawka_za_prace(20,4))
print('Sobota: ', stawka_za_prace(20,6))


