import os
from image_resizer import resize
from picture_to_numbers_converter import convert_image_to_csv


def read_files():
    resize()

    path = os.path.abspath("./dataset-builder/output/splitted/")
    if not os.path.exists(path):
        os.makedirs(path)
    dir_list = os.listdir(path)

    print("\nReading files...")
    for filename in dir_list:
        print(filename, type(filename))
        filepath = os.path.join(path, filename)
        convert_image_to_csv(filepath)

    print("Number of files in '", path, "':", len(dir_list))
    print("Files and directories:", dir_list)
