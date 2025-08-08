# iterator
# dane tylko gdy potrzebne

lista = [1, 2, 3, 4, 5]
iterator = iter(lista)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# 1
# 2
# 3
print("Coś innego")
print(next(iterator))


# Coś innego
# 4

class Count:
    def __init__(self, lows, high):
        """
        metoda inicjalizująca
        :param lows: start
        :param high: stop
        """
        self.current = lows
        self.higs = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.higs:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


print("-------")
counter = Count(1, 5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
try:
    print(next(counter))
except StopIteration as e:
    print("koniec:", e)
# -------
# 1
# 2
# 3
# 4
# 5
# koniec: