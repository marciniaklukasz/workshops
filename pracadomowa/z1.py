"""1.
Zadania po 1 tygodniu
Rozwiązania przysyłajcie na p.czarnik@alx.pl
Zadanie 1.1
Naprawa butów / dni tygodnia
Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (numer od 1 do 7).
Ma też podać, ile dni będzie trwała naprawa.
Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
Postaraj się obsłużyć także sytuacje, że naprawa trwa dłużej niż 7 dni.
W podstawowej wersji możesz wypisywać dzień odbioru też jako numer,
ale docelowo zrób wersję, w której program wypisuje dzień odbioru słownie."""
import datetime

oddane = int(input("W jaki dzień tygodnia oddajesz buty? Podaj numer dnia tygodnia od 1 do 7: "))
dlugosc = int(input("Ile dni będzie trwała naprawa, licząc od dnia kolejnego: "))

tydzien = ["poniedziałek","wtorek", "środe", "czwartek", "piątek", "sobote", "niedziele"]
oddany_slownie = tydzien[oddane-1]
doodbioru = oddane+dlugosc
nowy = doodbioru-7
if dlugosc > 7:
    print(f"Oddajesz buty w {tydzien[oddane-1]}, zapraszam w {tydzien[nowy-1]}.")
else:
    print(f"Oddajesz buty w {tydzien[oddane-1]}, zapraszam w {tydzien[nowy-1]}.")