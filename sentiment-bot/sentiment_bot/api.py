import logging

import tweepy

from sentiment_bot.config import config  # type: ignore

log = logging.getLogger(__name__)


auth = tweepy.OAuthHandler(config["api_key"], config["api_secret_key"])
auth.set_access_token(config["access_token"], config["access_token_secret"])


class AuthenticatedStream(tweepy.Stream):
    def __init__(self, listener):
        self._auth = auth
        super().__init__(self._auth, listener())


api = tweepy.API(auth)
log.info("api authenticated")
