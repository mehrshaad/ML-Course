## Data visualization

### 1. MNIST data set

+ **a:** Download a subset of MNIST dataset using one of the repositories/resources in the Internet.
+ **b:** Use scatter graph to show the distribution of the classes.
+ **c:** The pixel values are playing the role of features, so for each image of
size 28 × 28 there is a vector of size 784 elements. Please calculate
the a-priori probability for each feature value per class.
Linear Classification

## Linear Classification

### 2. Multiclass classification using linear classification

+ **a:** Consider the above multi-class classification which must be solved
using a binary classification technique. At first split the data set into
70% train and 30% test. The use one-versus-rest to classify all objects
in the train set. For example to classify 0 from the others there will
be one label (e.g., 0) for 0s and another label (e.g., 1) for the rest and
so on for other digits. Use linear classifier with Stochastic Gradient
Method to come up with the 10 classifiers.
+ **b:** Using the extracted 10 classifiers in the last part, predict the image
objects in the test set.
+ **c:** Calculate the accuracy of your classification scheme just for each
classifier.
+ **d:** Repeat the above steps for different ratio of train/set size wherein
80% is dedicated to train and 20% to test set respectively.
