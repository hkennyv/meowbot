from typing import List

import tweepy

from sentiment_bot.api import api


def format_tweet(tweet: tweepy.models.Status):
    return f"@{tweet.user.screen_name:<20s}\n---\n{tweet.text}"


def tweet_unroll_thread(tweet: tweepy.models.Status) -> List[tweepy.models.Status]:
    thread = []
    thread.append(tweet)

    while tweet.in_reply_to_status_id:
        tweet = api.get_status(tweet.in_reply_to_status_id)
        thread.append(tweet)

    return thread
