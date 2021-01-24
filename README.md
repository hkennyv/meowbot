<p align="center">
  <a href="https://github.com/hkennyv/meowbot/actions?query=workflow%3ABuild"><img alt="CI" src="https://img.shields.io/github/workflow/status/hkennyv/meowbot/Build"></a>
  <a href="https://github.com/hkennyv/meowbot/actions?query=workflow%3AFormat"><img alt="CI" src="https://img.shields.io/github/workflow/status/hkennyv/meowbot/Format?label=format"></a>
  <a href="https://github.com/hkennyv/meowbot/actions?query=workflow%3ATweet"><img alt="CI" src="https://img.shields.io/github/workflow/status/hkennyv/meowbot/Tweet?label=tweet"></a>
  <a href="https://github.com/hkennyv/meowbot/actions?query=workflow%3ABlack"><img alt="CI" src="https://img.shields.io/github/workflow/status/hkennyv/meowbot/Black?label=black"></a>
</p>

# meowbot

A simple twitter bot made to explore the Twitter API. I have not decided yet what I want to do with it yet...

Currently, this bot tweets "meow" everyday at 7:00PM PST. You can see the
status of the tweet action
[here](https://github.com/hkennyv/meowbot/actions?query=workflow%3ATweet).

See it in action here: <https://twitter.com/winstondakitten>

## Models

This project is designed to be used in conjunction with a fine-tuned version of
the popular [gpt2](https://github.com/openai/gpt-2) language model. In this
project, I take a pre-trained gpt2-small model and fine-tune it using a lot of
my own facebook messages from my friends.

For more details on this, see [models](models/README.md).

## License

See [LICENSE](LICENSE).
