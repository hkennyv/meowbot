import logging

import tweepy

from config import config

log = logging.getLogger(__name__)

auth = tweepy.OAuthHandler(config["api_key"], config["api_secret_key"])
auth.set_access_token(config["access_token"], config["access_token_secret"])

api = tweepy.API(auth)

log.info("api authenticated")
