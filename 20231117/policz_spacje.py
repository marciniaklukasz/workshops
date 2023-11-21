'''napis = input('Napisz cos:\n')
a = 0
for znak in napis:
    if znak == ' ':
        a=a+1
print(f"Liczba spacji:{a}")'''


napis = input('Napisz cos:\n')
a = 0
for znak in napis:
    if znak in ('a','e','i','o','u','y'):
        a=a+1
print(f"Liczba samoglosek lacznie:{a}")
