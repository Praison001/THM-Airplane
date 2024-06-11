# THM-Airplane - Enumerate Process IDs

This python3 script is related to enumerating processes on the Airplane machine from TryHackMe
https://tryhackme.com/r/room/airplane

I have made the script faster using aiohttp and aiosync libraries to make asynchronous requests.

This way, you can send multiple requests concurrently, which should speed up the process. 