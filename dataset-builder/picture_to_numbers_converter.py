from PIL import Image
import numpy as np
import os

global output_dir
output_dir = os.path.abspath("./dataset-builder/output/text/")

def convert_image_to_csv(image_path):
    try:
        # Convert image to NumPy array
        arr = np.asarray(Image.open(image_path))

        # Convert 3D array to list of 2d lists
        lst = [[str(pixel) for pixel in row] for row in arr]

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_file = os.path.join(output_dir, os.path.basename(image_path) + ".csv")
        with open(output_file, "w") as f:
            for row in lst:
                f.write(",".join(row) + "\n")

        print("CSV saved successfully: ", output_file)
    except Exception as e:
        print("An error occurred:", e)
