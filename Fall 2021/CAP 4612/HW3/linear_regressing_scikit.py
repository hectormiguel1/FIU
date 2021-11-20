import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

labels = pd.read_csv('MNIST_LABEL.csv')
features = pd.read_csv('MNIST_15_15.csv')
scaler = MinMaxScaler(feature_range=(0,255))
scaler.fit(features)
scaled_features = scaler.transform(features)
linear_model = LinearRegression()
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=1)

for train_index, test_index in skf.split(scaled_features, labels):
    X_train, X_test = features.iloc[train_index], features.iloc[test_index]
    y_train, y_test = labels.iloc[train_index], labels.iloc[test_index]

    linear_model.fit(X_train, y_train)
    prediction = linear_model.predict(X_test)
    apply_threshold = np.vectorize(lambda x: 5 if round(x + 0.5) == 5 or round(x - 0.5) == 5 else 6 if round(x + 0.5) == 6 or round(x - 0.6) == 6 else round(x))
    apply_rounding = np.vectorize(lambda x: round(x))
    prediction_threshold = apply_threshold(prediction)
    prediction_rounded = apply_rounding(prediction_threshold)
    # print(prediction_rounded)
    #print(accuracy_score(y_test, prediction))
    accuracy =  (sum(prediction_rounded == y_test.to_numpy()) / float(len(y_test))) * 100
    print(accuracy)