print("Kontrola bagazowa, podaj mi wymiary bagazu :-)")
"""x = int(input("Podaj mi wymiary krotszego boku w centymetrach"))
y = int(input("Podaj mi wymiary dluzszego boku w centymetrach"))
z = int(input("Podaj mi wymiary glebokosci w centymetrach"))"""

linia = input("Podaj trzy liczby wymiaru bagazu:\n")
x, y, z = (float(x) for x in linia.split())

v = x * y * z

print(f"Twoja objetosc walizki wynosi {v}. \n Wynik kontroli:")

if v <= 50000 and x < 50 and y < 50 and z < 50:
    print("Wsiadaj na samolot")
elif x > 50 or y > 50 or z > 50:
    print("Jeden wymiar jest ponad skale")
elif v >= 50000:
    print("Za duza walizka Wariacie :-)")
else:
    print("Blad")

bledy = []
if x > 50:
    bledy.append('Zbyt duza dlugosc')
if y > 50:
    bledy.append('Zbyt duza szerokosc')
if z > 50:
    bledy.append('Zbyt duza wysokosc')

if bledy:
    print("bagaz zostal odrzucony z takich problemow:")
    for blad in bledy:
        print(f' * {blad}')
else:
    print("spoko")