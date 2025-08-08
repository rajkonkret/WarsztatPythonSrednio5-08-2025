import pandas as pd
# pip install pandas pyarrow

# Przykłowy DataFrame
dane = {
    'imie': ['Jan', 'Anna', 'Piotr'],
    'wiek': [34, 28, 45],
    'miasto': ['Warszawa', 'Kraków', 'Gdańsk']
}
df = pd.DataFrame(dane)

# ✅ Zapis do pliku Parquet
df.to_parquet('dane.parquet', engine='pyarrow', index=False)
print("Zapisano dane do pliku dane.parquet")

# ✅ Odczyt z pliku Parquet
df_wczytane = pd.read_parquet('dane.parquet', engine='pyarrow')
print("Wczytane dane:")
print(df_wczytane)
