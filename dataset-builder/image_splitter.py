import os
from split_image import split_image


def split(fileNameWithImageFormat, rows, cols):
    print("\nSplitting image...")
    images_dir = os.path.abspath("./dataset-builder/datasets/images/")
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    input = os.path.join(images_dir, fileNameWithImageFormat)
    if not os.path.exists(input):
        print("File not found")
        return

    output = os.path.abspath("./dataset-builder/output/final/")
    if not os.path.exists(output):
        os.makedirs(output)

    split_image(input, rows, cols, False, False, output_dir=output)
