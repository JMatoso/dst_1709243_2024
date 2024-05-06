import os
import pickle as p1
import pandas as pd
from sklearn import linear_model

datasets_path = os.path.abspath("./simple-ai/datasets/")


def train_model():
    global datasets_path
    
    print(f"\nTraining model...")
    
    final_name = "prepared_dataset"
    train_data = pd.read_csv(
        os.path.join(datasets_path, f"{final_name}.csv"), sep=",", header=None
    )
    data_X = train_data.iloc[:, 1:]
    data_Y = train_data.iloc[:, 0:1]
    
    print(data_X, type(data_X))
    print(data_Y)

    regr = linear_model.Ridge(alpha=0.5)
    preditor_linear_model = regr.fit(data_X, data_Y)
    preditor_Pickle = open("./model_predictor", "wb")
    print("model_predictor")
    p1.dump(preditor_linear_model, preditor_Pickle)

    rr = regr.score(data_X, data_Y)
    print("coef. Correl", rr)
