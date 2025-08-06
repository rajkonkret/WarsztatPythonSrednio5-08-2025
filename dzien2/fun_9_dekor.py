import time
import tracemalloc
import numpy as np

# pip install numpy

print(np.iinfo(np.int32))
# ---------------------------------------------------------------
# min = -2147483648
# max = 2147483647
# ---------------------------------------------------------------
print(np.iinfo(np.int64))
# ---------------------------------------------------------------
# min = -9223372036854775808
# max = 9223372036854775807
# ---------------------------------------------------------------

tracemalloc.start()
# array1 = np.arange(10_000_000, dtype=np.int64)
array1 = np.arange(10_000_000, dtype=np.int32)
# array2 = np.arange(10_000_000, dtype=np.int64)
array2 = np.arange(10_000_000, dtype=np.int32)
#
# Current memory usage: 152.58807373046875 MB
# Peak memory usage: 152.58807373046875 MB
# int32
# Current memory usage: 76.29412841796875 MB
# Peak memory usage: 76.29412841796875 MB
current, peak = tracemalloc.get_traced_memory()
print(array1.dtype)
tracemalloc.stop()
print(f"Current memory usage: {current / 1024 ** 2} MB")
print(f"Peak memory usage: {peak / 1024 ** 2} MB")

# duza_liczba = 123456789654323
# print(f"{duza_liczba:_}")  # 123_456_789_654_323
# print(f"{duza_liczba:,}")  # 123,456,789,654,323
#
# parametr = 10_000_000_000
# print(type(parametr))  # <class 'int'>
# print(parametr)  # 10000000000
#
# tracemalloc.start()
# lista1 = list(range(10_000_000))
# lista2 = list(range(10_000_000))
#
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f"Current memory usage: {current / 1024 ** 2} MB")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB")
