import logging
import tweepy

from sentiment_bot.ml import classifier
from sentiment_bot.utils import format_tweet

log = logging.getLogger(__name__)


class Listener(tweepy.StreamListener):
    def on_connect(self):
        log.debug("stream connected")

    def on_status(self, tweet):
        print(format_tweet(tweet), classifier(tweet.text))
        print("\n")

    def on_disconnect(self, notice):
        log.warning(f"disconnected from stream: {notice}")

    def on_exception(self, exception):
        log.error(f"there was an error: {exception}")
