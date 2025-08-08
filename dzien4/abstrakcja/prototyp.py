from abc import ABC, abstractmethod

# klasa abstrakcyjna
# posiada metodę abstrakcyjną
class Prototyp(ABC):
    def __init__(self, x):
        self.x = x

    def msg(self):
        print("Metoda nieabstrakcyjna klasy abstrakcyjnej")

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def info(self, msg):
        pass
