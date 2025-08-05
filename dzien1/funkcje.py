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

# podpowiedz typów
def mnozenie2(a: int, b: int) -> (int, int, int):
    return a, b, a * b  # zwraca krotke, tuple


# _ * _ = _
c = mnozenie2(8, 9)
print(f"{c[0]} * {c[1]} = {c[2]}")  # 8 * 9 = 72

wynik = mnozenie2(7, 9)
print(wynik)  # (7, 9, 63)
# rozpakowanie krotki
a, b, wynik = mnozenie2(7, 9)
print(f"{a} * {b} = {wynik}") # 7 * 9 = 63

# ctrl alt l formatowanie wg PEP8
print(mnozenie2("radek", 10))
# ('radek', 10, 'radekradekradekradekradekradekradekradekradekradek')
# pip install mypy zainstalowanie skryptu mypy
#  cd .\dzien1\ przejscie do katalogu dzien1
#  mypy .\funkcje.py uruchomienie mypy na naszym pliku
# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPythonSrednio5-08-2025\dzien1> mypy .\funkcje.py
# funkcje.py:38: error: Syntax error in type annotation  [syntax]
# funkcje.py:38: note: Suggestion: Use Tuple[T1, ..., Tn] instead of (T1, ..., Tn)
# funkcje.py:52: error: Argument 1 to "mnozenie2" has incompatible type "str"; expected "int"  [arg-type]
# Found 2 errors in 1 file (checked 1 source file)