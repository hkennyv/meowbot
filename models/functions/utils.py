import os

from typing import Optional
from pathlib import Path

from aitextgen import aitextgen
from google.cloud import storage


# cache model to lower response times
TMP_PATH = Path(os.environ.get("TMP_DIR", "./"))
if not (TMP_PATH / "model.bin").exists():

    client = storage.Client("gpt2-models")
    bucket = client.get_bucket("gpt2-models")

    pytorch_model = bucket.get_blob(
        f"trained_models/{os.environ.get('model_name')}/v1/pytorch_model.bin"
    )
    pytorch_model.download_to_filename("model.bin")

    config = bucket.get_blob(
        f"trained_models/{os.environ.get('model_name')}/v1/config.json"
    )
    config.download_to_filename("config.json")

ai = aitextgen(model=Path("model.bin"), config=Path("config.json"))


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

    return res
