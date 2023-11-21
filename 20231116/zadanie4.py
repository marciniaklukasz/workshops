cena = int(input("Koszt godziny parkowania (zlotowki): "))
czas = int(input("Na ile parkujesz (godziny): "))
koszt = cena * czas

saldo = 0
print(f"koszt: {koszt} zl")
print(f"Twoje saldo: {saldo} zl")
wplaty = []
check = sum(wplaty)

while check < koszt:
    wplacone = int(input("Wrzuc monete: "))
    add = wplaty.append(wplacone)
    check = sum(wplaty)
    print(f"Wplaciles: {check} zlotych")
print(f"Dziekujemy za zaplate: {wplaty} zl")
reszta = check-koszt
if reszta > 0:
    print("Reszta:",reszta, "zl")
    print("Dziekujemy za skorzystanie!")
else:
    print("Dziekujemy za skorzystanie!")