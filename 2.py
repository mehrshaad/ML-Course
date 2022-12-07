# Ali Dadashzadeh
# 2nd practical question

# importing needed modules
import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.linear_model import SGDClassifier

# creating 2 data frames of MNIST test and train data
trainData = pd.read_csv("mnist_train.csv")
testData = pd.read_csv("mnist_test.csv")

# merging test and train data for division
dataFrame = pd.concat([trainData, testData])

# data division ratio (70-30)
# (change 70 to 80 for 80-20 mode)
ratio = 70
dataDivide = len(dataFrame) * ratio // 100

# setting labels and data
x1 = dataFrame.iloc[:, 1:].values.tolist()
x2 = sk.utils.validation.column_or_1d(dataFrame.iloc[:, :1].values.tolist())

# dividing data according to our ratio
x1Train, x1Test, x2Train, x2Test = x1[:dataDivide], x1[
    dataDivide:], x2[:dataDivide], x2[dataDivide:]

# defining the Stochastic Gradient Descent (SGD) Classifier
classifier = SGDClassifier(random_state=60)

# training the SGD Classifier
classifier.fit(x1Train, x2Train)

# testing the Classifier with our test data
result = sk.metrics.classification_report(x2Test, classifier.predict(x1Test))

# printing the result
print(result)