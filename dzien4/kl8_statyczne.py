# metody statyczne

class Matematyka:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


print(Matematyka.dodaj(67, 90))  # 157
print(Matematyka.odejmij(67, 90))  # -23
