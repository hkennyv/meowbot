"""
gentext.py
author(s): khuynh
description: this is a rough script to load in a pre-trained model and generate
some text from it. it heavily uses the aitextgen framework:

https://github.com/minimaxir/aitextgen
"""
import configparser
from pathlib import Path

from aitextgen import aitextgen

config = configparser.ConfigParser()
config.read("config.ini")

# user configurable
TRAINED_MODELS = config["DEFAULT"]["TRAINED_MODEL_FOLDER"]
MODEL_NAME = config["DEFAULT"]["MODEL_NAME"]
MODEL_VERSION = config["DEFAULT"]["MODEL_VERSION"]

# construct the directory that contains the model and config
directory = Path(TRAINED_MODELS).resolve() / MODEL_NAME / MODEL_VERSION


ai = aitextgen(model_folder=directory, config=directory)

# ai.generate(
#     n=3,
#     batch_size=5,
#     # prompt="i would give anything to",
#     min_length=256,
#     max_length=1024,
#     temperature=2.3,
#     top_p=0.9,
#     seed=0,
# )

ai.generate(n=10)
