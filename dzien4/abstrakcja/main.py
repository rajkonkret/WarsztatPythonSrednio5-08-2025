# import prototyp
from prototyp import Prototyp
from regular import Regular
from xyz import XYZ

# nie można tworzyc obiektów klasy abstrakcyjnej!!!
# TypeError: Can't instantiate abstract class Prototyp without an implementation
# for abstract methods 'info', 'policz'
# pr = Prototyp(5)

rg = Regular(4, 5)
xz = XYZ(4, 3, 7)

print(rg.info("abc 001"))
print(f"policz: {rg.policz()}")
print(f"policz: {rg.policz()}")
rg.msg()
# Wiadomość: abc 001
# policz: 3.2
# policz: 3.2
# Metoda nieabstrakcyjna klasy abstrakcyjnej

print(xz.info("abc 002"))
print(f"policz: {xz.policz()}")
xz.msg()

# abc 002abc 002abc 002
# policz: 40
# Metoda nieabstrakcyjna klasy abstrakcyjnej

# obiekty różnych klas
lista = [rg, xz]
# polimorfizm
# mozemy potraktoac jako obiekty yej samej klasy abstrakcyjnej
for i in lista:
    print(i.policz())
# 3.2
# 40
