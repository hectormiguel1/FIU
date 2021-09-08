# Table Of Contents
- [Introduction to Machine Learning](#class-8-31-:-introduction-to-machine-learning)
    - [Data Representation](##Data-representation)
    - [Types of Data](##Types-of-Data)
    - [Data Representation](##Data-Representation)
- [Class-9-2-:](#class-9-2-:)


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

## Data Representation
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

    
### *Missing Data can be a big problem in Machine Learning, and thus some cleaning of the data must of completed. If a sample has too many missing values, then the data can be discarded, otherwise, when few bits of data are missing, the values can be computed using something such ash Near Neighbor.*     


# Class 9-2: 

## Homework # 1 was issued
- Submission as word document or pdf
- Call code must be in single python file. 
- Violin plot must be provided, Density + Box plot. Plot values for each column.
- Use Pricipal Component Analsys
- Redece the dimensions. 
	- Categories:
		- Feature Selection: Determining subset of features from data. (Concrete Autoencoder)
		- Feature Extraction: Come up with new features. (Autoencoder)



# Class 9-7: Classificaion Problem 

## Learning Proccess in ML

Training Data -> Pre-processing -> Model Learning -> Model Testing <- Test Data 

Pre-proccesing 
- Missing value imputation 
- Noise Filtering 
- Feature selection:
  - Subset of (word) features (concrete autoencoder)
- Feature Extraction 
  - Come ups with new (hidden) features (Standard Autoencoder)
- Feature Scaling. 
  - Standarization
  - Normalization 
  - Min-Max Normalization 

Model Learning: 
- Classification 
  - Regression 
  - Clustering 

Model Testing:
   - Cross Validation 

