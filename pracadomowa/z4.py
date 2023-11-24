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

koszt_gipsowania = 0
koszt_malowania = 0
koszt_listwy = 0
koszt_paneli = 0

g = input("Czy gipsujemy ściany oraz sufit? (t/n)")
if g in ["y", "t"]:
    koszt_gipsowania = ppows * 100
m = input("Czy malujemy ściany oraz sufit? (t/n)")
if m in ["y", "t"]:
    koszt_malowania = ppows * 30
p = input("Czy kładziemy panele? (t/n)")
if p in ["y", "t"]:
    koszt_paneli = ppow * 50
l = input("Czy kładziemy listwy? (t/n)")
if l in ["y", "t"]:
    koszt_listwy = obw * 40

suma = koszt_paneli+koszt_listwy+koszt_gipsowania+koszt_malowania


if g in ["y", "t"] and m in ["y", "t"] and p in ["y", "t"] and l in ["y", "t"]:
    suma_po_rabacie = float(suma*.99)
    rabat = float(suma*.01)
    print(f"\nZa kompleksowa usługę dostajesz rabat! Caly 1%! (Taki black friday!)\n")
    print(f"Podsumowanie:\n"
      f"Koszt gipsowania: {koszt_gipsowania} zł\n"
      f"Koszt malowania: {koszt_malowania} zł\n"
      f"Koszt paneli: {koszt_paneli} zł\n"
      f"Koszt gipsowania: {koszt_listwy} zł\n\n"
      f"------------------------------------\n\n"
      f"Razem: {suma:.2f} zł\n"
      f"Rabat: {rabat:.2f} zł\n"
      f"Razem po rabacie: {suma_po_rabacie:.2f} zł")
else:
    print(f"\nPodsumowanie:\n"
          f"Koszt gipsowania: {koszt_gipsowania} zł\n"
          f"Koszt malowania: {koszt_malowania} zł\n"
          f"Koszt paneli: {koszt_paneli} zł\n"
          f"Koszt gipsowania: {koszt_listwy} zł\n\n"
          f"------------------------------------\n\n"
          f"Razem: {suma:.2f} zł\n")