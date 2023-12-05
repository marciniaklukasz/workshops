cennik = {
    'kawa': 8.90,
    'herbata': 11.50,
    'soczek': 3.99,
    'ciastka': 7.50
}


zamowienie = input("Co chcesz kupic?")
sztuk = int(input("Ile sztuk?"))
cena = sztuk * cennik[zamowienie]
print(f"Chcesz kupic {sztuk} x {zamowienie}, kosztuje to {cena}")