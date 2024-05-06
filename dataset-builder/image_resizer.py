import os
from PIL import Image


def resize():
    print("\nResizing images...")

    input_dir = os.path.abspath("./dataset-builder/output/final/")
    output_dir = os.path.abspath("./dataset-builder/output/final/")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)

        if os.path.isfile(input_path) and filename.lower().endswith(
            (".png", ".jpg", ".jpeg")
        ):
            image = Image.open(input_path)
            resized_image = image.resize((35, 35))
            output_path = os.path.join(output_dir, filename)
            resized_image.save(output_path)

            print("Image resized and saved:", output_path)
        else:
            print("Ignoring:", input_path, "- It's not a valid image.")
