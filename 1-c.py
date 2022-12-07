# Ali Dadashzadeh
# 1st practical question part (c)

# importing needed modules
import numpy as np
import pandas as pd

# creating a data frame from the MNIST train dataset
dataFrame = pd.read_csv("mnist_train.csv")

# grouping data by their label from 0 to 9
groupedData = dataFrame.groupby(dataFrame.label)

# creating empty dictionaries to append the output data
output = [[{} for j in range(785)] for i in range(10)]

# iterates trough the labels (0 to 9)
for label in range(10):

    # the data of the current label
    labelData = groupedData.get_group(label)

    # length of the current label data
    length = len(labelData)

    # iterates through the 28*28=784 pixels
    for pixel in range(785):

        # exploiting the pixel data
        pixelData = labelData.iloc[:, pixel].value_counts()

        # iterates features for every pixel
        for x, y in pixelData.items():

            # appending a-priori probability of the current feature, to output
            output[label][pixel][x] = y / length

# printing the output data (it's huge!)
print(output)