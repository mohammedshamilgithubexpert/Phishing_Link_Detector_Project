# Purpose - This file is used to validate the data.

import numpy as np

from sklearn.metrics import accuracy_score, classification_report

import joblib

# Load the classifier from the .pkl file
clf = joblib.load('classifier.pkl')

labels = []
data_file = open('dataset/Testing Dataset.arff').read()
data_list = data_file.split('\r\n')
data = np.array(data_list)
data1 = [i.split(',') for i in data]
data1 = data1[0:-1]
for i in data1:
    labels.append(i[30])
data1 = np.array(data1)
features = data1[:, :-1]
# Choose only the relevant features from the data set.
features = features[:, [0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]]
# Convert the features to float
features = features.astype(float)
# Predict the labels
predicted = clf.predict(features)
# Calculate the accuracy
accuracy = accuracy_score(labels, predicted)
print("Accuracy: ", accuracy)
print("Classification Report: \n", classification_report(labels, predicted))
