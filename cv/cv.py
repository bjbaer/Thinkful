import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import cross_validation 
from sklearn import datasets
iris = datasets.load_iris()
from sklearn.lda import LDA
from sklearn import svm
from sklearn import metrics

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = .4)

print len(X_train)
print len(X_test)

#train the SVM on the train
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

#Find it's score on the test
clf.score(X_test, y_test)

clf = svm.SVC(kernel='linear')
clf.fit(X, y)
print clf.score(X, y)
#The score is higher here, which makes sense

scores = cross_validation.cross_val_score(clf, iris.data, iris.target, cv=5)

print scores

print("Accuracy: %0.2f (std dev %0.2f)" % (scores.mean(), scores.std()))

scores = cross_validation.cross_val_score(clf, iris.data, iris.target, cv=5, scoring='f1')
print scores
print("Accuracy: %0.2f (std dev %0.2f)" % (scores.mean(), scores.std()))
#f1 is very close, same number of flowers for each of the three types, so this makes sense