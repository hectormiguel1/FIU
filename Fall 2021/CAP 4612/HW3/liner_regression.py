import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_curve


labels = pd.read_csv('MNIST_LABEL.csv')
features = pd.read_csv('MNIST_15_15.csv')


def linear_regression(X, y):
    return np.dot(np.dot(np.linalg.pinv(np.dot(X.transpose(), X)), X.transpose()), y)


def predict(X, b, threshhold):
    bool_to_num = np.vectorize(lambda x: 5 if x else 6)
    values = np.array(np.dot(X, b) > threshhold)
    return bool_to_num(values)


def accuracy(X, y):
    return (sum(X == y) / float(len(y))) * 100


def min_max_norm(X):
    return X / 255.0


def fpr_tpr(expected, predicted) -> tuple[float, float]:
    fp = 0
    tp = 0
    fn = 0
    tn = 0
    for i in range(len(expected)):
        if (predicted[i] == 5) & (expected[i] == 6):
            fp += 1
        if (predicted[i] == 5) & (expected[i] == 5):
            tp += 1
        if (predicted[i] == 6) & (expected[i] == 5):
            fn += 1
        if (predicted[i] == 6) & (expected[i] == 6):
            tn += 1
    print (f'FP: {fp}, TP: {tp}, FN: {fn}, TN: {tn}')

    return ((fp / (fp + tn)), (tp / (fn + tp)))


def cost(X, y, b):
    return np.sum((np.dot(X, b) - np.array(y)) ** 2)


def gradient_decent_linear_regression(X, y, b):
    return -np.dot(X.transpose(), y) + np.dot(np.dot(X.transpose(), X), b)


normalized_features = features / 255.0
b_opt = linear_regression(normalized_features, labels)
predictions = predict(features, b_opt, .5)
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=1)
betas = []
costs = []
learning_reate = 10
_, number_features = normalized_features.shape
# class_to_bool = np.vectorize(lambda x: True if x == 6 else False)
# labels = pd.DataFrame(class_to_bool(labels.to_numpy()))
for train_index, test_index in skf.split(normalized_features, labels):
    X_train, X_test = normalized_features.iloc[train_index], normalized_features.iloc[test_index]
    y_train, y_test = labels.iloc[train_index], labels.iloc[test_index]
    estimated_beta = np.zeros(number_features)
    estimated_beta = np.zeros(number_features)
    betas = [estimated_beta]

    costs = [cost(X_train, y_train, estimated_beta)]
    for i in range(0, 100):
        estimated_beta = estimated_beta - learning_reate * \
            gradient_decent_linear_regression(X_train, y_train, estimated_beta)
        estimated_cost = cost(X_train, y_train, estimated_beta)
        betas.append(estimated_beta)
        costs.append(estimated_cost)
    prediction = predict(X_test, estimated_beta, 0.5)
    prediction_to_csv = pd.DataFrame(prediction)
    prediction_to_csv.to_csv("prediction.csv")
    predict_values = prediction[:, 3]
    y_test = y_test.to_numpy()
    shape, shape2 = y_test.shape
    var = predict_values.reshape(shape, shape2)
    # print(y_test_values)
    fpr, tpr = fpr_tpr(y_test, predict_values)
    print(f"FPR: {fpr}, TPR: {tpr}")
    acc = accuracy(var, y_test)
    print(acc)
