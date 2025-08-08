def oblicz_srednia(lista):
    if not lista:
        return 0
    suma = sum(lista)
    return suma / len(lista)

def oblicz_srednia_z_kontrola(lista):
    if not lista:
        raise ValueError("Lista nie może być pusta")
    suma = sum(lista)
    return suma / len(lista)
def oblicz_srednia_z_kontrola_i_wyjatkiem(lista):
    if not lista:
        raise ValueError("Lista nie może być pusta")
    try:
        suma = sum(lista)
        return suma / len(lista)
    except TypeError as e:
        raise TypeError("Wszystkie elementy listy muszą być liczbami") from e
def oblicz_srednia_z_kontrola_i_wyjatkiem_i_logowaniem(lista):
    import logging
    logging.basicConfig(level=logging.ERROR)
    if not lista:
        raise ValueError("Lista nie może być pusta")
    try:
        suma = sum(lista)
        return suma / len(lista)
    except TypeError as e:
        logging.error("Wystąpił błąd: %s", e)
        raise TypeError("Wszystkie elementy listy muszą być liczbami") from e

# napisz funkcje obliczjaćą pole trójkąta
def oblicz_pole_trojkata(podstawa, wysokosc):
    if podstawa <= 0 or wysokosc <= 0:
        raise ValueError("Podstawa i wysokość muszą być większe od zera")
    return (podstawa * wysokosc) / 2
# tabnine
# napisz funkcje obliczjaćą pole koła
def oblicz_pole_kola(promien):
    import math
    if promien <= 0:
        raise ValueError("Promień musi być większy od zera")
    return math.pi * (promien ** 2)

# zrob klase osoba z atrybutami imie, nazwisko, wiek
class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        if not imie or not nazwisko:
            raise ValueError("Imię i nazwisko nie mogą być puste")
        if wiek < 0:
            raise ValueError("Wiek nie może być ujemny")
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, {self.wiek} lat"