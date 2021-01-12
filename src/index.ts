import { TwitterClient } from "twitter-api-client";

require("dotenv").config();

const twitterClient: TwitterClient = new TwitterClient({
  apiKey: process.env.TWITTER_API_KEY || "",
  apiSecret: process.env.TWITTER_API_SECRET || "",
  accessToken: process.env.TWITTER_ACCESS_TOKEN,
  accessTokenSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
});

// tweet "meow"
twitterClient.tweets
  .statusesUpdate({
    status: "meow",
  })
  .then((res) => console.log(res))
  .catch((err) => console.log(err));
