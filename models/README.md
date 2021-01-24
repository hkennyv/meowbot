# Models

This directory contains the files related to the GPT2 models. The approach for
these models leverage the popular [GPT2](https://github.com/openai/gpt-2) by
[OpenAI](https://openai.com/) and fine tuning some new data on top of them.

In this case, I am fine tuning the GPT2-small model on a ton of facebook
messages (so far, I've tried up to 38k fb messages for some models, but have
also had decent results with as little as 3k).

This project is bootstrapped using the [aitextgen](https://github.com/minimaxir/aitextgen)
framework. It's built on top of [PyTorch](https://pytorch.org/) and
[huggingface.co](https://huggingface.co/).

## Usage

### Downloading facebook messages

You can download a huge dump of your facebook messages
[here](https://www.facebook.com/dyi/?referrer=yfi_settings).

### Code

The code is placed into two main directories: `scripts/` and `notebooks/`.
Inside of `scripts/` are some code to clean some facebook message data and to
generate some text using a pre-trained model. Inside of `notebooks/` is the
notebook that is used to fine-tune the gpt2 model using the cleaned facebook
messages.

**NOTE:** it is highly recommended to use a GPU when running the notebook.
running in colab, it took me ~30-60m per model on a nvidia tesla t4 gpu.

## Trained models

Due to the large size of the models, I will not be checking them into this
repository. Instead, please contact me and I can share a link to the google
cloud storage bucket I'm hosting them in.

## License

[aitextgen license](https://github.com/minimaxir/aitextgen/blob/master/LICENSE)
[this repository's license](../LICENSE)
