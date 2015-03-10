import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
from operator import itemgetter
import collections
import math

iris = pd.read_csv('iris.txt', header = None)


sepal_length =iris[0]
sepal_width = iris[1]
iristype = iris[4]

plt.scatter(sepal_length, sepal_width) #this works but I need to color code it by iris type
plt.show()



##iterate through the database and find the distance
##iterate through the database and find the distance
def KNN(k):
    distances = []	
    for plant in xrange(len(iris.index)):
        dist = math.sqrt((sepal_length[k]-sepal_length[plant])**2 + (sepal_width[k] - sepal_width[plant])**2) 
        distances.append([dist, iris.iat[plant , 4]]) #create a minilist of the distance and the row and the type, right now broke
        print [dist, iris.iat[plant , 4]]
##sort the points by distance
    sorted(distances, key=itemgetter(0)) #this doesn't seem to be sorting correctly
    distances = distances[1:] #drop the closest point which is the point itself
##pick a certain number of points, will always be ten right now but could modify the function
#to take two values and the second one could replace the 10
    neighbors  = []
    for row in xrange(10):
        neighbors.append(distances[1][1]) 
    votes = collections.Counter()
##determine the neighbors and take a vote
    for i in neighbors: #iterate through the neighbors
        votes[i] += 1
    print max(votes)

KNN(5)