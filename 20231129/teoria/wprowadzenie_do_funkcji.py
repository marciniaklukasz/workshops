print("Pierwsza linia programu")


def aaa():
    print("Pierwsza linijka aaa")
    print("Druga linijka aaa")
    print("Trzecia linijka aaa")
    print("Czwarta linijka aaa")
    print("Piata linijka aaa")


print("Funkcja BBB zostala zdefiniowana")
print("Teraz wywolam funkcje aaa:\n\n\n\n")
aaa()

#parametry

def bbb(ile_razy):
    print("Poczatek funckji bbb, parametr ma wartosc",ile_razy)
    for i in range(ile_razy):
        aaa()
    print("To jest koniec funkcji bbb")
print("Teraz bbb wywolam")
bbb(3)

print("\n\n\n\n\nOstatnia linia programu")