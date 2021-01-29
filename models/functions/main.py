from utils import generate_text_from_model


def handler(request):
    base_url = request.base_url

    # remove trailing slash if present
    if base_url[-1] == "/":
        base_url = base_url[:-1]

    name = base_url.split("/")[-1]
    prompt = request.args.get("prompt", "")
    n = int(request.args.get("n", 1))

    print(f"{name=} {prompt=} {n=}")

    res = generate_text_from_model(n, name, prompt, min_length=25)

    if res is None:
        f"no model for {name} :(", 400

    return "".join([f"<p>{text}</p>" for text in res]), 200
