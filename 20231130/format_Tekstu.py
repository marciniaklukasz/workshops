def formatuj_tekst(*args, **kwargs):
    wynik = []
    for napis in args:
        for k, v in kwargs.items():
            napis = napis.replace(f'${k}', str(v))
        wynik.append(napis)
    napisy = '\n'.join(wynik)
    return napisy


# Przykładowe użycie:
sformatowany_tekst = formatuj_tekst(
    'Koszt towaru $nazwa wynosi $cena kawalkow zlota',
    cena=10,
    nazwa = 'drzewo'
)

print(sformatowany_tekst)
