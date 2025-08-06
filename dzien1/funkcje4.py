# lambda - skrócony zapis funkcji
# lambda - zwraca wynik
# funkcja anonimowa - możliwość użycia funkcji w miejscu deklaracji
from functools import reduce, lru_cache


def liczymy(x, y):
    return x * y


print(liczymy(6, 9))  # 54

liczymy2 = lambda x, y: x * y
print(liczymy2(5, 9))  # 45

# mapowanie danych
lista = [1, 2, 5, 56, 78, 90, 100, 200, 500]

# zrobic liste z tymi wartościami do potęgi 2

# list comprehensions
print([i ** 2 for i in lista])
# [1, 4, 25, 3136, 6084, 8100, 10000, 40000, 250000]

lista_wyn = []  # pusta lista
for i in lista:
    lista_wyn.append(i ** 2)
print(lista_wyn)  # [1, 4, 25, 3136, 6084, 8100, 10000, 40000, 250000]


def zmien(x):
    return x ** 2


lista_wyn2 = []
for i in lista:
    lista_wyn2.append(zmien(i))
print(lista_wyn2)  # [1, 4, 25, 3136, 6084, 8100, 10000, 40000, 250000]

# funkcje wyższego rzędu
# map() przyjmuje funkcje i kolekcje
print(f"Zastosowanie map() {list(map(zmien, lista))}")
# Zastosowanie map() [1, 4, 25, 3136, 6084, 8100, 10000, 40000, 250000]

# lambda jako funkcja anonimowa
# anonimowa - nie jest przypisana do żadnej nazwy(zmiennej)
print(f"Zastosowanie map() {list(map(lambda z: z ** 2, lista))}")
# Zastosowanie map() [1, 4, 25, 3136, 6084, 8100, 10000, 40000, 250000]
print(f"Zastosowanie map() {list(map(lambda z: z ** 3, lista))}")
# Zastosowanie map() [1, 8, 125, 175616, 474552, 729000, 1000000, 8000000, 125000000]
print(f"Zastosowanie map() {list(map(lambda z: z / 3, lista))}")
# Zastosowanie map() [0.3333333333333333, 0.6666666666666666, 1.6666666666666667, 18.666666666666668,
# 26.0, 30.0, 33.333333333333336, 66.66666666666667, 166.66666666666666]

# filtrowanie danych
for i in lista:
    if i < 10:
        print(i, end=" : ")  # 1 : 2 : 5 :

print()
# filter()
print(f"Użycie filter() {list(filter(lambda x: x < 10, lista))}")
# Użycie filter() [1, 2, 5]
print(f"Użycie filter() {list(filter(lambda x: x > 100, lista))}")  # Użycie filter() [200, 500]
print(f"Użycie filter() {list(filter(lambda x: x < 200, lista))}")  # Użycie filter() [1, 2, 5, 56, 78, 90, 100]
print(f"Użycie filter() {list(filter(lambda x: x > 5 and x < 200, lista))}")
print(f"Użycie filter() {list(filter(lambda x: 5 < x < 200, lista))}")
# Użycie filter() [56, 78, 90, 100]
# Użycie filter() [56, 78, 90, 100]

r0 = {'miasto': "Kielce"}
r1 = {'miasto': "Kielce", "ZIP": "25-900"}

print(r0['miasto'])
print(r1['miasto'])
# Kielce
# Kielce

print(r1['ZIP'])
# print(r0['ZIP']) # KeyError: 'ZIP'

d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))
# 00-000
# 25-900
print(r0)
print(r1)
# {'miasto': 'Kielce', 'ZIP': '00-000'}
# {'miasto': 'Kielce', 'ZIP': '25-900'}

lata = [(2000, 29.7), (2001, 33.12), (2010, 32.92)]
print(max(lata))  # (2010, 32.92)
print(min(lata))  # (2000, 29.7)

print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))
# 33.12
print(max(map(lambda c: c[1], lata)))  # 33.12
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)

a = 10


def funkcja_julia():
    a = 15  # nowa zmienna o zasięgu lokalnym
    print(a)


funkcja_julia()  # 15
print(a)  # 10


def funkcja_julia():
    global a
    a = 15  # uzycie zmiennej globalnej
    print(a)


funkcja_julia()  # 15
print(a)  # 15

max_temp = max(map(lambda c: (c[1], c[0]), lata))
print(max_temp)
temp, year = max_temp
print(temp, year)  # 33.12 2001

# reduce()
#  reduce(function, iterable[, initial], /) -> value
#
#     Apply a function of two arguments cumulatively to the items of an iterable, from left to right.
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
#     calculates ((((1 + 2) + 3) + 4) + 5).
liczby = [1, 2, 3, 4, 5]
wynik = reduce(lambda x, y: x + y, liczby)
print("Wynik reduce x + y", wynik)  # Wynik reduce x + y 15
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15

wynik = reduce(lambda x, y: x * y, liczby)
print("Wynik reduce x*y:", wynik)  # Wynik reduce x*y: 120


# lru_cache

@lru_cache(maxsize=1000)  # dekorator
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


print(fib_cached(10))  # 55
print(fib_cached.cache_info())  # CacheInfo(hits=8, misses=11, maxsize=1000, currsize=11)
print(fib_cached(10))  # 55
print(fib_cached.cache_info())  # CacheInfo(hits=9, misses=11, maxsize=1000, currsize=11)
print(fib_cached(15))  # 610
# CacheInfo(hits=9, misses=11, maxsize=1000, currsize=11)
fib_cached.cache_clear()
print(fib_cached.cache_info())  # CacheInfo(hits=0, misses=0, maxsize=1000, currsize=0)
