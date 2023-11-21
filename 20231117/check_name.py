"""
Napisz program zliczajacy liczbe znakow w podanym przez uzytkownika napisie pomiedzy nawiasami <>
Nawiasy moga wystapic tylko raz
"""

text = input('Napisz cos z nawiasem:\n')
a = 0
b = 0
while True:
    a = text.find("<", b)
    if a == -1:
        break
    b = text.find(">", a)
    if b == -1:
        break
    print('tekst z nawiasow:', text[a + 1:b])
    print('dlugosc w nawiasach:', len(text[a + 1:b]))

print('Koniec')
