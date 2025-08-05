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
print(imiona)# ['Jan', 'Piotr', 'Anna', 'Nadia', 'Jan', 'Tomek', 'Maria', 'Anna', 'Jan']
print(imiona[0]) # Jan

# slicowanie
print(imiona[2:4]) # ['Anna', 'Nadia'] indeksy 2,3
print(imiona[1:]) # ['Piotr', 'Anna', 'Nadia', 'Jan', 'Tomek', 'Maria', 'Anna', 'Jan'] z ostatnim wlcznie
print(imiona[:5]) # ['Jan', 'Piotr', 'Anna', 'Nadia', 'Jan'] indeksy 0,1,2,3,4

print(imiona[-1]) # ostatni element
print(imiona[-2]) # przedostatni
print(imiona[-2:0]) # [] -> [7:0]
print(imiona[0:-2]) # -> [0:7], ['Jan', 'Piotr', 'Anna', 'Nadia', 'Jan', 'Tomek', 'Maria']

imionaparzyste = imiona[::2] # krok co 2
print(imionaparzyste) # ['Jan', 'Anna', 'Jan', 'Maria', 'Jan']

imiona.append("Karol")
print(imiona)
# ['Jan', 'Piotr', 'Anna', 'Nadia', 'Jan', 'Tomek', 'Maria', 'Anna', 'Jan', 'Karol']
imiona.insert(3,"Leon")
# ['Jan', 'Piotr', 'Anna', 'Nadia', 'Jan', 'Tomek', 'Maria', 'Anna', 'Jan', 'Karol']
imiona.remove("Nadia")
print(imiona) # ['Jan', 'Piotr', 'Anna', 'Leon', 'Jan', 'Tomek', 'Maria', 'Anna', 'Jan', 'Karol']

del imiona[5]
print(imiona)
print(imiona.pop(5)) # zwroci usuniety element, Maria