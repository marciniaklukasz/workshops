limit = int(input("Podaj limit: "))

szer1 = len(str((limit+5)))
szer2 = len(str((limit+5)**2))
szer3 = len(str((limit+5)**3))

for i in range (1,limit+1):
    print(f"liczba {i:{szer1}}{i**2:{szer2}}{i**3:{szer3}}")

print (szer1, szer2, szer3)



liczba = 100

liczba += 50
print(liczba)