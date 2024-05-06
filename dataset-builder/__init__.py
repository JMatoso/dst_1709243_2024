import os
from image_splitter import split
from dataset_builder import build
from file_reader import read_files


def load_ai(file_name):
    print(f"\nLoading AI with file '{file_name}'...")
    ai_path = os.path.abspath("./simple-ai/__init__.py")

    if not os.path.isfile(ai_path):
        print("File not found:", ai_path)
        return

    os.system(f"python {ai_path} {file_name}")


if __name__ == "__main__":
    split("tabela6_approved.png", 10, 10)
    read_files()
    load_ai(build())
