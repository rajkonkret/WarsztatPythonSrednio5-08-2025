# funkcja zagnieżdżona, wewnętrzna

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    # fun2()
    return fun2  # zwracamy adres funkcji, bez nawiasów


fun1()  # To jest fun1
new_fun = fun1()
print(type(new_fun))  # <class 'function'>
print(new_fun)  # <function fun1.<locals>.fun2 at 0x000001651D5D3BA0>
new_fun()  # urchomienie funkcji, To jest fun2


# zrobić funkcję plik
# funkcja przyjmuje parametr - zapis, odczyt
# w zależności od parametru zwróci funkcję do odczytu lub zapis pliku
# zmienne, nazwy, plików - snake_case
# klasy PascalCase, UpperCamelCase
def plik(arg):
    print("Sprawdzam czy plik istnieje...")

    def zapis():
        print("Zapisałem plik")

    def odczyt():
        print("Odczytałem plik")

    match arg.casefold():
        case "zapis":
            return zapis  # zwracamy adres funkcji

        case _:
            return odczyt

zapis_pliku = plik("zapis")
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()

odczyt_pliku = plik("odczyt")
odczyt_pliku()
odczyt_pliku()
odczyt_pliku()
odczyt_pliku()
# Sprawdzam czy plik istnieje...
# Zapisałem plik
# Zapisałem plik
# Zapisałem plik
# Zapisałem plik
# Zapisałem plik
# Zapisałem plik
# Sprawdzam czy plik istnieje...
# Odczytałem plik
# Odczytałem plik
# Odczytałem plik
# Odczytałem plik

zapis_pliku()
odczyt_pliku()
zapis_pliku()
# Zapisałem plik
# Odczytałem plik
# Zapisałem plik

# 'w'       open for writing, truncating the file first
fh = open("text.txt", "w")
fh.write("Zapisano\n")
fh.close()