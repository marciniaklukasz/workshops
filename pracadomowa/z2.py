"""
Napisz program, który odczytuje trzy liczby, sprawdza czy liczby
te mogą stanowić boki trójkąta (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?),
a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
Wzór Herona:√p(p−a)(p−b)(p−c), gdzie p jest połową obwodu: (a+b+c)/2.
Pierwiastek kwadratowy to funkcja sqrt z modułu math, można też podnieść do potęgi 0.5.
"""
import math

boka = float(input ("Podaj bok trójkata A: "))
bokb = float(input ("Podaj bok trójkata B: "))
bokc = float(input ("Podaj bok trójkata C: "))

"""Warunek istnienia trójkąta, nazywany również nierównością trójkąta, mówi, 
że suma długości dowolnych dwóch boków trójkąta musi być większa niż długość trzeciego boku.
"""
if boka + bokb > bokc and bokb + bokc > boka and boka + bokc > bokb:
    p = int((boka + bokb + bokc))
    p2 = int((boka + bokb + bokc)/2)
    pole = math.sqrt(p2 * (p2 - boka) * (p2 - bokb) * (p2 - bokc))
    print(f"Mozesz stworzyc trojkat o bokach {boka},{bokb},{bokc}. Obwod wynosi {p}. Pole powierzchni wynosi: {round(pole,5)}")
else:
    print("Nie mozesz stworzyc trojkatu")