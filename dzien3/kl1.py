# klasy - elementy progrmowania obiektowwego
# szablon, przepis, pieczątka, matryca
# zawiera cechy (zmienne) i metody (funkcje)
# obiekt (instancja) klasy - zbudowany wg przepisu
import math


# PascalCase UpperCamelCase
class MyFirstClass:
    """
    Klasa w Pythonie
    """

    def __init__(self, x=0, y=0):
        """
        Funkcja inicjalizująca (konstruktor)
        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    # oblicz odległośc między punktami
    def calculate(self, other: "MyFirstClass") -> float:
        """
        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).
        :return:
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"{self.x, self.y}"


# print(MyFirstClass.__doc__)  # wypisanie dokumentacji: Klasa w Pythonie
# help(MyFirstClass)
# dokumentacja
# pydoc -b .\kl1.py - serwer dokumentacji
#  pydoc -w kl1 - generuje plik html

point1 = MyFirstClass(5, 9)
print(point1)
# <__main__.MyFirstClass object at 0x000001E3E8D26F90>
print(point1.x)  # 5
print(point1.y)  # 9
# po dodaniu __str__
# (5, 9)

point1.move(45, 90)
print(point1)  # (45, 90)

point2 = MyFirstClass()
print(point2)  # (0, 0)
point2.move(45, 87)
print(point2)  # (45, 87)

point1.reset()
print(point1)  # (0, 0)

print(point2.calculate(point1))
# 97.94896630388705