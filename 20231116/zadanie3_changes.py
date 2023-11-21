'''Napisz program, który na podstawie dwóch podanych liczb obliczy
wynik zadanej operacji (dodawanie, odejmowanie, mnożenie,
dzielenie). W przypadku podania nieprawidłowej operacji program
ma wyświetlić odpowiedni komunikat o błędzie.
Przykładowy komunikat programu:
Podaj pierwszą liczbę: 10
Podaj drugą liczbę: 5
Podaj rodzaj operacji: +2+
Wynik: 15
'''
while True:
    x = input("Podaj rodzaj operacji (+, -, *, /: ) lub znak ! by zakończyć: ")
    if x == '!':
        break
    a = int(input("Podaj pierwsza liczbę: "))
    b = int(input("Podaj drugą liczbę: "))



    if x == "+":
        results = a + b
    elif x == "-":
        results = a-b
    elif x == "*":
        results = a*b
    elif x == "/":
        if a != 0 and b != 0 :
            results = a/b
        else:
            print("Nie dzielimy przez zero!")

    else:
        print("Wybierz cos z listy wyboru, a nie cos innego")
    print(f"Wynik to: {results}")

print("***** ***")