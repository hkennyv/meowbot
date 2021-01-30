import os

from flask import jsonify
from utils import generate_text_from_model


def handler(request):
    url = request.url
    prompt = request.args.get("prompt", None)
    n = int(request.args.get("n", 1))

    print(f"{url=} {prompt=} {n=}")

    res = generate_text_from_model(n, prompt, min_length=25)

    return (
        jsonify(
            {
                "version": 0.1,
                "entry_point": os.environ.get("ENTRY_POINT", ""),
                "function_name": os.environ.get("FUNCTION_NAME", ""),
                "region": os.environ.get("FUNCTION_REGION", ""),
                "results": res,
            }
        ),
        200,
    )
