ile_godzin = int (input ("Podaj liczbe godzin parkowania: "))
do_zaplaty = 3 * ile_godzin
print ('Do zaplaty:', do_zaplaty)

suma_wplat = 0
while suma_wplat < do_zaplaty:
    print (f"Do tej pory wplacono {suma_wplat}, pozostalo jeszcze {do_zaplaty - suma_wplat}")
    moneta = int (input ("wrzuc monete: "))
    suma_wplat += moneta
if suma_wplat > do_zaplaty:
    print (f"Wydaje reszte: {suma_wplat - do_zaplaty}")

print ("***** ***")
