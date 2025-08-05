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
