import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras import layers, model
import data


def create_seq_data(train_data, window_size=6):
    X, y = [], []

    for i in range(window_size, len(train_data)):
        X.append(train_data[i - window_size:i])
        y.append(train_data[i][3:5])
    return np.array(X), np.array(y)


def split_test_data(test_data):
    X, y = [], []

    for i in range(len(test_data)):
        X.append(test_data)


train_data = np.array(data.get_train_data())
X, y = create_seq_data(train_data)

scaler_X = StandardScaler()
scaler_Y = StandardScaler()

X = X.reshape((X.shape[0], X.shape[1] * X.shape[2]))
X = scaler_X.fit_transform(X)
y = scaler_Y.fit_transform(y)


