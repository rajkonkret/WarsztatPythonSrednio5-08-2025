import sys

print()
print("pierwsza linia")  # pierwsza linia
# komentarz
"""
Komentarz wielolinijkowy
dokumentacje
"""

# typowanie dynamiczne, typ wnoszony na podstawie zawartości
info = """
to teskt wielolinijowy
    zachowuje
formatowanie"""

print(info)
print(info)
print(info)
print(info)

# ctrl d - powielanie linii
# "to teskt wielolinijowy
#     zachowuje
# formatowanie"
print(type(info))  # <class 'str'>, tekstowy

info = 90
print(info)
print(type(info))  # <class 'int'>, liczba całkowita
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)

# kolekcje

# lista
imiona = ["Jan", "Piotr", "Anna", "Nadia", "Jan", "Tomek", "Maria", "Anna", "Jan"]
print(imiona)  # ['Jan', 'Piotr', 'Anna', 'Nadia', 'Jan', 'Tomek', 'Maria', 'Anna', 'Jan']
print(imiona[0])  # Jan

# slicowanie
print(imiona[2:4])  # ['Anna', 'Nadia'] indeksy 2,3
print(imiona[1:])  # ['Piotr', 'Anna', 'Nadia', 'Jan', 'Tomek', 'Maria', 'Anna', 'Jan'] z ostatnim wlcznie
print(imiona[:5])  # ['Jan', 'Piotr', 'Anna', 'Nadia', 'Jan'] indeksy 0,1,2,3,4

print(imiona[-1])  # ostatni element
print(imiona[-2])  # przedostatni
print(imiona[-2:0])  # [] -> [7:0]
print(imiona[0:-2])  # -> [0:7], ['Jan', 'Piotr', 'Anna', 'Nadia', 'Jan', 'Tomek', 'Maria']

imionaparzyste = imiona[::2]  # krok co 2
print(imionaparzyste)  # ['Jan', 'Anna', 'Jan', 'Maria', 'Jan']

imiona.append("Karol")
print(imiona)
# ['Jan', 'Piotr', 'Anna', 'Nadia', 'Jan', 'Tomek', 'Maria', 'Anna', 'Jan', 'Karol']
imiona.insert(3, "Leon")
# ['Jan', 'Piotr', 'Anna', 'Nadia', 'Jan', 'Tomek', 'Maria', 'Anna', 'Jan', 'Karol']
imiona.remove("Nadia")
print(imiona)  # ['Jan', 'Piotr', 'Anna', 'Leon', 'Jan', 'Tomek', 'Maria', 'Anna', 'Jan', 'Karol']

del imiona[5]
print(imiona)
print(imiona.pop(5))  # zwroci usuniety element, Maria

imen = enumerate(imiona, 111)  # numeruje kolekcje
for i in imen:
    print(i)
# (111, 'Jan') # tupla, krotka, niemutowalna lista
# (112, 'Piotr')
# (113, 'Anna')
# (114, 'Leon')
# (115, 'Jan')
# (116, 'Anna')
# (117, 'Jan')
# (118, 'Karol')
tup = 1, 2
print(type(tup))  # <class 'tuple'>
print(tup)  # (1, 2)
a, b = tup
print(a, b)  # 1 2

# ctrl / - komentarz fragmentu kodu
# f - stirng format
imen = enumerate(imiona, 111)
for index, wartosc in imen:
    print(f"index -> {index}, wartośc: {wartosc}")
# index -> 111, wartośc: Jan
# index -> 112, wartośc: Piotr
# index -> 113, wartośc: Anna
# index -> 114, wartośc: Leon
# index -> 115, wartośc: Jan
# index -> 116, wartośc: Anna
# index -> 117, wartośc: Jan
# index -> 118, wartośc: Karol
print("a: {}, b: {}".format(a, b))  # a: 1, b: 2
print("a:", a, "b:", b)  # a: 1 b: 2
#  sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
print("a: %i b: %i" % (a, b))  # a: 1 b: 2
# walidacja typów
# print("a: %i b: %i" % (a, "radek"))  # TypeError: %i format: a real number is required, not str

noweimie = imiona  # referencja, kopia adersu listy
qimie = list(imiona)  # nowe listy, nowy adres
pimie = imiona[:]
lista_copy = imiona.copy()  # nowa lista, kopia elementów listy

print(imiona)
print(noweimie)
print(pimie)
print(qimie)
print(lista_copy)
# ['Jan', 'Piotr', 'Anna', 'Leon', 'Jan', 'Anna', 'Jan', 'Karol']
# ['Jan', 'Piotr', 'Anna', 'Leon', 'Jan', 'Anna', 'Jan', 'Karol']
# ['Jan', 'Piotr', 'Anna', 'Leon', 'Jan', 'Anna', 'Jan', 'Karol']
# ['Jan', 'Piotr', 'Anna', 'Leon', 'Jan', 'Anna', 'Jan', 'Karol']

