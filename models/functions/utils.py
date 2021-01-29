from typing import Optional
from pathlib import Path

from aitextgen import aitextgen

DIR_MODELS = Path("trained_models")

# cache models for serverless function
models = {
    "elias": aitextgen(
        model=DIR_MODELS / "elias/v2/pytorch_model.bin",
        config=DIR_MODELS / "elias/v2/config.json",
    ),
    "jai": aitextgen(
        model=DIR_MODELS / "jai/v1/pytorch_model.bin",
        config=DIR_MODELS / "jai/v1/config.json",
    ),
    "diana": aitextgen(
        model=DIR_MODELS / "diana/v1/pytorch_model.bin",
        config=DIR_MODELS / "diana/v1/config.json",
    ),
    "saumil": aitextgen(
        model=DIR_MODELS / "saumil/v1/pytorch_model.bin",
        config=DIR_MODELS / "saumil/v1/config.json",
    ),
}


def generate_text_from_model(
    n: int,
    model: str,
    prompt: str,
    min_length: int = None,
    max_length: int = 256,
    temperature: float = 1.5,
    top_p: float = 0.7,
    **kwargs
) -> Optional[str]:
    ai = models.get(model, None)

    if ai is None:
        return None

    res = ai.generate(
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
