from cennik import cennik_lista

lista_zakupow = {}
while True:
    print('Co chcesz zrobić?:\n'
          '* Z - Zakupy\n'
          '* C - Ustaw cenę produktu\n'
          '* U - Usuń produkt z cennika\n'
          '* Q - Wyjście z programu')
    wybor = input('Twój wybór: ').upper()

    if wybor == 'Q':
        print('Koniec programu.')
        break
    elif wybor == 'Z':
        suma = 0

        print("Witaj w sklepie!")
        while True:
            zamowienie = input("Co chcesz kupić? (q - wyjście): ").lower()
            if zamowienie == 'q':
                print("Zakończenie zakupów.")
                break
            elif zamowienie in cennik_lista:
                cena = round(float(cennik_lista[zamowienie]), 2)
                lista_zakupow[zamowienie] = cena
                suma += cena
                print(f"Dodano {zamowienie} za {cena} zł. Suma: {suma} zł.")
            else:
                print("Produkt nieznaleziony w cenniku!")
    elif wybor == 'C':
        produkt = input("Podaj nazwę produktu: ").lower()
        try:
            nowa_cena = float(input(f"Podaj cenę dla produktu {produkt}: "))
            cennik_lista[produkt] = nowa_cena
            print(f"Ustawiono cenę {nowa_cena} zł dla produktu {produkt}.")
        except ValueError:
            print("Nieprawidłowa wartość ceny!")
    elif wybor == 'U':
        delete = input("Podaj nazwę produktu do usunięcia: ").lower()
        if delete in cennik_lista:
            del cennik_lista[delete]
            print(f"Produkt {delete} został usunięty z cennika.")
        else:
            print("Taki produkt nie istnieje w cenniku!")
    else:
        print("Nieprawidłowy wybór!")

if lista_zakupow:
    print("\nLista zakupów:")
    for i, (produkt, cena) in enumerate(lista_zakupow.items()):
        print (f"{produkt:<20}{cena:>10.2f} zł")
print ("-"*10)
print (f"Suma to:{suma:>22.2f} zl")


