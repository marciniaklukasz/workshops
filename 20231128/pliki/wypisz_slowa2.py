# Regex jako split
import re
word = input("Podaj jakie slowo: ")
pattern = re.compile(r'\w+')
#znaczenie wzorca: nie pusty ciag znakow typu: "w", co obejmuje litery, cyfry i znaki

nr = 0
with open('pan_tadeusz.txt', mode='r', encoding='utf-8') as plik:
    for linia in plik:
        for slowo in re.findall(pattern,linia):
            if slowo == word:
                nr += 1
print("Wystepuje:",nr)
