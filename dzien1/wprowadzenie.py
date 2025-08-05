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

noweimie = imiona # referencja, kopia adersu listy
qimie = list(imiona) # nowe listy, nowy adres
pimie = imiona[:]
lista_copy = imiona.copy() # nowa lista, kopia elementów listy

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