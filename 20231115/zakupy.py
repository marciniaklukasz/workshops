produkt = input("Co chcesz kupic? ")
cena = float(input(f"Ile kosztuje jedna sztuka {produkt}? "))
liczba = int(input("Ile sztuk chcesz kupic?"))

koszt = cena*liczba
#print("Ok, chcesz kupic ", produkt, ". Jedna sztuka kosztuje ", cena, "zl. Chcesza kupic ", liczba, " sztuk. Zaplacisz", cena*liczba, "zlotych!")
print(f"Ok, chcesz kupic {produkt}. Jedna sztuka kosztuje {cena} zl. Chcesz kupic {liczba} sztuk. Zaplacisz {koszt:.2f} zlotych!")