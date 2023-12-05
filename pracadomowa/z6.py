"""
Napisz grę tekstową polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o rozmiarach 10 na 10.
Program na początku losuje pozycję skarbu oraz pozycję gracza.
Następnie użytkownik może wprowadzać komendy zmieniające położenie postaci o jedną pozycję w górę/dół/lewo/prawo (np zgodnie z konwencją WSAD) –
normalnie za pomocą input.
Gdy gracz wejdzie na pole, na którym kryje się skarb – wygrywa.
Gdy wyjdzie poza planszę – przegrywa.
Po każdym ruchu użytkownik powinien otrzymywać informację o tym, czy zmierza w dobrym kierunku.
Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez użytkownika na dojście do celu.
"""
a=5
b=10
szerokosc = 2
for i in range(10):
    print(i+10, 5)