from random import randint
import uuid
x = randint(99,100)
y = randint(99,100)
# z = uuid.uuid4()

print(f"Wylosowane liczby: x = {x}, y = {y}")

#podstawowa postac ifa, dwie galezie if oraz else
#python wykona jedna albo druga czesc, w zaleznosci od prawdziwosci warunku

if x >= 50:
    print("X jest rowny conajmniej 50")
    print("X jest w drugiej polowie")
else:
    print("X jest w pierwszej polowie")

print("a to jest poza tematem")

#sam if bez else
#jesli prawda - instrukcje sie wykonaja, jezeli nie prawda - instrukcje sie nie wykonuja, ale program dziala dalej

if x % 2 == 0:
    print(f"{x} jest liczba parzysta")

print ("\n"+"***** ***"*1+"\n")

#if, elif, else
#Python po kolei bedzie sprawdzal warunki i wykona te czesc programu, ktora jest pierwszym prawdziwym warunkiem

if x>y:
    print(f"x jest wiekszy od y, bo {x} > {y}")
elif x<y:
    print(f"x jest mniejszy od y, bo {x} > {y}")
else:
    print(f"x jest rowny y, bo {x} = {y}")
