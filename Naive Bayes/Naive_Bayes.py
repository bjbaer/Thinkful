import pandas as pd
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
#Remove the ' from the column names and sex by just removing all the ', may not be best practice
with open('ideal_weight.csv', 'r') as infile, open('clean_weight.csv', 'w') as outfile:
    temp = infile.read().replace("'", "")
  
    outfile.write(temp)

df = pd.read_csv('clean_weight.csv')

df['Male'] = (df['sex'] == 'Male')


print df['Male'].value_counts() #How many males vs females
train_features = df[['actual', 'ideal', 'diff']]
train_labels = df['sex']

clf = GaussianNB()
clf.fit(train_features, train_labels)
#clf.predict([4.8, 4.2])

accuracy = clf.score(train_features, train_labels)
print accuracy


print clf.predict([145, 160, -15])

print clf.predict([160, 145, 15])