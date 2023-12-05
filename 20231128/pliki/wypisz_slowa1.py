# jednym ze sposobów dzielenia lini na pojedyncze slowa jest uzycie split:


nr = 0
with open('pan_tadeusz.txt', mode='r', encoding='utf-8') as wejscie:
    for linia in wejscie:
        for slowo in linia.split():
            nr += 1
            print(slowo)
