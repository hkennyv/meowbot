from api import api

for tweet in api.home_timeline():
    print(f"{tweet.user.screen_name} {tweet.text}")
