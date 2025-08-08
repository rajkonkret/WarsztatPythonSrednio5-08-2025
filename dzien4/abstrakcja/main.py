# import prototyp
from prototyp import Prototyp
from regular import Regular

# nie można tworzyc obiektów klasy abstrakcyjnej!!!
# TypeError: Can't instantiate abstract class Prototyp without an implementation
# for abstract methods 'info', 'policz'
# pr = Prototyp(5)

rg = Regular(4, 5)
