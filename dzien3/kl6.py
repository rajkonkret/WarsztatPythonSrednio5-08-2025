class A:
    def method(self):
        print("Metoda z klasy A")


a = A()
a.method()  # Metoda z klasy A


class B:
    def method(self):
        print("Metoda z klasy B")


b = B()
b.method()  # Metoda z kalsy B


class C(B, A):
    """
    Klasa dziedziczy po klasie B i a
    """


c = C()
c.method()  # Metoda z kalsy B
print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

class D(A, B):
    """
    Klasa dziedziczy po A i B
    """


d = D()
d.method()  # Metoda z klasy A


class E(A, B):
    def method(self):
        print("Metoda z klasy E")


print(E.__mro__)
e = E()
e.method()  # Metoda z klasy E


class F(A, B):
    def method(self):
        B.method(self)


print(F.__mro__)
# (<class '__main__.F'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
f = F()
f.method()  # Metoda z klasy B


class G(A, B):
    def method(self):
        super().method()  # super() - możemy uzyć super, tutaj klasa: A
        print("Dopisane")
        B.method(self)


g = G()
g.method()
# Metoda z klasy A
# Dopisane
# Metoda z klasy B