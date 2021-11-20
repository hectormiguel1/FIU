import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


labels = pd.read_csv('MNIST_LABEL.csv')
features = pd.read_csv('MNIST_15_15.csv')

def solveLinearRegresion(X, y):
    """
        Finds the optimal B given the data X and Y
    """
    return np.dot(np.dot(np.linalg.pinv(np.dot(X.transpose(), X)), X.transpose()),y)

def predict(X, b, threshold):
    """
        Determines which classification X is using B based on some threshold
    """
    return np.array(np.dot(X, b) > threshold)

def accuracy(X, y):
    """
        Determines how many we guessed correctly
    """
    to_int = np.vectorize(lambda x: int(x))
    return (sum(to_int(X) == to_int(y)) / float(len(y))) * 100

def min_max_norm(X):
    """
        Simple min-max norm to normalize the data. Not really sure this is needed but got an extra 2% in my GD accuracy.
    """
    return X / 255.0

def cost(X, y, b):
    """
        Calculates the Ordinary least Squares
    """
    return np.sum((np.dot(X,b) - np.array(y))**2)

def GD_LR(X, y, b):
    """
        Calculates gradient descient linear regression
    """
    return -np.dot(X.transpose(), y) + np.dot(np.dot(X.transpose(), X), b)

normalized_features = min_max_norm(features)
X_train, X_test, y_train, y_test = train_test_split(normalized_features, labels, test_size=0.3, random_state=42)
labels = labels.replace([5,6], [0,1])
b_opt = solveLinearRegresion(X_train, y_train)

kfold = KFold(n_splits=10, shuffle=True)
tprs = []
fprs = []
accuracies = []
for train_index, test_index in kfold.split(normalized_features,labels):
    y_train_kfolds = labels.iloc[train_index]
    y_test_kfolds = labels.iloc[test_index]
    X_test_kfolds = normalized_features.iloc[test_index]
    X_train_kfolds = normalized_features.iloc[train_index]
    b_kfold =solveLinearRegresion(X_train_kfolds, y_train_kfolds)
    predictions_kfold = predict(X_test_kfolds, b_kfold,0.5)
    accuracies.append(accuracy(predictions_kfold, y_test_kfolds))
    tp, fn, fp, tn = confusion_matrix(y_test_kfolds,predictions_kfold,labels=[0,1]).reshape(-1)
    tprs.append(tp/(tp+fn))
    fprs.append(fp/(fp+tn))

print(f'TPRs: {tprs}')
print(f'FPRs: {fprs}')
print(f"Average TPR: {np.mean(tprs)}, Average FPR: {np.mean(fprs)}")
print(f"Average Accuracy: {np.mean(accuracies)}")
