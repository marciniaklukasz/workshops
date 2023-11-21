napis = 'Ala ma kota'
print(napis)
print(len(napis))

for znak in napis:
	print('Kolejny znak:', znak)
print()

print('Typ napisu:', type(napis))
print('Typ znaku:', type(napis[4]))

print('znak:', napis[4])
# numeracja od 0
print('fragment:', napis[4:6])
# zakres lewostronnie domknięty

# Zawartości napisu nie da się zmienić, to nie są tablice takie jak w C. str is immutable
# napis[7] = 'K'
print()

if 'm' in napis:
	print('Jest literka m')
else:
	print('Nie ma literki m')

# Dla napisów operator in sprawdza czy napis jest fragmentem dużego napisu (a nie tylko czy litera jest elementem)
if 'kot' in napis:
	print('kot obecny')
else:
	print('nie ma kota')

print('kot jest na pozycji', napis.index('kot'))
print('kot jest na pozycji', napis.find('kot'))
# Gdy nie znajdą: index wyrzuca wyjątek, a find zwraca -1
#ERR print('pies jest na pozycji', napis.index('pies'))
print('pies jest na pozycji', napis.find('pies'))
print()

# Napisy można dodawać - wynikiem jest nowy napis
nowy = napis + ' oraz psa'
print('nowy napis:', nowy)
print('stary napis:', napis)

# Napisy można mnożyć przez liczbę całkowitą - oznacza powtózenie treści
print('Ala ma kota. ' * 10)
print()

napis = 'Ala ma kota, a Ola ma psa. Pomagamy zwierzakom.'
print(napis)

print(napis.replace('ma', 'posiada'))

napis = '   Ala ma kota, a Ola ma psa.  '
print(napis.replace(' ', '_'))
print()

print('upper:', napis.upper())
print('lower:', napis.lower())
print('trip:', napis.strip())
print('capitalize:', 'abcd efg opr'.capitalize())
print('title:     ', 'abcd efg opr'.title())
print()
print(napis.split())
print(napis.split(','))

lista = ['Ala', 'Ola', 'Ela']
napis = ';'.join(lista)
print(napis)
print('Witamy osoby ' + ' oraz '.join(lista) + ".")
print()

litera = 'A'
cyfra = '0'
napis1 = 'AbcDĘ'
napis2 = 'Abc ,!@#$ '
napis3 = '   '

# gdy napis zawiera wyłącznie litery (ale także innych alfabetów), to isalpha zwraca True
# gdy jest pusty lub zawiera chociaż jeden znak nibędący literą, to zwraca False
print(litera.isalpha())
print(cyfra.isalpha())
print(napis1.isalpha())
print(napis2.isalpha())
print(napis3.isalpha())
print(napis3.isspace())
# są też inne metody .is_____
