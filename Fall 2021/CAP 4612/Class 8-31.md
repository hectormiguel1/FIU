 [Table of Contents](#table-of-contents)
- [Class 8-31 : Introduction to Machine Learning](#class-8-31--introduction-to-machine-learning)
  - [Data representation:](#data-representation)
  - [Types of Data](#types-of-data)
  - [Types of Variable](#types-of-variable)
  - [Data Representation Cont.](#data-representation-cont)
  - [Note](#note)
- [Homework # 1 was issued](#homework--1-was-issued)
- [Class 9-7: Classification Problem](#class-9-7-classification-problem)
  - [Learning Process in ML](#learning-process-in-ml)
- [K-Nearest Neighbor Algorithm](#k-nearest-neighbor-algorithm)
  - [Classification Approach](#classification-approach)
    - [Training Data](#training-data)
  - [Pseudo-code](#pseudo-code)
  - [Decision Boundaries](#decision-boundaries)
  - [Pros and Cons](#pros-and-cons)
- [Evaluation](#evaluation)
  - [Metrics](#metrics)
  - [Limitiation of Accuracy](#limitiation-of-accuracy)
  - [ROC Curve](#roc-curve)
  - [Methods of Validation](#methods-of-validation)
  - [Stratified cross-validation](#stratified-cross-validation)
- [Linear Regression](#linear-regression)
  - [Correlation (r)](#correlation-r)
  - [Ordinary Least Squares (OLS)](#ordinary-least-squares-ols)
  - [Optimization](#optimization)
  - [Linear regression with categorical cariables](#linear-regression-with-categorical-cariables)
- [Optimization](#optimization-1)


# Class 8-31 : Introduction to Machine Learning

## Data representation: 
    While in general we use binary for computer science, we use matrix/vectors for machine learning. 

## Types of Data 
     Scalar: Holds a single value. 
     Vector: Holds an array of values. 
     Matrix: Holds a M x N dimensional array of data (2-D Array)
     Tensor:  Array with more than one axes, an Array of Matrices. 

## Types of Variable
     Categorical Variables: Discrete or qualitative variables
        * Nominal: Have two or more categories, but which do not have an intrinsic order. 
            Example: Gender and Color
        * Ordinal: Have two ore more categories which can be ordered or ranked. 
            Example: Class Letter grades. 
     Contentious Variables: Anything else. 

## Data Representation Cont.
       - Many have implicit/explicit patterns to describe a phenomenon. 
    Features: 
       - An individual measurable property of a phenomenon being observed. 
       - They number of features or distinct traits that can be used to describe each item in a quantitative manner. 
       - Many have implicit/explicit patterns to describe a phenomenon. 
    Samples: 
        - Items to process (classify or cluster)
        - Can be a document, a picture, a sound, a video, or a patient
        - Features are characteristics of a sample. 
    Feature Vector: 
        - An N-dimensional vector of numerical features that represent some objects. 
        - A sample consists of feature vectors
    Feature Extraction (Feature Selection):
        - Preparation of feature vector
        - Transforms the data in the high-dimensional space to a space of fewer dimensions. 
        - Dimensional Reduction when actual features are found and the search space is lowered.  
        - Feature Engineering: Process that takes raw data and transforms it into features that can be used to create a predictive model using machine learning or statistical modeling.
table of Contents
    
## Note 
 *Missing Data can be a big problem in Machine Learning, and thus some cleaning of the data must of completed. If a sample has too many missing values, then the data can be discarded, otherwise, when few bits of data are missing, the values can be computed using something such ash Near Neighbor.*     

# Homework # 1 was issued
- Submission as word document or pdf
- Call code must be in single python file. 
- Violin plot must be provided, Density + Box plot. Plot values for each column.
- Use Principal Component Analysis
- Reduce the dimensions. 
	- Categories:
		- Feature Selection: Determining subset of features from data. (Concrete Auto-encoder)
		- Feature Extraction: Come up with new features. (Auto-encoder)



# Class 9-7: Classification Problem 

## Learning Process in ML

Training Data -> Pre-processing -> Model Learning -> Model Testing <- Test Data 

Pre-proceeding 
- Missing value imputation 
- Noise Filtering 
- Feature selection:
  - Subset of (word) features (concrete auto-encoder)
- Feature Extraction 
  - Come ups with new (hidden) features (Standard Auto-encoder)
- Feature Scaling. 
  - Standardization
  - Normalization 
  - Min-Max Normalization 

Model Learning: 
- Classification 
  - Regression 
  - Clustering 

Model Testing:
   - Cross Validation 


# K-Nearest Neighbor Algorithm 
- Simple , but a very powerful classification algorithm (Supervised learning)
- Classifies based on a similarity measure
- Non-parametric
- Lazy Learning 
  - Does not "learn" until the text example is given 
  - Whenever we have a new data to classify, we find its K-nearest neighbors from the training data. 

## Classification Approach
- Classified by the "Majority Votes" for its neighbor classes
  - Assigned to the most common class amongst its k-nearest neighbors (by measuring "distant" between data). 

### Training Data
  |     | Label |
  | --- | ----- |
  | 1   | A     |
  | 2   | B     |
  | 3   | A     |
  | 4   | A     |
  | 5   | B     |
  | 6   | B     |
  | 7   | B     |

Sort in ascending  order 

## Pseudo-code
1. Determine the parameter K = number of nearest neighbors.
2. Calculate the distance between the query-instance and all the training examples.
3. Sort the distance and determine the nearest neighbors based on the k-th minimum distance 
4.  Gather the category Y of the nearest neighbors. 
5.  Use simple majority of the category of the nearest neighbors as the prediction value of the query instance. 

## Decision Boundaries 
- Voronoi diagram 
  - Describes the areas that are the nearest to any given point, give a set of data. 
  - Each line segment is equidistant between two points of the opposite class. 
- With large numbers of examples,and possible noise on the labels, the decision boundary can become nasty, 
  - "Over-fitting" Problem: Model is too complex, boundaries are placed strictly around classes samples.  
- Larder k produces smoother boundary effects. 
- When K == N, always predict tge majority class. 
  - The smaller the K value the higher the chances the model will ......
  - If k == # of Majority class, Model will always predict majority class. 
## Pros and Cons

- Pros 
  - Learning and implementations is extremely simple and intuitive. 
  - Flexible decision boundaries
- Cons 
  - Irrelevant or correlated features have high impact and must be eliminated
  - Typically difficult to handle hight dimensionality 
  - Computational cost: memory and classification time computation. 


Given K == N: Prediction from model will always be 'Major Class' 

Give K >= N/2: Prediction from model will no always be 'Major Class'
# Evaluation

<h3 style="color:red">  Unspoervised agorithms do no have proper evaluation procedures. </h3>

## Metrics

- Confusion Matrix: shows performance of an alogrithm, specially predictive capability.  


|                |                                                                                              | Prediction Condition                                                                                     |                                                                                                 |                                                                                                            |                                                                                                    |
| -------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
|                | Total Population                                                                             | Predicted Condition Positive                                                                             | Predicted Condition Negative                                                                    | Prelevance = \(\frac {\sum Condition Positive} {\sum Total Population} \)                                  |                                                                                                    |
| True Condition | Condition Positive                                                                           | True positive                                                                                            | False Negative                                                                                  | True Positive Rate (TPR), Sensitivity, Recall = \( \frac {\sum True Positive} {\sum Condition Positive} \) | False Negative Rate (FNR), Miss Rate = \( \frac {\sum False Negative} {\sum Condition Positive} \) |
| True Condition | Condition Negative                                                                           | False Positive (Type I Error)                                                                            | True Negative                                                                                   | False Positive Rate (FPR), Fall out = \(\frac {\sum False Positive} {\sum Condition Negative}\)            | True Negative Rate (TNR), Specifity (SPC) \(\frac {\sum True Negative} {\sum Condition Negative}\) |
|                | Accuracy (ACC) = \(\frac {\sum True Positive + \sum True Negative} {\sum Total Population}\) | Positive Predictive Value (PPV), Precision = \(\frac {\sum True Positive} {\sum Test Outcome Positive}\) | False Ommision Rate (FOR) = \(\frac {\sum False Negative} {\sum Test Outcome Negative}\)        | Positive Likelyhood ratio  = \( LR+ = \frac {TPR} {FPR} \)                                                 | Diagnostics Odds Ratio \(DOR = \frac {LDR+} {LDR-}\)                                               |
|                |                                                                                              | False Discovery Rate (FDR) = \(\frac {\sum False Positive} {\sum Test Outcome Positive}\)                | Negative Predictive Value = (NPV) = \(\frac {\sum True Negative} {\sum Test Outcome Negative}\) | Nagive Likelyhood ratio = \( LR- = \frac {FNR} {TNR} \)                                                    |                                                                                                    |

## Limitiation of Accuracy

- There are conditions in which accuracy alone is not a good metric to determine the validity of the alorith, thus weighted accuracy is a better metric to track the alogrithm on, this is the case for data sets which are highly unbalanaced
  - Instead data needs to be normalized, before it can be used
  
## ROC Curve 

- Receiver Operating Characteristc
  - Graphical approach for displaying the tradeoff between true positive rate (TPR) and false positive rate (FPR) of a classifier
  - TPR on y-axis and FPR on x-axis
  - The area under the graph represents the quality of the algorithm 
  
| TPR | FPR | Outcome                     |
| --- | --- | --------------------------- |
| 0   | 0   | Ever Prediction is Negative |
| 1   | 0   | Ideal                       |
| 1   | 1   | Ever Prediction is positive |

## Methods of Validation 
- Holdout 
  - Use 2/3 of training and 1/3 for testing 
- Corss-Validation 
  - Random subsampling
  - K-Fold Cross Validation 
  - Leave-one-out
- Stratified cross validation
  - Stratified 10-fold cross validation is often the best 
- Bootstrapping 
  - Sampling with replacements 
  - Oversampling vs undersampling 

## Stratified cross-validation

When dandomly slelecting training or test sets, ensure that class proportions are maintained in each selected set. 

1. Stratify instances by class 
2. Randomly select instance from each class. 
  
# Linear Regression
## Correlation (r)

- Linerar associaten between two variables
- Show how to determine both the nature and strength of relationship between two variables
- Correlation lies between  + 1 to -1
- Zero correlation indicates thaty there is no relationship between the variables
- Pearson correlation coeficient
  - Most familiar measure of dependence between two quentities
  
When the line perfectly fits the representation then we can consider the correlation to be positive, on the other hand, when the data can be considered to be close, but not perfectly matached the correlation can be considered to be -1, and the cases when no linear correlation can be drawn between the varibles. 

$$
 corr(X,Y) = \frac {cov(X,Y)} {\sigma_X \sigma_Y} = \frac {E[(X-)]} {\sigma_X \sigma_Y} = \frac {\sum {(x_i - \bar{x})}} {\sqrt{\sum{(x_i - \bar{x})} \sqrt{\sum{(y_1 - \bar{y})}}}}
$$

- How to represent the data as a vector/matrix
  - We assume a model:
     $$
     \bar{y} = b_0 + bX + \epsilon
     $$
  - where \(b_0\) abd b are the intercept and slope, knosn as coefficients or parameters, \(\epsilon \) is the error term (typically assume that \(\epsilon \sim  N(\mu, \sigma^2)\)
  - Include bias constant in the input vector 
    $$
    X \in \real^{n * (p+ 1)}, y \in \real^{p+1}, e \in \real^{n}
    $$ 

    $$
        y = X \cdot b + e  
    $$

## Ordinary Least Squares (OLS)

$$
  Y = Xb + e
$$
- Estimate the unkown parameters (b) on ;omear regression model
- Minimizing the sum of squares of the differences between the observed responses and the preicted by a liner function 
- Sum of Squared error : 
  $$
    \sum^n _{i=1} (y_i - x_i * b) ^2
  $$ 

## Optimization 
- Need to minimize the error:
  $$
  min J(b) = \sum^{n}_{i=1} {(y_i - x_i * b)^2}
  $$

  <h2> I REALLY HOPE ALL THIS MATH IS NOT ON EXAM!!!!!</h2>

## Linear regression with categorical cariables

- We assumed that all variables are continuous variables
- Categorical variables:
  - Oridanl variables - Encode data with continues values 
  - Nominal Values - Use dummy variables
  - For binary classication
    - encode class labels as y = {0,1} or {-1, 1}
    - Apply OLS
    - Check which class the prediction is closer to 
      - If class 1 is encoded to 1 and class 2 is -1.
        - class 1 if f(x) >= 0
        - clas2 2 if f(x) < 
    - Linear models are not optimized for classification 
  - Logistic Regression

# Optimization 

- Minimization: Cost/Loss Function (ML)
- Maximization: Profit


