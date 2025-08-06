import time
import tracemalloc
import numpy as np

# numpy - do dzialń na tablicach i macierzach, napisana w c
# pip install numpy
#
# print(np.iinfo(np.int32))
# # ---------------------------------------------------------------
# # min = -2147483648
# # max = 2147483647
# # ---------------------------------------------------------------
# print(np.iinfo(np.int64))
# # ---------------------------------------------------------------
# # min = -9223372036854775808
# # max = 9223372036854775807
# # ---------------------------------------------------------------
#
# tracemalloc.start()
# # array1 = np.arange(10_000_000, dtype=np.int64)
array1 = np.arange(10_000_000, dtype=np.int32)
# # array2 = np.arange(10_000_000, dtype=np.int64)
array2 = np.arange(10_000_000, dtype=np.int32)
# #
# # Current memory usage: 152.58807373046875 MB
# # Peak memory usage: 152.58807373046875 MB
# # int32
# # Current memory usage: 76.29412841796875 MB
# # Peak memory usage: 76.29412841796875 MB
# current, peak = tracemalloc.get_traced_memory()
# print(array1.dtype)
# tracemalloc.stop()
# print(f"Current memory usage: {current / 1024 ** 2} MB")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB")


# duza_liczba = 123456789654323
# print(f"{duza_liczba:_}")  # 123_456_789_654_323
# print(f"{duza_liczba:,}")  # 123,456,789,654,323
#
# parametr = 10_000_000_000
# print(type(parametr))  # <class 'int'>
# print(parametr)  # 10000000000
#
# tracemalloc.start()
lista1 = list(range(10_000_000))
lista2 = list(range(10_000_000))


#
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f"Current memory usage: {current / 1024 ** 2} MB")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB")
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_time():
    time.sleep(2)  # zatrzyma się na 2 sekundy


@measure_time
def add_without_np():
    result = [lista1[i] + lista2[i] for i in range(len(lista1))]
    return "Ok"


@measure_time
def add_with_for():
    result = []  # pusta lista
    for i in range(len(lista1)):
        suma = lista1[i] + lista2[i]
        result.append(suma)  # dodnie do listy
    return "OK"


# zip() - łaczy kolekcje
@measure_time
def add_zip():
    result = [a + b for a, b in zip(lista1, lista2)]
    return "OK ZIP"


@measure_time
def add_np():
    result = array1 + array2
    return "ok np"


my_time()  # Czas wykonania funkcji my_time: 2.0003836154937744
add_without_np()  # Czas wykonania funkcji add_without_np: 0.9656975269317627
add_with_for()  # Czas wykonania funkcji add_with_for: 1.089667558670044
add_zip()  # Czas wykonania funkcji add_zip: 0.838559627532959
add_np()  # Czas wykonania funkcji add_np: 0.019431591033935547

l1 = [1, 2, 3]
l2 = [3, 4, 5]
