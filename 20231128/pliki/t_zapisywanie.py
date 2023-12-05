#aby uzyskac dostep do pliku, nalezy zaczac od wywolania fuknkcji open
from datetime import datetime

#np

plik = open('nowy_plik.txt', mode='w', encoding='utf-8')

#Dwa sposoby zapisywania tekstu do pliku:
# 1.) Metody wywolywane na obiekcie pliku:
# nie dopisuja znaku nowej lini
plik.write('Ala ma kota')
plik.write('i psa\n')
lista = ['Ala ma kota\n','sadasdadas', 'dasdsadasdas\n']
plik.writelines(lista)

#funkcja print z parametrem file
print('Biezacy czas:', datetime.now(), file=plik)
print('Gdansk', 'Zgierz', 'Ozorkow', sep=';', file=plik)

#Gdy konczymy korzystac z pliku, musimy go zamknac
plik.close()


#Najbardziej zalecany sposob zamykania plikow, to jest otwieranie ich w konstrukcji with
#Z otwartego pliku mozna korzystac wewnatrz bloku with
#a w momencie gdy z niego wychodzimy, python automayycznie zamknie otwarty plik

Tryby:
r - odczyt
w - plik zostanie utworzony, jezeli istnial - nadpisany
x -

with open('nowy_plik.txt', mode='w', encoding='utf-8') as plik2:
    print('To jest dopisane juz wewnatrz with.', file=plik2)
    print('To jest naprawde koniec', file=plik2)

print('Gotowe')