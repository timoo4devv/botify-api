from botify import BotifyAPI

api = BotifyAPI()  # API key is set in .env

user_stats = api.get_user_stats(123456789)  # Replace with user ID
print(user_stats)