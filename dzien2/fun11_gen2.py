from itertools import zip_longest


def wznowienie(n, k):
    print("Wstrzymanie działania...")
    yield 1001
    print("Wznowienie dizałania")
    yield n + k
    print("Działanie - dodawanie - Wstrzymanie")
    print("Wznowienie działania")
    n = 3 * n
    yield n - k
    print("Działanie - odejmowanie - Wstrzymanie")
    print("Wznowienie działania")
    yield n * k
    print("Działanie - mnożenie - Wstrzymanie")
    print("Wznowienie działania")
    yield n / k
    print("Działanie - dzielenie - Wstrzymanie")


print(wznowienie(6, 7))
print(list(wznowienie(6, 7)))

print(20 * "-")
for i in wznowienie(6, 8):
    if i == 1001:
        continue  # wraca na początek pętli pobiera kolejny element
    print(f"Yield zwraca wartość: {i}")


# --------------------
# Wstrzymanie działania...
# Wznowienie dizałania
# Yield zwraca wartość: 14
# Działanie - dodawanie - Wstrzymanie
# Wznowienie działania
# Yield zwraca wartość: 10
# Działanie - odejmowanie - Wstrzymanie
# Wznowienie działania
# Yield zwraca wartość: 144
# Działanie - mnożenie - Wstrzymanie
# Wznowienie działania
# Yield zwraca wartość: 2.25
# Działanie - dzielenie - Wst

def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


def gen5():
    i = 1
    while True:
        command = yield i * i
        print(command)
        if command == "stop":
            break  # zatrzyma generator
        i += 1


g5 = gen5()
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))
g5.send("Ok")  # Ok

try:
    g5.send("stop")  # StopIteration
except Exception as e:
    print("Bład:", e)


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fib = fibo_with_index(10)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
# (0, 0)
# (1, 1)
# (2, 1)
# (3, 2)
# (4, 3)

for i, n in fibo_with_index(10):
    print(f'Pozycja: {i}, element: {n}')
# Pozycja: 0, element: 0
# Pozycja: 1, element: 1
# Pozycja: 2, element: 1
# Pozycja: 3, element: 2
# Pozycja: 4, element: 3
# Pozycja: 5, element: 5
# Pozycja: 6, element: 8
# Pozycja: 7, element: 13
# Pozycja: 8, element: 21
# Pozycja: 9, element: 34

person = ["Radek", "Tomek", "Zenek", 'Ania', "Kasia"]
wiek = [34, 56, 78, 34]

# Radek 34
for p, w in zip(person, wiek):
    print(p, w)
# Radek 34
# Tomek 56
# Zenek 78
# Ania 34
print(10 * "-")
for p, w in zip(person, wiek):
    print(p, w)

zipped = zip_longest(person, wiek, fillvalue="Brak danych")
print(zipped) # <itertools.zip_longest object at 0x0000023B79ABC3B0>
lista = list(zipped) # wrzucamy do listy by dane można było używać wielokrotnie
# tylko raz można wykorzystac dane z iteratora/generatora
print(25 * "- -")
for imie, wiek in zipped:
    print(imie, wiek)
# Radek 34
# Tomek 56
# Zenek 78
# Ania 34
# Kasia Brak danych
# generator wykorzystany - dane juz się nie pojawią
print(25 * "-")
for imie, wiek in zipped:
    print(imie, wiek)

for imie, wiek in lista:
    print(imie, wiek)
# Radek 34
# Tomek 56
# Zenek 78
# Ania 34
# Kasia Brak danych