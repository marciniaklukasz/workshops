pierwsze_imie = input("Jak masz na imie? ")
wiek = int(input("Ile masz lat? "))
if wiek < 18:
    print("Och Ty Malolacie!")
elif wiek <65:
    print("Nie potrzebujesz dowodu")
else:
    print ("Emeritto")