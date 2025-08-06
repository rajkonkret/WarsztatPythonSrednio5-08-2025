# Zadanie 1
#
# Zbuduj plik wycieczka.py:
# Napisz funkcję kwota, w której policzysz kwotę do zapłaty za wycieczkę,
# która opiera się na rozliczeniu wartości takich jak cena za transport,
# nocleg i wyżywienie, wycieczki, ubezpieczenie i inne koszty, gdzie rabatowane są tylko dwie pierwsze wartości.
#
# Użyj funkcji do policzenia rabatu.
#
# Następnie zbuduj listę z różnymi wartościami rabatu
# i iteracyjnie wyznacz wartości do zapłaty dla stałych kosztów z zmiennego rabatu.
def oblicz_rabat(transport, nocleg, rabat_procent):
    return (transport + nocleg) * rabat_procent


def kwota(transport, nocleg, wyzywienie, wycieczki, ubezpieczenie, inne, rabat=0.0):
    rabat_kwota = oblicz_rabat(transport, nocleg, rabat)
    koszt_rabatowany = (transport + nocleg) - rabat_kwota
    koszt_pelny = wyzywienie + wycieczki + ubezpieczenie + inne
    suma = koszt_pelny + koszt_rabatowany
    return round(suma, 2)


# shift tab - cofnięcie tabulatora
# funkcje_zad_praca_wlasna - gdy z importu
# __main__ - gdy uruchammiamy z tego pliku
print(__name__)
if __name__ == '__main__':
    rabaty = [0.0, 0.05, 0.10, 0.15, 0.20]

    print("Rabat (%) -> Kwota do zapłaty (zł)")
    print("-" * 35)
    for r in rabaty:
        kw = kwota(
            transport=500,
            nocleg=800,
            wyzywienie=400,
            wycieczki=300,
            ubezpieczenie=100,
            inne=50,
            rabat=r
        )
        print(f"{int(r * 100):>3}%      ->      {kw:.2f} zł")
# >3 - wyrównaj do prawej, długośc tekstu 3 znaki
# .2f dwa miejsca po przecinku przy wyświetlaniu
# Rabat (%) -> Kwota do zapłąty (zł)
# -----------------------------------
#   0%      ->      2150.00 zł
#   5%      ->      2085.00 zł
#  10%      ->      2020.00 zł
#  15%      ->      1955.00 zł
#  20%      ->      1890.00 zł
