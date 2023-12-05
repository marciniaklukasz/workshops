import re
from collections import defaultdict

pattern = re.compile(r'\w+')
slownik = defaultdict(int)

with open('pan_tadeusz.txt', mode='r', encoding='utf-8') as plik:
    for linia in plik:
        for slowo in re.findall(pattern,linia):
            slownik[slowo.lower()] += 1


print("Najdluzsze slowo: ",max(len(slowo) for slowo in slownik.keys()))

for slowo, ile in sorted(slownik.items(), key=lambda item: item [1], reverse=True):
    print(f'{slowo:>20} -> {ile:4}')