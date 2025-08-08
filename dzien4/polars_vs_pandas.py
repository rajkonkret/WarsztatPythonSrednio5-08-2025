import time
import numpy as np
import pandas as pd
import polars as pl

# dane testowe
N = 5_000_000
a = np.random.randint(0, 100, size=N)
b = np.random.rand(N)

# pandas
df_pd = pd.DataFrame({"a": a, "b": b})

start = time.perf_counter()
mean_pd = df_pd[df_pd["a"] > 50]["b"].mean()
pd_end_time = time.perf_counter() - start

# polars
df_pl = pl.DataFrame({"a": a, "b": b})
start = time.perf_counter()
mean_pl = df_pl.filter(pl.col("a") > 50)["b"].mean()
pl_end_time = time.perf_counter() - start

print(f'Pandas: {pd_end_time:.4f} s, wynik = {mean_pd}')
print(f'Polars: {pl_end_time:.4f} s, wynik = {mean_pl}')
# Pandas: 0.0676 s, wynik = 0.5000858355553662
# Polars: 0.0170 s, wynik = 0.5000858355553661
