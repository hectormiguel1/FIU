# Table of Contents
- [Table of Contents](#table-of-contents)
- [Algorithms](#algorithms)
  - [PCA: Principal Component Analysis](#pca-principal-component-analysis)
    - [Standardization](#standardization)
    - [Covariance Matrix](#covariance-matrix)
    - [Compute Eigenvectors and Eigenvalues](#compute-eigenvectors-and-eigenvalues)
    - [Feature Vector](#feature-vector)
    - [Recast Data](#recast-data)
  - [t-Distributed Stochastic Neighbor Embedding (tSNE):](#t-distributed-stochastic-neighbor-embedding-tsne)
- [Works Cited](#works-cited)


# Algorithms 

For the first homework, there were several algorithms used to be able to extract or learn new information from the data set provided, both the [MNIST](https://en.wikipedia.org/wiki/MNIST_database) data and the [housing training](https://fiu.instructure.com/courses/109798/files/18124455?wrap=1) data set. The two main algorithms used where the PCA (Principal Component Analysis) and tSNE (t-Distributed Stochastic Neighbor Embedding) 

## PCA: Principal Component Analysis 
Principal Component Analysis is an unsupervised learning algorithm used to reduce the number of dimensions (columns) used in machine learning. It uses a statical approach to attempt to reduce the number of features in the data set while keeping as much relevant information as possible. There are several steps involved in principal component analysis, these are as fallow: 

### Standardization
In this stage the contentious values are placed in the same scale, making sure that each value contributes equally to the overall analysis. The particular reason why performing standardization is that algorithms like PCA are quite sensitive to variances in the data, data with large ranges will dominate over the data with smaller ranges, this will lead to biased results from the algorithm. Mathematically this is accomplished by subtracting the mean and dividing by the standard divination for each value of each variable. 
### Covariance Matrix
In this step we aim to understand how variables in the data set are varying from the mean with respect to each other. In other words, to see if there is any relationship between them; variables can at times be very correlated in such a way they they contain redundant information. In order to identify these relationships, we compute the covariance matrix. 

The covariance matrix is a *p* x *p* symmetrical matrix containing all the possible pairs in the initial data set. A few bits of information can be extracted from the matrix by fallowing some rules. 

Rules:
1. Convergence(a,a) = Variable(a)
2. Convergence(a,b) = Convergence(b,a) (*commutative*)

This means that our convergence matrix is perfectly symmetrical through the diagonal. 

### Compute Eigenvectors and Eigenvalues
_Definitions_: 
- _Eigenvector_: Special set of vectors associated with a linear system of equations, also known as characteristics vectors.  
- _Eigenvalues_: Special set of scalers associated with a liner system of equations, also known as characteristic roots or characteristic values. 

Eigenvectors come in pairs, for each one there is an accompanying Eigenvalue, this number denotes the number of dimensions in the data. The eigenvectors in the convergence matrix actually denotes the axes where there is the most variance and by extensions the most information,  we call these the principal components, after we have all these eigenvectors, we can then rank them to find the vectors with the most significance. 

### Feature Vector
After we have ranked the eigenvectors, we can select that which contains the most information of them all. Usually by this point in the process, the most information is contained on the first vector, and the fallowing contain further diminishing data. 

### Recast Data
After the feature vector/s was selected from the step above, the entire data set can no be represented in the principal components axis. 




## t-Distributed Stochastic Neighbor Embedding (tSNE): 


# Works Cited
These websites were essential in understanding how the algorithms used in the project worked and to gain a deep understanding. 

1. [Step By Step PCA](https://builtin.com/data-science/step-step-explanation-principal-component-analysis)
2. [Eigenvector & Eigenvalues Definitions](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwicuIPyufDyAhXPSzABHWbLDAsQFnoECA8QAw&url=https%3A%2F%2Fmathworld.wolfram.com%2FEigenvector.html&usg=AOvVaw1d1iN4NCLrk3Rp4M1hGLqS)