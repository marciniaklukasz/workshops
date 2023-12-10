from cennik import cennik_lista
from magazyn import magazyn_lista
import csv

def zapisz_do_pliku(plik_, cennik, magazyn):
    with open(plik_, mode='w', newline='') as plik:
        writer = csv.writer(plik)
        writer.writerow(['Produkt', 'Cena', 'Ilosc'])
        for produkt in cennik:
            writer.writerow([produkt, cennik[produkt], magazyn.get(produkt, 0)])

def odczytaj_z_pliku(plik__):
    with open(plik__, mode='r') as plik:
        reader = csv.DictReader(plik)
        cennik = {}
        magazyn = {}
        for row in reader:
            produkt = row['Produkt']
            cennik[produkt] = float(row['Cena'])
            magazyn[produkt] = int(row['Ilosc'])
        return cennik, magazyn

lista_zakupow = {}
suma = 0
while True:
    print('Co chcesz zrobić?:\n'
          '* Z - Zakupy\n'
          '* C - Ustaw cenę produktu\n'
          '* U - Usuń produkt z cennika\n'
          '* D - Dostawa towaru\n'
          '* R - Odczyt danych z pliku\n'
          '* W - Zapis danych do pliku\n'
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
            elif zamowienie in cennik_lista and magazyn_lista:
                if magazyn_lista[zamowienie] > 0:
                    cena = round(float(cennik_lista[zamowienie]), 2)
                    stan_magazynowy = (magazyn_lista[zamowienie]) - 1
                    lista_zakupow[zamowienie] = cena
                    suma += cena
                    print(f"Dodano {zamowienie} za {cena} zł. Suma: {suma} zł")
                else:
                    print("Sorry, mamy braki na sklepie!")
            else:
                print("Sorry, nie mamy takiego produktu!")
    elif wybor == 'C':
        produkt = input("Podaj nazwę produktu: ").lower()
        try:
            nowa_cena = float(input(f"Podaj cenę dla produktu {produkt}: "))
            cennik_lista[produkt] = nowa_cena
            print(f"Ustawiono cenę {nowa_cena} zł dla produktu {produkt}.")
        except ValueError:
            print("Nieprawidłowa wartość!")
    elif wybor == 'U':
        delete = input("Podaj nazwę produktu do usunięcia: ").lower()
        if delete in cennik_lista:
            del cennik_lista[delete]
            print(f"Produkt {delete} został usunięty z cennika.")
        else:
            print("Taki produkt nie istnieje w cenniku!")
    elif wybor == 'D':
        produkt = input("Podaj nazwę produktu: ").lower()
        if produkt in cennik_lista:
            try:
                ilosc = int(input(f"Podaj liczbę sztuk dla produktu {produkt}: "))
                magazyn_lista[produkt] += ilosc
                print(f"Dodano {ilosc} sztuk produktu {produkt}.")
            except ValueError:
                print("Nieprawidłowa wartość!")
        else:
            print("Nie ma takiego produktu w cenniku!")
    elif wybor == 'R':
        nazwa_pliku = input("Podaj nazwę pliku: ")
        try:
            cennik_lista, magazyn_lista = odczytaj_z_pliku(nazwa_pliku)
            print("Dane zostały wczytane pomyślnie.")
        except FileNotFoundError:
            print("Plik nie istnieje!")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")
    elif wybor == 'W':
        nazwa_pliku = input("Podaj nazwę pliku: ")
        zapisz_do_pliku(nazwa_pliku, cennik_lista, magazyn_lista)
        print("Dane zostały zapisane pomyślnie.")
if lista_zakupow:
    print("\nLista zakupów:")
    for i, (produkt, cena) in enumerate(lista_zakupow.items()):
        print(f"{produkt:<20}{cena:>10.2f} zł")

print("-" * 10)
print(f"Suma to: {suma:>22.2f} zł")

#1903 - 05122023
#1855 - 07122023
#1941 - 10122023
