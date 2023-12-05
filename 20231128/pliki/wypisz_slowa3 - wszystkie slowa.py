import re
pattern = re.compile(r'\w+')
unikalne = {}

with open('pan_tadeusz.txt', mode='r', encoding='utf-8') as plik:
    for linia in plik:
        for x in re.findall(pattern,linia):
            x = x.lower()
            if x in unikalne:
                unikalne[x] += 1
            else:
                unikalne[x] = 1

for x, ile in sorted(unikalne.items()):
    print(f"{x}: {ile}")

