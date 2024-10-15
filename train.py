# Purpose - This file is used to create a classifier and store it in a .pkl file. You can modify the contents of this
# file to create your own version of the classifier.

import numpy as np

from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn import metrics

import joblib

labels = []
data_file = open('dataset/Training Dataset.arff').read()
data_list = data_file.split('\r\n')
data = np.array(data_list)
data1 = [i.split(',') for i in data]
data1 = data1[0:-1]
for i in data1:
    labels.append(i[30])
data1 = np.array(data1)
features = data1[:, :-1]
# Choose only the relevant features from the data set.
features = features[:, [0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12,  13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]]
# Convert the features to float
features = features.astype(float)
# Create a random forest classifier
clf = RandomForestClassifier(n_estimators=100)
# Train the classifier
clf.fit(features, labels)
# Save the classifier to a .pkl file
joblib.dump(clf, 'classifier.pkl')
