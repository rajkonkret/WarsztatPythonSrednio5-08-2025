import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

response = requests.get(url)
print(response)
data = response.json()
print(data)
