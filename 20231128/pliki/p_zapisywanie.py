limit = int(input("Podaj limit: "))

with open('nowy_plik2.txt', mode='w', encoding='utf-8') as plik2:
    for i in range (1, limit+1):
        print ('To jest liczba:', i , file=plik2)
