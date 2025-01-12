import base64

def encode_image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as img_file:
        base64_string = base64.b64encode(img_file.read()).decode("utf-8")
    return base64_string