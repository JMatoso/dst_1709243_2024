import os
from datetime import datetime


def process_line(contents):
    processed_line = ""

    content = contents.replace("\n", "").replace(",", ";").replace("  ", ",")
    content = content.replace(" ", ",").replace(",,", ",").replace("[,", "[")

    word_array = content.replace(",]", "]").split(";")
    for word in word_array:
        word = word.replace("[", "").replace("]", "").split(",")
        processed_line = (
            processed_line
            + ";"
            + str(int((int(word[0]) + int(word[1]) + int(word[2])) / 3))
        )

    return processed_line


def build():
    print("\nBuilding dataset...")

    path = os.path.abspath("./dataset-builder/output/text/")
    if not os.path.exists(path):
        os.makedirs(path)

    print(type(os.listdir(path)))
    file_list = os.listdir(path)
    dataset = ""
    for file in file_list:
        file_path = os.path.join(path, file)
        print(file_path)

        if not os.path.isfile(file_path):
            print("Ignoring:", file_path, " - File not found.")
            continue

        with open(file_path) as f:
            content = f.readlines()
            for line in content:
                dataset = dataset + ";" + process_line(line)
        dataset = dataset + "\n"

    builds_path = os.path.abspath("./dataset-builder/datasets/builds/")
    if not os.path.exists(builds_path):
        os.makedirs(builds_path)

    file_name = f"final_{str(datetime.now().timestamp())}_{file_list[0]}"
    file = open(os.path.join(builds_path, file_name), "w")
    file.write(dataset)
    file.close()
    
    print("\nDataset built and saved:", file_name)
