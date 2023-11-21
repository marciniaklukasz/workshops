from random import  randint

x = randint(1,10)
y = randint(1,10)

r = x*y
i = 1
a = int(input(f'Ile to jest {x} x {y}: '))
while a != r:
    print ("Sprobuj jeszcze raz :-)")
    a = int (input ("Jaki powinien byc wynik mnozenia? "))
    i +=1
    if a == r:
        print(f"Brawo, zgadles za {i} razem!")




