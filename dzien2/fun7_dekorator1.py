# dekorator - funkcja , która przyjmuje inną funkcję jako argument
# dodaje, modyfikuje działanie tej funkcji
# wykorzystuje mechanizm funkcji wewnętrznej
def dekor(func):
    def wew():
        print("Dekorator. Dodatkowy napis")
        return func()  # zwracamy wynik funkcji

    return wew

@dekor
def nasza_funkcja():
    print("Funkcja, którą chcemy udekorować")


nasza_funkcja()  # Funkcja, którą chcemy udekorować
# po użyciu dekoratora @dekor
# Dekorator. Dodatkowy napis
# Funkcja, którą chcemy udekorować