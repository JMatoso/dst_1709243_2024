import os
import pandas as pd

global datasets_path
datasets_path = os.path.abspath("./simple-ai/datasets/")

def prepare_dataset(dataset_name): # from the folder building_dataset
    print(f"\nPreparing dataset '{dataset_name}'...")
    final_name = "prepared_dataset"
    data = pd.read_csv(os.path.join(datasets_path, f"{dataset_name}"), sep=";", header=None)
    print(type(data))
    print(data)
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    u = []
    u.append(0)

    for x in list:
        u.append(0)
        for y in range(0, 10):
            u.append(x)
    print(u)
    print(len(u))
    data[0] = u
    print(data)
    data.to_csv(os.path.join(datasets_path, f"{final_name}.csv"), header=None, index=None)
