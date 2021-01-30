from utils import generate_text_from_model


def handler(request):
    prompt = request.args.get("prompt", None)
    n = int(request.args.get("n", 1))

    print(f"{prompt=} {n=}")

    res = generate_text_from_model(n, prompt, min_length=25)

    return "".join([f"<p>{text}</p>" for text in res]), 200
