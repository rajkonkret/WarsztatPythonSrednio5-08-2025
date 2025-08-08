import time

import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"


# response = requests.get(url)
# print(response)
# data = response.json()
# print(data)

def multiple_requests():
    start_time = time.perf_counter()

    for _ in range(100):
        response = requests.get(url)
        print(response.json())

    elapsed = time.perf_counter() - start_time
    print(f"Requests time: {elapsed:.4f} ")

# Requests time: 0.0445  dla jedego
multiple_requests() # Requests time: 4.5089
