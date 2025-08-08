from prototyp import Prototyp


class XYZ(Prototyp):
    def __init__(self, x, a, b):
        super().__init__(x)
        self.a = a
        self.b = b

    def policz(self):
        return self.x * (self.a + self.b)

    def info(self, msg):
        return msg * 3


# dygresja
print("13" + "23")  # konkatenacja 1323
print(13 + 23)  # 36
print(12 * "_")  # ____________
# silne typowanie - nie zmienia typów samodzielnie
print(45 + "89")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("89" + 45)
