from sklearn import datasets
import matplotlib.pyplot as plt
iris = datasets.load_iris()
from sklearn import svm
import numpy as np

plt.scatter(iris.data[:, 1], iris.data[:, 2], c=iris.target)
plt.xlabel(iris.feature_names[1])
plt.ylabel(iris.feature_names[2])
plt.show()

#petal length and sepal wideth
plt.scatter(iris.data[0:100, 1], iris.data[0:100, 2], c=iris.target[0:100])
plt.xlabel(iris.feature_names[1])
plt.ylabel(iris.feature_names[2])
plt.show()

svc = svm.SVC(kernel='linear')
X = iris.data[0:100, 1:3]
y = iris.target[0:100]
svc.fit(X, y)

#Adapted from https://github.com/jakevdp/sklearn_scipy2013
from matplotlib.colors import ListedColormap
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

def plot_estimator(estimator, X, y):
    estimator.fit(X, y)
    x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
    y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = estimator.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.axis('tight')
    plt.axis('off')
    plt.tight_layout()

plot_estimator(svc, X, y)
plt.show()

def irissvm(flower1, flower2, feature1, feature2):
    svc = svm.SVC(kernel='linear')
    X = iris.data[flower1:flower2, feature1:feature2]
    y = iris.target[flower1:flower2]
    svc.fit(X, y)
    plot_estimator(svc, X, y)
    plt.show()

irissvm(0, 100, 0, 2)
irissvm(0, 100, 1, 3)
irissvm(0, 100, 2, 4)
irissvm(50, 150, 0, 2)
irissvm(50, 150, 1, 3)
irissvm(50, 150, 2, 4)

