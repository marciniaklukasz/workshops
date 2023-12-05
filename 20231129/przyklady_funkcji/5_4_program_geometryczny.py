import geometria


"""bok1 = float(input ('podaj pierwszy bok prostokąta: '))
bok2 = float(input ('podaj drugi bok prostokąta: '))

pole = geometria.pole_prostokata(bok1,bok2)
obwod = geometria.obwod_prostokata(bok1,bok2)

print('pole: ',pole, 'obwod: ', obwod)"""

from geometria import *

tekst_menu = input('Wybierz rodzaj figury:\n* K - kwadrat\n* P - prostokąt\n* O - koło\n* T - trojkat\n* Q - wyjście z programu')

# TODO dodaj obsługę koła do definicji funkcji
# TODO do programu oraz definicji funkcji dodaj obsługę trójkąta (w oparciu o 3 boki, jak w zadaniu domowym)

while True:
    print(tekst_menu)
    wybor = input('Twój wybór: ').upper()
    try:
        if wybor == 'Q':
            break
        elif wybor == 'K':
            a = float(input('Podaj długość boku: '))
            pole = pole_kwadratu(a)
            obw = obwod_kwadratu(a)
            print(f'Kwadrat o boku {a} ma pole {pole} oraz obwód {obw}')
        elif wybor == 'P':
            a = float(input('Podaj długość pierwszego boku: '))
            b = float(input('Podaj długość drugiego boku: '))
            pole = pole_prostokata(a, b)
            obw = obwod_prostokata(a, b)
            print(f'Prostokąt o bokach {a} i {b} ma pole {pole} oraz obwód {obw}')
        elif wybor == 'O':
            r = float(input('Podaj promień: '))
            pole = pole_kola(r)
            obw = obwod_kola(r)
            print(f'Koło o promieniu {r} ma pole {pole} oraz obwód {obw}')
        elif wybor == 'T':
            boka = float(input("Podaj bok A: "))
            bokb = float(input("Podaj bok B: "))
            bokc = float(input("Podaj bok C: "))
            pole = pole_trojkata(boka,bokb,bokc)
            p = obw_trojkata(boka,bokb,bokc)
            print(f'Pole trojkata to: {round(pole,5)}.\nObwod to: {p}')
        print('Niepoprawny wybór')
    except Exception as e:
        print('Wystapil jakis blad',e)

print('Do widzenia')
