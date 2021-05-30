# pyright: reportMissingImports=false
from sentiment_bot.api import api, AuthenticatedStream
from sentiment_bot.listener import Listener
from sentiment_bot.utils import tweet_unroll_thread

stream = AuthenticatedStream(listener=Listener)
stream.filter(track=["covid19"])
