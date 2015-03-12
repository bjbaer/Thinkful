import pandas as pd
import numpy as np
import csv
import math
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as skm
import pylab as pl


with open('C:/Thinkful/Random Forests/UCI_HAR/features.txt', 'r') as infile, open('C:/Thinkful/Random Forests/UCI_HAR/featuresclean.txt', 'w') as outfile:
    temp = infile.read().replace("()", "")
    temp2 = temp.replace("-", "")
    temp3 = temp2.replace(',', '_')
    temp4 = temp3.replace('Body', "")
    temp5 = temp4.replace('Mag', '')
    temp6 = temp5.replace('mean', 'Mean')
    temp7 = temp6.replace('std', 'STD')
     
    outfile.write(temp3)

train = pd.read_csv('samtrain.csv')
values = pd.read_csv('samval.csv')
test = pd.read_csv('samtest.csv')
data = pd.read_csv('samsungdata.csv')
minumum = pd.read_csv('samsungmin.csv')



forest = RandomForestClassifier(n_estimators=500, oob_score=True)
train_data = train[train.columns[1:-2]]
train_truth = train['activity']
model = forest.fit(train_data, train_truth)

forest.oob_score

importance = enumerate(forest.feature_importances_)
cols = train.columns
[(values,cols[i]) for (i,value) in importance if value > .04]

val_data = values[values.columns[1:-2]]
val_truth = values['activity']
val_pred = forest.predict(val_data)

test_data = test[test.columns[1:-2]]
test_truth = test['activity']
test_pred = forest.predict(test_data)

print "validation score = %f" % (forest.score(val_data, val_truth))
print "test score = %f" % (forest.score(test_data, test_truth))

test_cm = skm.confusion_matrix(test_truth, test_pred)

pl.matshow(test_cm)
pl.title('Confusion matrix for test data')
pl.colorbar()
pl.show()

print "Accuracy = %f" %(skm.accuracy_score(test_truth,test_pred))
print("Precision = %f" %(skm.precision_score(test_truth,test_pred)))
print("Recall = %f" %(skm.recall_score(test_truth,test_pred)))
print("F1 score = %f" %(skm.f1_score(test_truth,test_pred)))



#need to combine the 4 text files, x-train y-train subject-train and cleanfeatures, can do it in pandas, or in sql if thats what you want
#for random forest, look in package sklearn