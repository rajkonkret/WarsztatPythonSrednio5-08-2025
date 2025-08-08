# print(2 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\WarsztatPythonSrednio5-08-2025\dzien4\kl_13_wyjatki.py", line 1, in <module>
#     print(2 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

# # rzucanie wyjątku jawnie
# raise ZeroDivisionError("Błąd dzielenia")
# # ZeroDivisionError: Błąd dzielenia

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę cąlkowitą większą od zera"))
    if x <= 0:
        raise MyException("Liczba musi być wieksza od zera")
except MyException:
    print("Wartość musi być większa od zera")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Bład:", e)
else:  # tylko gdy nie ma błedu
    print("Podana wartość:", x)
finally:  # wykona się zawsze
    print("Koniec")
# Podaj liczbę cąlkowitą większą od zera12
# Podana wartość: 12
# Koniec
