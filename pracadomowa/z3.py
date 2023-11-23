"""
Napisz program, który wczytuje liczbę całkowitą,
a następnie na konsolę wypisuje w tylu liniach „choinkę” ze znaków * .
Np. dla parametru 3 powinno się wypisać:
*
***
*****
"""

ile = int(input("Ile rzedow: "))

for i in range(ile):
    gwiazdki = '*' * (i + 1)
    print(gwiazdki.center(ile+50))




