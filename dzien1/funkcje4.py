# lambda - skrócony zapis funkcji
# lambda - zwraca wynik
# funkcja anonimowa - możliwość użycia funkcji w miejscu deklaracji

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