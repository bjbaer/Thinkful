import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import datasets
iris = datasets.load_iris()
from sklearn.lda import LDA
import math
from operator import itemgetter
import collections

X = iris.data
y = iris.target
target_names = iris.target_names

pca = PCA(n_components = 2)
X_r = pca.fit(X).transform(X)

print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))

#PDC plotting
plt.figure()
for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], c=c, label=target_name)
plt.legend()
plt.title('PCA of IRIS dataset')
plt.show()

#LDA
lda = LDA(n_components=2)
X_r2 = lda.fit(X, y).transform(X)

plt.figure()
for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], c=c, label=target_name)
plt.legend()
plt.title('LDA of IRIS dataset')

plt.show()

def KNN(idx, k, x, y):
    distances = []	
    for plant in xrange(len(iris.data)):
        dist = math.sqrt((x[idx]-x[plant])**2 + (y[idx] - y[plant])**2) 
        distances.append([dist, iris.target[plant]]) #create a minilist of the distance and the row and the type, right now broke
        #print [dist, iris.iat[plant , 4]] #check to make sure it is working
    #sort the points by distance
    distances = sorted(distances, key=itemgetter(0)) #this doesn't seem to be sorting correctly
    distances = distances[1:] #drop the closest point which is the point itself
    #pick a certain number of points, will always be ten right now but could modify the function
    #to take two values and the second one could replace the 10
    neighbors  = []
    for row in xrange(k):
        neighbors.append(distances[row][1]) 
    votes = collections.Counter()
    #determine the neighbors and take a vote
    for i in neighbors: #iterate through the neighbors
        votes[i] += 1
    print max(votes)

KNN(5, 10, X_r[:,0], X_r[:,1])
KNN(132, 10, X_r2[:,0], X_r2[:,1])
