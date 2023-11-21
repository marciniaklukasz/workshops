MiastoA = input("Z jakiego miasta chcesz zaczac podroz? ")
MiastoB = input("Do jakiego miasta jedziesz? ")
Dystans = int(input("Orientacyjny dystans miedzy tymi miastami? "))
Cena = float(input("Po ile teraz jest paliwo? "))
Spalanie = float(input("Ostatnie pytanie - ile pali Twoj samochod? "))

koszt = float(((Dystans*Spalanie)/100)*Cena)
#print("Ok, chcesz kupic ", produkt, ". Jedna sztuka kosztuje ", cena, "zl. Chcesza kupic ", liczba, " sztuk. Zaplacisz", cena*liczba, "zlotych!")
#print(f"Ok, chcesz kupic {produkt}. Jedna sztuka kosztuje {cena} zl. Chcesz kupic {liczba} sztuk. Zaplacisz {koszt:.2f} zlotych!")
print(f"Ok, chcesz wyjechac z miasta {MiastoA}, jedziesz do miasta {MiastoB}. Dystans to {Dystans}. "
      f"Twoj samochod pali {Spalanie} na 100 km, paliwo jest w cenie {Cena}, wiec podroz wyniesie Cie {koszt:.2f} ")