import pandas as pd
import pickle as p1

def predict():
    try:
        print("\n\n------ Start ------")
        data_X = input("Insert the values to predict\n> ")

        my_list = data_X.split(",")
        res = [eval(i) for i in my_list]
        print(my_list, type(my_list))
        print(res, type(res), len(res))

        df = pd.DataFrame(res)

        loaded_model = p1.load(open("./model_predictor", "rb"))

        y_pred = loaded_model.predict(df.transpose())

        print("\nNumber Predictor: ", int(y_pred[0][0]))
        print("------ Ended ------\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Trying again...\n\n")
    finally:
        predict()
