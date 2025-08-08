from functools import total_ordering


class MyNumber:
    def __init__(self, value):
        self.values = value


num1 = MyNumber(5)
num2 = MyNumber(15)

print(5 < 15)  # True
# print(num1 < num2)  # TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'
print(num1.values < num2.values)  # True


@total_ordering  # pozwala na wszystkie porównania
class MyNumber2:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


num3 = MyNumber2(5)
num4 = MyNumber2(15)
print(num3 < num4)  # True
print(num3 == num4)  # False, porównanie referencji
# musimy dodac metode __eq__ aby działao przyrównanie
print(num3 > num4)
num5 = MyNumber2(15)
print(num5 == num4)  # True


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point1 = Point(1, 4)
point2 = Point(7, 8)

result = point1 + point2
print("Wynik:", result)  # Wynik: Point(8, 12)
