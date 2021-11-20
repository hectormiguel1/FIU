import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import confusion_matrix

labels = pd.read_csv('MNIST_LABEL.csv')
features = pd.read_csv('MNIST_15_15.csv')

class LinearRegression:
    """
        A simple class to perform a task of Linear Regression.
        
        Steps
        -----
        * Find the hypothesis using y = mX + c, where X is as input vector.
        * Find the cost value.
        * Use gradient descent to update each parameters.
    """
    def __init__(self):
        """
            This method doesnot take any initial attributes. You will tune the attributes later using methods.
        """
        # instantiate train data and label
        self.X = None 
        self.y = None
        # to store all costs, initially cost is infinity
        self.costs = [np.inf]
        
        # m is for len(X)
        self.m = None
        
        # learning rate
        self.alpha = None
        
        # our all parameters(from each iterations), m, c in y = mx + c
        self.all_parameters = []
    
    def hypothesis(self, x):
        """
            A method to perform linear operation(mx + c) and return.
            
            Formula:
            --------
            \begin{equation}
            h{_\theta}{(x)} = {\theta}^{T}x = \theta{_0} + \theta{_1} x_1 
            \end{equation}

        """
        # y = XM, where X is of shape (M, N) and M of (N, 1)
        h = np.dot(x, self.parameters)
        return h
    
    def cost(self, yp, yt):
        """
            yp: Predicted y.
            yt: True y.

            Formula:
            -------
            \begin{equation}
            J{(\theta)} = \frac{1} {2m} \sum_{i=1}^m (h_\theta (x^{(i)}) - y^{(i)})^2
            \end{equation}

        """
        # find actual deviation
        d = yp - yt 
        # constant 1/2m
        c = 1/(2 * self.m)
        # finally, sum the square of gradients 
        delta = c * np.sum(d ** 2)   
        return delta
    
    def gradient_descent(self):
        """
            A method to perform parameter update based on gradient descent algorithm.
            
            Rule:
            -----
            \begin{equation}
            \theta_j = \theta_j - \alpha \frac{1}{m} \sum_{i=1}^m (h_\theta (x^{(i)}) - y^{(i)}) x_j^{(i)}
            \end{equation}

        """
        temp_theta = self.parameters
        # for each theta
        for j in range(len(temp_theta)):
            grad = np.sum((self.hypothesis(self.X) - self.y)*np.array(self.X[:,j]).reshape(self.m, 1))
            temp_theta[j] = self.parameters[j] - (self.alpha / self.m) * grad
        self.parameters = temp_theta
        self.all_parameters.append(temp_theta.flatten())
        
    def predict(self, X):
        """
            A method to return prediction. Perform preprocessing if model was trained preprocessed data.

            Preprocessing:
            -------------
            X = (X - X.mean()) / X.std()
        """
        if self.preprocessed != True:
            X = np.insert(X, 0, 1, axis=1)
            X = self.normalize(X)
        return self.hypothesis(X)
    
    def visualize(self, thing="cost"):
        """
            Visualise the plots.
            Available thing:
            ----------
            i. cost: Cost value vs iteration
            ii. param: Parameters vs iteration
            iii. all: cost and param vs iteration
        """
        legend = ["Loss"]
        if thing == "cost" or thing == "all":
            plt.title("Loss vs step.")
            plt.grid(True)
            plt.plot(self.costs)
            plt.xlabel("Iterations")
            plt.ylabel("Loss")
            plt.legend(legend)
    
    #def visualize_parameters(self):
        if thing == "param" or thing == "all":
            plt.title("Parameter on each step.")
            plt.grid(True)
            plt.plot(self.all_parameters)
            plt.xlabel("Iterations")
            plt.ylabel("Parameters")
            l = [fr"$\Theta{i}$" for i in range(len(self.parameters))]
            if thing == "all":
                l.insert(0, legend[0])
                legend = l
            else:
                legend = l
            plt.legend(legend)
        
    def normalize(self, X):
        """
            X: Input training data.
            Returns: normalized x.
            
            Normalization:
            --------------
            X = (X - X.mean()) / X.std()
        
        """
        
        means, stds = [], []
        normalized_x = X.copy()
        # since we need to work with only the column we will iterate over shape[1]
        for col in range(normalized_x.shape[1]):
            means.append(normalized_x[:, col].mean())
            stds.append(normalized_x[:, col].std())
            if not col: continue
            normalized_x[:, col] = (normalized_x[:, col] - means[-1])/stds[-1]
        # store the means and stds. We need them on future.
        self.means = means
        self.stds = stds
        return normalized_x

    def fit(self, X, y, error_threshold = 0.001, preprocessed = True, alpha=0.01, show_every=100, iterations=1500):
        """
            X: input train (m X n),  if is not normalized and added axis for bias, use preprocessed=False.
            y: train label (n X 1)
            error_threshold: How much error is tolerable?
            preprocessed: does train data has added axis for bias and normalized?
            alpha: learning rate(update step)
            show_every: how often to show cost?
            iterations: how many steps to run weight update(gradient descent)?
        """
        
        self.preprocessed = preprocessed
        # if data already have bias added and normalized, leave it.
        if preprocessed!=True:
            X = np.insert(X, 0, 1, axis=1)
            X = self.normalize(X)
        self.X = X
        self.y = y
        self.alpha = alpha
        
        # how many of training examples are there?
        self.m = len(X)
        
        # how many of parameters?
        # initialize it to 0, shape must be (num. features + 1, 1)
        # X here is normalized i.e it already have axis for bias
        self.parameters = np.zeros((X.shape[1], 1))
        costs = [np.inf] #Used to plot cost as function of iteration
        i = 0
        
        # if our update is not done for iterations and error is pretty high, 
        while (iterations>i and costs[-1]>error_threshold):
            # find the cost value
            cost_value = self.cost(self.hypothesis(self.X), self.y)
            costs.append(cost_value)
            # perform gradient descent and update param
            self.gradient_descent() 
            if i % show_every == 0:
                print(f"Step: {i} Cost: {round(cost_value, 4)}.")
            
            i+=1
        self.costs = costs


normalized_features = features / 255.0
# b_opt = linear_regression(normalized_features, labels)
# predictions = predict(features, b_opt, .5)
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=1)
_, number_features = normalized_features.shape
lr = LinearRegression()
predictions = []
for train_index, test_index in skf.split(normalized_features, labels):
    X_train, X_test = normalized_features.iloc[train_index], normalized_features.iloc[test_index]
    y_train, y_test = labels.iloc[train_index], labels.iloc[test_index]
    lr.fit(X_train.to_numpy(), y_train.to_numpy().ravel(), error_threshold=0.5)
    prediction = lr.predict(X_test.to_numpy())
    prediction_rounded = np.round(prediction)
    accuracy = (prediction_rounded == y_test.to_numpy()).sum() / len(y_test)
    print(f'Accuracy: {accuracy}')
    (tp, fp, fn, tn) = confusion_matrix(y_test.to_numpy(), prediction_rounded)
    print(prediction)
    print(f'TP: {tp}, FP: {fp}, FN: {fn}, TN: {tn}')