noweimie.append("Kunegunda")
print(imiona)  # ['Jan', 'Piotr', 'Anna', 'Leon', 'Jan', 'Anna', 'Jan', 'Karol', 'Kunegunda']
print(noweimie)  # ['Jan', 'Piotr', 'Anna', 'Leon', 'Jan', 'Anna', 'Jan', 'Karol', 'Kunegunda']
print(pimie)  # ['Jan', 'Piotr', 'Anna', 'Leon', 'Jan', 'Anna', 'Jan', 'Karol']
print(qimie)  # ['Jan', 'Piotr', 'Anna', 'Leon', 'Jan', 'Anna', 'Jan', 'Karol']
print(lista_copy)  # ['Jan', 'Piotr', 'Anna', 'Leon', 'Jan', 'Anna', 'Jan', 'Karol']

print(id(imiona))
print(id(noweimie))
print(id(pimie))
print(id(qimie))
print(id(lista_copy))
# 1394149663552
# 1394149663552
# 1394149470464
# 1394151816896
# 1394151754688

# krotka, tupla
miasto = ("Kraków", "Lublin", "Płock", "Łódź")
print(miasto)  # ('Kraków', 'Lublin', 'Płock', 'Łódź')
print(type(imiona))  # <class 'list'>
print(type(miasto))  # <class 'tuple'>

print(miasto.index("Łódź"))  # 3
print(miasto.count("Kraków"))  # występuje 1 raz

# del miasto[0] # TypeError: 'tuple' object doesn't support item deletion
del miasto  # kasowanie całej krotki jest możliwe

# zbior, set - nie przechowuje duplikatów
# zbior nie posiada indeksu
drzewa = {'jodła', "buk", "świerk", "dąb", "klon", "dąb"}
print(drzewa)  # {'jodła', 'klon', 'dąb', 'świerk', 'buk'}
print(type(drzewa))  # <class 'set'>

drzewa.add("osika")
print(drzewa)  # {'jodła', 'dąb', 'buk', 'klon', 'osika', 'świerk'}

lista = [1, 2, 3, 4, 4, 5, 5, 6, 1, 2, 3]
zbior = set(lista)
print(zbior)  # {1, 2, 3, 4, 5, 6} gubimy kolejność

pusty_zbior = set()
print(pusty_zbior)  # set(), pusty zbiór

# słownik - para typu klucz:wartość
osoba = {
    "id": 89,
    "imie": "Tadeusz",
    "rok urodzenia": 1976,
    "miasto": "Łódź"
}

print(osoba)
# {'id': 89, 'imie': 'Tadeusz', 'rok urodzenia': 1976, 'miasto': 'Łódź'}
print(type(osoba))  # <class 'dict'>
# print(osoba['miasto'])  # Łódź
# print(osoba['Miasto'])  # KeyError: 'Miasto'
print(osoba.get("miasto"))  # Łódź
print(osoba.get("Miasto"))  # None, nie rzuca wyjątkiem
print(osoba.get("Miasto", "default"))  # default gdy nie znajdzie klucza
osoba['imie'] = "Radek"
print(osoba)
# {'id': 89, 'imie': 'Radek', 'rok urodzenia': 1976, 'miasto': 'Łódź'}
print(osoba.keys())
print(osoba.values())
print(osoba.items())
# dict_keys(['id', 'imie', 'rok urodzenia', 'miasto'])
# dict_values([89, 'Radek', 1976, 'Łódź'])
# dict_items([('id', 89), ('imie', 'Radek'), ('rok urodzenia', 1976), ('miasto', 'Łódź')])

lista = [1, 2, 3, 4, 4, 5, 5, 6, 1, 2, 3]
print(dict.fromkeys(lista))  # nie zmienia kolejnosci
# {1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
print(list(dict.fromkeys(lista)))  # [1, 2, 3, 4, 5, 6]

pusty_slownik = {}
print(pusty_slownik)  # {}
pusty_slownik = dict()
print(pusty_slownik)  # {}

# pętla
licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat!")
    if licznik > 10:
        break

licznik = 0

while licznik < 10:
    licznik += 1
    print("Komunikat 2")

przekaski = ['hotdog', 'pizza', 'hamburger', 'frytki']
prompt = "wybierz swoją przekąskę"

# while True:
#     choice = input(prompt)  # odczytuje dane od użytkownika
#     if choice in przekaski:
#         break
#     print("Nie ma")

# walrus operator, operator morsa
# while (choice := input(prompt)) not in przekaski:
#     if choice == "exit":
#         break
#     print("Nie ma")

name = "Radek"
a = len(name)
if a > 4:
    print("Długość większa od 4, wynosi:", a)

if (a:= len(name)) > 4:
    print("Długość większa od 4, wynosi:", a)
# Długość większa od 4, wynosi: 5
# Długość większa od 4, wynosi: 5

odp = "Radek"
if odp == "radek": # porównanie
    print("Radek")
elif odp =="Tomek":
    print("tomek")
else:
    print("Nie znam Cię")
# Nie znam Cię

# od pythona 3.10 match case
odp = input("Podaj imię")
match odp.casefold().strip().capitalize():
    case "Radek":
        print("Ok")
    case 'Tomek':
        print("Też OK")
    case _: # odpowiednik else
        print("Nie znam")
# Podaj imięradek
# Nie znam
# Podaj imięradek
# Ok

name1 = "GROSS"
name2 = "groẞ"

print(name1.lower() == name2.lower()) # False
print(name1.upper() == name2.upper()) # False
print(name1.casefold() == name2.casefold()) # True