print("Gipsowanie ścian: 100 zł za metr kwadratowy")
print("Malowanie ścian i sufitów: 30 zł za metr kwadratowy")
print("Położenie paneli podłogowych: 50 zł za metr kwadratowy")
print("Położenie listew przypodłogowych: 40 zł za metr bieżący")

wys = int(input("Podaj wysokość pomieszczenia (w metrach): "))
szer = int(input("Podaj szerokość pomieszczenia (w metrach): "))
dl = int(input("Podaj długość pomieszczenia (w metrach): "))

obw = (2 * szer) + (2 * dl)
ppow = szer * dl
ppows = ((2 * (szer * wys)) + (2 * (dl * wys))+ppow)
print(f"Pole powierzchni podłogi i sufitu wynosi po {ppow} m2. \n"
      f"Obwód wynosi {obw} metrów. \n"
      f"Pole powierzchni ściany 'A' wynosi {szer * wys} metrów, pole powierzchni ściany 'B' wynosi {dl * wys} metrów")

# Usługi
usa = input("Czy gipsujemy ściany? (t/n): ")
if usa in ["y", "t"]:
    koszt_gipsowania = ppows * 100
    print(f"Super, gipsujemy ściany, przy podanych parametrach cena za usługę: {koszt_gipsowania} zł.")
    usb = input("Czy malujemy ściany i sufit? (t/n): ")
    if usb in ["y", "t"]:
        koszt_malowania = ppows * 30
        print(f"Malujemy, więc do ceny doliczamy: {koszt_malowania} zł.")
        koszt_gipsowania_malowania = koszt_gipsowania + koszt_malowania
        usc = input("Czy kładziemy panele podłogowe? (t/n): ")
        if usc in ["y", "t"]:
            koszt_paneli = ppow * 50
            koszt_gipsowania_malowania_paneli = koszt_gipsowania_malowania + koszt_paneli
            usd = input("Czy kładziemy listwy przypodłogowe? (t/n): ")
            if usd in ["y", "t"]:
                koszt_listew = obw * 40
                koszt_koncowy = koszt_gipsowania_malowania_paneli + koszt_listew
                koszt_koncowy_znizka = koszt_koncowy * 0.9
                print(f"Super, za kompleksową usługę dostajesz 10% zniżki! \n"
                      f"Łącznie wyszło: \n"
                      f"    - Gipsowanie: {koszt_gipsowania} zł \n"
                      f"    - Malowanie: {koszt_malowania} zł \n"
                      f"    - Panele podłogowe: {koszt_paneli} zł \n"
                      f"    - Listwy przypodłogowe: {koszt_listew} zł \n"
                      f"Suma po zniżce: {koszt_koncowy_znizka:.2f} zł")
            else:
                print(f"Łączny koszt: {koszt_gipsowania_malowania_paneli} zł")
        else:
            print(f"Łączny koszt: {koszt_gipsowania_malowania} zł")
    else:
        print(f"Łączny koszt: {koszt_gipsowania} zł")
else:
    print("Nie wybrano żadnej usługi.")
