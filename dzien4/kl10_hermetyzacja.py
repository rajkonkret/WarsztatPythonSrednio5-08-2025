# hermatyzacja
class Boat:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        # pole prywatne
        # mangling_name - zaciemnianie nazw
        self.__speed = 0

    def sail(self):
        self.__speed += 10
        self.__test()

    def speedometer(self):
        print(f"Speed is {self.__speed} knots")

    def __test(self):
        print("All tested!")


boat = Boat("Omega", 2025)
boat.sail()
boat.sail()
boat.sail()
boat.sail()
boat.sail()
# AttributeError: 'Boat' object has no attribute '__speed'
# pole prywatne
# print(boat.__speed)  # 50
boat.speedometer()  # Speed is 50 knots
boat.__speed = 0  # pole dodakowe o tej samej nazwie co prywatne
boat.speedometer()  # Speed is 0 knots, po ustawieniu na prywatne: Speed is 50 knots
# All tested!
# All tested!
# All tested!
# All tested!
# All tested!
# Speed is 50 knots
# Speed is 50 knots
