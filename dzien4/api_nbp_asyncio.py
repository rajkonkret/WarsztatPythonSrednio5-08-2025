import asyncio
import aiohttp
import time


async def fetch(url, session, index):
    async with session.get(url, ssl=False) as response:
        text = await response.text()
        print(f"Text: {text}")
        return response.status


async def measure_aiohttp():
    url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"

    tasks = []

    overall_start_time = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        for i in range(100):
            tasks.append(fetch(url, session, i + 1))

        statuses = await asyncio.gather(*tasks)

    overall_elapsed_time = time.perf_counter() - overall_start_time
    print(f"Overral time for request: {overall_elapsed_time:4f} seconds.")
    return statuses


# uruchomienie metody asynchronicznej
asyncio.run(measure_aiohttp())
# Overral time for request: 0.309706 seconds.
