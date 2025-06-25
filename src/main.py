# src/main.py

from data import load_data, split_data
from features import preprocess
from models import train_model, save_model
from metrics import evaluate_model

def main():
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    X_train_scaled, X_test_scaled, scaler = preprocess(X_train, X_test)
    
    model = train_model(X_train_scaled, y_train)
    save_model(model)
    
    metrics = evaluate_model(model, X_test_scaled, y_test)
    print("Model Evaluation Metrics:")
    print(metrics)

if __name__ == "__main__":
    main()
