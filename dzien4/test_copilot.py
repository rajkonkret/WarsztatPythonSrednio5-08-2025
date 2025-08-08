import unittest
import math
from io import StringIO
import logging

# Zakładam, że funkcje są w tym samym pliku — jeśli nie, trzeba zaimportować z innego modułu

# Funkcje, które testujemy
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
    logging.basicConfig(level=logging.ERROR)
    if not lista:
        raise ValueError("Lista nie może być pusta")
    try:
        suma = sum(lista)
        return suma / len(lista)
    except TypeError as e:
        logging.error("Wystąpił błąd: %s", e)
        raise TypeError("Wszystkie elementy listy muszą być liczbami") from e

def oblicz_pole_trojkata(podstawa, wysokosc):
    if podstawa <= 0 or wysokosc <= 0:
        raise ValueError("Podstawa i wysokość muszą być większe od zera")
    return (podstawa * wysokosc) / 2

def oblicz_pole_kola(promien):
    if promien <= 0:
        raise ValueError("Promień musi być większy od zera")
    return math.pi * (promien ** 2)

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


class TestFunkcje(unittest.TestCase):

    # Testy oblicz_srednia
    def test_oblicz_srednia_zwykle(self):
        self.assertEqual(oblicz_srednia([1, 2, 3]), 2)

    def test_oblicz_srednia_pusta(self):
        self.assertEqual(oblicz_srednia([]), 0)

    # Testy oblicz_srednia_z_kontrola
    def test_oblicz_srednia_z_kontrola(self):
        self.assertEqual(oblicz_srednia_z_kontrola([2, 4]), 3)

    def test_oblicz_srednia_z_kontrola_pusta(self):
        with self.assertRaises(ValueError):
            oblicz_srednia_z_kontrola([])

    # Testy oblicz_srednia_z_kontrola_i_wyjatkiem
    def test_oblicz_srednia_z_typem(self):
        self.assertEqual(oblicz_srednia_z_kontrola_i_wyjatkiem([1, 2]), 1.5)

    def test_oblicz_srednia_z_typem_nie_liczba(self):
        with self.assertRaises(TypeError):
            oblicz_srednia_z_kontrola_i_wyjatkiem([1, 'a'])

    def test_oblicz_srednia_z_typem_pusta(self):
        with self.assertRaises(ValueError):
            oblicz_srednia_z_kontrola_i_wyjatkiem([])

    # Testy z logowaniem
    def test_oblicz_srednia_z_logowaniem(self):
        self.assertAlmostEqual(oblicz_srednia_z_kontrola_i_wyjatkiem_i_logowaniem([3, 6]), 4.5)

    def test_oblicz_srednia_z_logowaniem_blad(self):
        with self.assertRaises(TypeError):
            oblicz_srednia_z_kontrola_i_wyjatkiem_i_logowaniem([1, 'x'])

    # Testy pola trójkąta
    def test_oblicz_pole_trojkata(self):
        self.assertEqual(oblicz_pole_trojkata(4, 5), 10)

    def test_oblicz_pole_trojkata_blad(self):
        with self.assertRaises(ValueError):
            oblicz_pole_trojkata(0, 3)

    # Testy pola koła
    def test_oblicz_pole_kola(self):
        self.assertAlmostEqual(oblicz_pole_kola(2), math.pi * 4)

    def test_oblicz_pole_kola_blad(self):
        with self.assertRaises(ValueError):
            oblicz_pole_kola(-1)

    # Testy klasy Osoba
    def test_osoba_poprawna(self):
        osoba = Osoba("Jan", "Kowalski", 30)
        self.assertEqual(str(osoba), "Jan Kowalski, 30 lat")

    def test_osoba_puste_imie(self):
        with self.assertRaises(ValueError):
            Osoba("", "Nowak", 25)

    def test_osoba_ujemny_wiek(self):
        with self.assertRaises(ValueError):
            Osoba("Anna", "Nowak", -5)

if __name__ == '__main__':
    unittest.main()
