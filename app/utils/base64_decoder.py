import base64

def decode_base64_to_image(base64_string: str, output_path: str) -> None:
    image_data = base64.b64decode(base64_string)
    with open(output_path, "wb") as file:
        file.write(image_data)
    print(f"Image saved at {output_path}")