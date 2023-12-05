cennik = {
    'kawa': 8.90,
    'herbata': 11.50,
    'soczek': 3.99,
    'ciastka': 7.50
}
"""suma = 0
while True:
    zamowienie = input("Podaj nazwe produktu (lub nacisnij enter aby przerwac): ")
    if not zamowienie: break
    if zamowienie not in cennik:
        print("Nie ma takiego produktu")
        continue
    sztuk = int(input("Ile sztuk?: "))
    cena = sztuk * cennik[zamowienie]
    suma += cena
    print(f"Chcesz kupic {sztuk} x {zamowienie}, kosztuje to {cena:.2f} Twoj koszyk ma wartosc: {suma:.2f}zl")


print(f"Suma: {suma:.2f}")
"""
for towar,cena in (cennik.items()):
    print(towar,cena)