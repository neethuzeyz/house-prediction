# src/models.py

from sklearn.ensemble import RandomForestRegressor
import pickle

def train_model(X_train, y_train):
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

def save_model(model, path='model/house_price_model.pkl'):
    with open(path, 'wb') as f:
        pickle.dump(model, f)

def load_model(path='model/house_price_model.pkl'):
    with open(path, 'rb') as f:
        return pickle.load(f)
