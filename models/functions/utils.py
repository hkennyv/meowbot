import logging
import os

import torch

from typing import Optional
from pathlib import Path

from aitextgen import aitextgen
from google.cloud import storage


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# cache model to lower response times
TMP_PATH = Path(os.environ.get("TMP_DIR", "./"))

if not (TMP_PATH / "model.bin").exists():
    client = storage.Client("gpt2-models")
    bucket = client.get_bucket("gpt2-models")

    pytorch_model = bucket.get_blob(
        f"trained_models/{os.environ.get('model_name')}/v1/pytorch_model.bin"
    )
    pytorch_model.download_to_filename(TMP_PATH / "model.bin")

    config = bucket.get_blob(
        f"trained_models/{os.environ.get('model_name')}/v1/config.json"
    )
    config.download_to_filename(TMP_PATH / "config.json")

logger.debug(f"{torch.cuda.is_available()=}")

ai = aitextgen(
    model=TMP_PATH / "model.bin",
    config=TMP_PATH / "config.json",
    to_gpu=torch.cuda.is_available(),
)


def generate_text_from_model(
    n: int,
    prompt: str,
    min_length: int = None,
    max_length: int = 256,
    temperature: float = 1.5,
    top_p: float = 0.7,
    **kwargs,
) -> Optional[str]:

    res = ai.generate(
        batch_size=5,
        n=n,
        prompt=prompt,
        min_length=min_length,
        max_length=max_length,
        temperature=temperature,
        top_p=top_p,
        return_as_list=True,
        **kwargs,
    )

    return [s.strip().replace("\n", " ") for s in res]
