import sys
from dataset_preparer import prepare_dataset
from dataset_splitter import split_dataset
from model_trainer import train_model
from model_evaluator import evaluate_model
from predictor import predict

file_name = sys.argv[1]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing required argument: file_name")
        sys.exit(1)
    
    prepare_dataset(file_name)
    split_dataset()
    train_model()
    evaluate_model()
    predict()
