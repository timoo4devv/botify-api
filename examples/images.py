import io

from PIL import Image

from botify import BotifyAPI

api = BotifyAPI()  # API key is set in .env

user_stats = api.get_guild_image(1010915072694046794)  # Your guild ID
img = Image.open(io.BytesIO(user_stats))
img.show()