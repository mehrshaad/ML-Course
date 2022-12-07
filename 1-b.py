# Ali Dadashzadeh
# 1st practical question part (b)

# importing needed modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# loading the MNIST train dataset into a data frame
dataFrame = pd.read_csv("mnist_train.csv")

# grouping data by their label
groupData = dataFrame.groupby(dataFrame.label)

# creating colors list for each class
colors = ['b', 'c', 'y', 'm', 'r', 'g']

# creating a range of 28*28=784 for plot's X
plotX = range(785)

# iterating through the labels
for label in range(10):

    # getting the data of the current label (class)
    labelData = groupData.get_group(label)

    # iterating through the first 50 data of label's data
    # (it has been limited to 50 for speed increase)
    for data in range(50):

        # setting the data for scatter graph
        plt.scatter(plotX, labelData.iloc[data], c=colors[label % len(colors)])

    # setting the current graph's title
    plt.title(f'Class: {label}\nClose to continue...')

    # showing the plot of the current label
    plt.show()