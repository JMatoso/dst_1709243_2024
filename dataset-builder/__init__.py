from image_splitter import split

from dataset_builder import build
from file_reader import read_files


if __name__ == "__main__":
    split("set.jpg", 4, 4)
    read_files()
    build()
