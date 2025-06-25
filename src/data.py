# src/data.py

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import pandas as pd

def load_data():
    dataset = fetch_california_housing(as_frame=True)
    X = dataset.data
    y = dataset.target
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
