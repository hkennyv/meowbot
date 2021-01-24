"""
gentext.py
author(s): khuynh
description: this is a rough script to load in a pre-trained model and generate
some text from it. it heavily uses the aitextgen framework:

https://github.com/minimaxir/aitextgen
"""
from aitextgen import aitextgen
from pathlib import Path

# user configurable
TRAINED_MODELS = Path("trained_models").resolve()
MODEL_NAME = "elias"
MODEL_VERSION = "v2"

# construct the directory that contains the model and config
directory = TRAINED_MODELS / MODEL_NAME / MODEL_VERSION


ai = aitextgen(model=directory / "pytorch_model.bin", config=directory / "config.json")
# ai.quantize()

ai.generate(
    n=3,
    batch_size=5,
    prompt="how are you doing?",
    min_length=25,
    max_length=256,
    temperature=2.3,
    top_p=0.9,
    seed=0,
)
