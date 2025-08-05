# funkcje - fragment kodu, który można wykonac w dowolnym momencie
# funkcja musi najpierw zostac zadeklarowana
# wywołanie funkcji uruchamia kod

# deklaracja funkcji
# symulacja przeciążania funkcji rózną liczbą argumentów
def odejmij(a, b, c=0):  # c=0 parametr o wartości domyślnej
    print(a - b - c)


# argumenty pozycyjne
odejmij(4, 5)  # -1
odejmij(4, 5, 8)  # -9

# argumenty mieszane
odejmij(4, c=8, b=90)  # -94

# argumenty nazwane(keywords arguments)
odejmij(c=90, a=90, b=54)  # -54


# pozycyjne muszą być przed nazwanymi
# odejmij(a=90, 4, 5) # SyntaxError: positional argument follows keyword argument

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(odejmij(5, 6) + odejmij(6, 9, 0))

# funkcje zwracające wynik
def mnozenie(a, b):
    return a * b


print(mnozenie(6, 9))  # 54
zmienna = mnozenie(7, 43)
print("Zmienna:", zmienna)  # Zmienna: 301


def mnozenie2(a: int, b: int) -> (int, int, int):
    return a, b, a * b

# _ * _ = _
print()