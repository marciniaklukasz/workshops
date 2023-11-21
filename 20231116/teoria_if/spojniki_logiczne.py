from random import randint

x = randint(1,100)
y = randint(1,100)
print(f"Wylosowane liczby: x {x}, y={y}")

#and, logiczna koniunkcja, jest prawda gdy oba warunki sa prawdziwe

if x > 50 and y > 50:
    print("Obie liczby sa >50")
else:
    print("Co najmniej jedna z liczb nie jest wieksza od 50")

#or, logiczna alternatywa, jest prawda gdy conajmniej jeden warunek jest prawdziwy

if x > 50 or y > 50:
    print("or jest prawda")
    print("Conajmniej jedna z licz jest > 50")
else:
    print("or jest nieprawda")
    print("zadna liczba nie jest > 50")

#Sprawdzanie, czy liczba znajduje sie w okreslonym pzedziale, mozna zapisac w Pythonie
#Czy X nalezy od przedzialu 30 wlacznie do 60 wylaczajac

if x >=30 and x<60:
    print("AAA prawda")
else:
    print("AAA falsz")

#Porownianie obustronne, rzecz dostepna w pythonie, a niedostepna w wielu innych jezykach
#Mozna rozciagac: np if 10 < x < y <50
if x <=30 and x<60:
    print("BBB prawda")
else:
    print("BBB falsz")


#Tylko dla liczb calkowitych, czesto spotykany zapis (bo ladnie wyglada), ale jest odrobinke mniej wydajny od sposobu 2

if x in range (30,60):
    print("CCC - prawda")
else:
    print("CCC- falsz")