# Botify API
[![](https://img.shields.io/pypi/v/botify-api.svg?style=for-the-badge&logo=pypi&color=yellow&logoColor=white)](https://pypi.org/project/botify-api/)
[![](https://img.shields.io/pypi/l/botify-api?style=for-the-badge&color=5865F2)](https://github.com/timoo4devv/botify-api/blob/main/LICENSE)
[![](https://img.shields.io/readthedocs/botify-api?style=for-the-badge)](https://botify-api.readthedocs.io/)

Official wrapper for the Botify API.

## ⚙️ Installation
Python 3.9 or higher is required
```
pip install botify-api
```

## 🔑 How to get an API key?
1. Invite [Botify](https://discord.com/oauth2/authorize?client_id=1259624304526491669&permissions=8&integration_type=0&scope=bot+applications.commands) to your Discord server or to your Discord account
2. Run `/premium api`

## 🚀 Example Usage
The API key can be passed as a parameter or set as the environment variable `BOTIFY_KEY`.
For more information, see to our [documentation](https://botify-api.readthedocs.io/).

### Sync Example
```python
from botify import BotifyAPI

api = BotifyAPI(api_key="[YOUR_API_KEY]")

user_stats = api.get_user_stats(123456789)  # Replace with user ID
```
### Async Example
```python
import asyncio
from botify import AsyncBotifyAPI

api = AsyncBotifyAPI(api_key="[YOUR_API_KEY]")

async def main():
    user_stats = await api.get_user_stats(123456789)  # Replace with user ID
    await api.close()

asyncio.run(main())
```
You can also use an asynchronous context manager (recommended)
```python
async def main():
    async with api as con:
        user_stats = await con.get_user_stats(123456789)  # Replace with user ID
```