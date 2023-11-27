"""

Program losuje liczbę z zakresu od 0 do 999.
Użytkownik ma zgadnąć tę liczbę nie widząc jej.
Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała.
Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.
Nawiasem mówiąc technika wyszukiwania oparta o „podpowiedzi” za dużo/za mało nazywa się bisekcją i pełni w informatyce bardzo ważną rolę.
Umiejętnie ją stosując powinno się te zagadki rozwiązywać w 9-10 próbach (bo 210=1024).

"""
from random import randint

x = randint (1, 10)
krok = 0
while True:
    gg = int (input ("Podaj liczbe wariacie: "))
    krok = krok+1
    if gg == x:
        print(f"Brawo, udalo Ci sie za {krok} razem!")
        break
    elif gg > x:
        print("Podpowiem Ci: Za dużo\nSprobuj ponownie!\n\n"+"."*50+"\n")
    else:
        print("Podpowiem Ci: Za mało\nSprobuj ponownie!\n\n"+"."*50+"\n")
