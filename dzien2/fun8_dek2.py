# zrobic dekorator, który zmienia wynik dziłania funkcji na duże litery

# teksty są niemutowalne
# """ Return a copy of the string converted to uppercase. """
wynik = "tekst".upper()
print(wynik)  # TEKST
print("tekst".upper())  # TEKST


def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper  # adres, referencja


# zamiana na pogrubione, kolor czerwony
# "\033[1m", "\033[0m"
def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "\033[1m" + result + "\033[0m"

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello World!!!"


print(greeting())  # HELLO WORLD!!!

# kolejnosc ma znaczenie
@bold_decorator
@uppercase_decorator
def greeting2(string):
    return f"Podałeś {string}"


print(greeting2("Radek"))  # bez dekoratora: Podałeś Radek
# z dekoratorem PODAŁEŚ RADEK
