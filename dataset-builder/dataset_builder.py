import os
from datetime import datetime

dataset = ""

def process_line(contents):
    global dataset
    conteudo_aux0 = contents.replace("\n", "")
    conteudo_aux1 = conteudo_aux0.replace(",", ";")
    conteudo_aux11 = conteudo_aux1.replace("  ", ",")
    conteudo_aux2_1 = conteudo_aux11.replace(" ", ",")
    conteudo_aux2_2 = conteudo_aux2_1.replace(",,", ",")
    conteudo_aux2_3 = conteudo_aux2_2.replace("[,", "[")
    conteudo_aux2 = conteudo_aux2_3.replace(",]", "]")
    w_array = conteudo_aux2.split(";")
    print("******************")

    for w in w_array:
        w1 = w.replace("[", "")
        w2 = w1.replace("]", "")
        w3 = w2.split(",")
        print(w3[0], ",", w3[1], ",", w3[2], "\n")
        print(
            w3[0],
            ",",
            w3[1],
            ",",
            w3[2],
            ",",
            str(int((int(w3[0]) + int(w3[1]) + int(w3[2])) / 3)),
        )
        dataset = dataset + ";" + str(int((int(w3[0]) + int(w3[1]) + int(w3[2])) / 3))


def build():
    print("\nBuilding dataset...")

    path = os.path.abspath("./dataset-builder/output/text/")
    if not os.path.exists(path):
        os.makedirs(path)

    print(type(os.listdir(path)))
    file_list = os.listdir(path)
    global dataset
    for file in file_list:
        file_path = os.path.join(path, file)
        print(file_path)

        if not os.path.isfile(file_path):
            print("Ignoring:", file_path, " - File not found.")
            continue

        with open(file_path) as f:
            content = f.readlines()
            for line in content:
                process_line(line)
        dataset = dataset + "\n"

    builds_path = os.path.abspath("./dataset-builder/datasets/builds/")
    if not os.path.exists(builds_path):
        os.makedirs(builds_path)

    file_name = f"final_{str(datetime.now().timestamp())}_{file_list[0]}"
    dataset_path = os.path.join(builds_path, file_name)
    file = open(dataset_path, "w")
    file.write(dataset)
    file.close()

    print("\nDataset built and saved:", file_name)
    return dataset_path
