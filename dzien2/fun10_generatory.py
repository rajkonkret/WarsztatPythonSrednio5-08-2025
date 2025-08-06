# generator - generuje wartość w momencie kiedy jest potrzebna

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


# generator
def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # zwraca wartość obliczenia, pamięta, który jest następny


kwa = kwadrat2(5)
print(type(kwa))  # <class 'generator'>
print(kwa)  # <generator object kwadrat2 at 0x000001684C4EA8E0>

print(next(kwa))  # 0
print(next(kwa))  # 1
print(next(kwa))  # 4
print(next(kwa))  # 9
print('Zrob cokolwiek')

print(next(kwa))  # 16
# print(next(kwa)) # StopIteration - generator wyczerpał dane

kwa2 = kwadrat2(10)
for k in kwa2:
    print(k)

kwa3 = kwadrat2(10)
kwa4 = kwadrat2(10)

print(next(kwa3))  # 0
print(next(kwa4))  # 0
print(next(kwa3))  # 1
print(next(kwa4))  # 1
