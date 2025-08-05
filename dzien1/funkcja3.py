# przykład2 - funkcja wyższego rzędu

def witaj(imie):
    return f"Miło cię widzieć {imie}"


def konkurs(imie, miejsce, punkty):
    return f"Uczestnik konkursu: {imie}, miejsce: {miejsce}, liczba punktów: {punkty}"


def bonus(punkty):
    if punkty > 50:
        bn = punkty + 10
    else:
        bn = punkty
    return f"liczba punktów z bonusem: {bn}"


def osoba(funkcja, *args):
    return funkcja(*args)


def multiosoba(*args):
    print(bonus(args[2]))
    konkurs(*args)
    return "opublikowano wyniki konkursu"


print(osoba(witaj, "Leon"))  # {'a': 10, 'b': 90, 'name': 'Radek'}
print(osoba(konkurs, "Leon", 'Kraków', 56))  # {'a': 10, 'b': 90, 'name': 'Radek'}
print(multiosoba("Anna", 19, 88))
print(multiosoba("Anna", "Toruń", 88))


def fun_args(*args):  # przyjmij dowolną liczbę argumentów pozycyjnych
    print(args)  # (1, 2, 3)


fun_args(1, 2, 3)
fun_args(1, 2, 3, 5, 6, 7, 8, 9, 9)  # (1, 2, 3, 5, 6, 7, 8, 9, 9)


def fun_kwargs(**kwargs):  # dowolna liczba argumentów nazwanych
    print(kwargs)


fun_kwargs(a=10, b=90, name="Radek")  # {'a': 10, 'b': 90, 'name': 'Radek'}
