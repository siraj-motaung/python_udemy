import asyncio

import ssl
import certifi
import aiohttp



async def fetch_url(session, url):
    context = ssl.create_default_context(cafile=certifi.where())
    async with session.get(url, ssl=context) as response:
        print(f"Fetched {url} with status {response.status}, Content-type: {response.headers['content-type']} ")


async def main():
    urls = ["https://httpbin.org/delay/2"] * 3

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls ]
        await asyncio.gather(*tasks)
    

asyncio.run(main())







