from sentiment_bot import __version__
from sentiment_bot import api, utils


def test_version():
    assert __version__ == "0.1.0"


class TestUtils:
    SAMPLE_TWEET_ID = 1379142615828860929

    def test_tweet_unroll_thread(self):
        tweet = api.api.get_status(self.SAMPLE_TWEET_ID)
        thread = utils.tweet_unroll_thread(tweet)

        assert len(thread) == 3
