import asyncio

from botify import BotifyAPI

api = BotifyAPI() # API key is set in .env


async def main():
    async with api as con:
        user_stats = await con.get_member_stats(1234567890) # Replace with user ID
        print(user_stats)

asyncio.run(main())