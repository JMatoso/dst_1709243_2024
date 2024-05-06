import os
import random
import pandas as pd


x = 1000
x_train = 0
x_test = 0
select_train = []
select_test = []
data_train = []
data_test = []
final_name = "prepared_dataset"

datasets_path = os.path.abspath("./simple-ai/datasets/")


def size_x():
    global x
    data = pd.read_csv(
        os.path.join(datasets_path, f"{final_name}.csv"), sep=",", header=None
    )
    x = len(data) - 2


def num_rows(x):
    global x_train
    global x_test
    x_train = int(2 / 3 * x)
    x_test = int(1 / 3 * x)
    while (x_train + x_test) != x:
        x_train = x_train + 1


def select_rows(x):
    global select_train
    global select_test
    row = []
    for i in range(0, x):
        row.append(i)
    i = -1

    while i < x_train:
        i = i + 1
        rnd = random.randrange(len(row))
        select_train.append(row[rnd])
        row.pop(rnd)
        print(len(row))
    select_test = row
    select_train.sort()


def generate_train():
    data = pd.read_csv(
        os.path.join(datasets_path, f"{final_name}.csv"), sep=",", header=None
    )
    global data_train
    global data_test

    for i in select_train:
        print("data[", i, "]=", data.iloc[i])
        data_train.append(data.loc[i])
    for i in select_test:
        data_test.append(data.loc[i])


def split_dataset():
    global x
    global x_train
    global x_test
    global select_train
    global select_test
    global data_train
    global data_test
    global final_name
    global datasets_path
    
    print("\nSplitting dataset...")

    size_x()
    print("size_x= ", x)
    num_rows(x)
    select_rows(x)
    generate_train()
    print(x_train, x_test, (x_train + x_test) == x)
    print("selection_train= ", select_train)
    print("selection_test= ", select_test)
    print(type(data_train))

    df_train = pd.DataFrame(data_train)
    df_test = pd.DataFrame(data_test)

    df_train.to_csv(
        os.path.join(datasets_path, f"{final_name}_train.csv"), header=None, index=None
    )
    df_test.to_csv(
        os.path.join(datasets_path, f"{final_name}_test.csv"), header=None, index=None
    )
