import csv
import urllib2
import pandas as pd
import scipy
from scipy.cluster.vq import kmeans, vq,  whiten
import numpy as np
from pylab import plot,show

#read in the data from un.csv as a pandas dataframe
df = pd.read_csv('un.csv', header=0, low_memory=False)

len(df.index)
#There are 207 rows in the csv

df.info()
#look at the non nulls

#Create the new variables based lifeMale, lifeFemale, infantMorality, and GDPperCapita, make them numpy arrays
lifeMale = df['lifeMale'].values

#lifeMale = lifeMale[(np.nonzero(lifeMale))]
lifeFemale = df['lifeFemale'].values
#lifeFemale = lifeFemale[(np.nonzero(lifeFemale))]
infantMortality = df['infantMortality'].values
#infantMortality = infantMortality[(np.nonzero(infantMortality))]
GDPperCapita = df['GDPperCapita'].values
#GDPperCapita = GDPperCapita[(np.nonzero(GDPperCapita))]
gdpmale = {'gdp': GDPperCapita, 'lifemale': lifeMale}
dfgm = pd.DataFrame(gdpmale)
gdpfemale = {'gdp': GDPperCapita, 'lifefemale': lifeFemale}
dfgf = pd.DataFrame(gdpfemale)
gdpinfmort = {'gdp': GDPperCapita, 'InfantMortality': infantMortality}
dfgim = pd.DataFrame(gdpinfmort)

#turn the dataframes into arrays, gm = gdp male, gf = gdp female, gim = gdp infant mortality
dfgm = dfgm.values
dfgf = dfgf.values
dfgim = dfgim.values


#Male lifetime and GDP


avg_dist_male = []
for i in range(1,11):
    centroids1,dist1 = kmeans(dfgm,i)
    idx1,idxdist1 = vq(dfgm,centroids1)
    avg_dist = np.mean(idxdist1)
    avg_dist_male.append(avg_dist)

plot(range(1,11), avg_dist_male)
show()

#Female lifetime and GDP

avg_dist_female = []
for i in range(1,11):
    centroids1,dist1 = kmeans(dfgf,i)
    idx1,idxdist1 = vq(dfgf,centroids1)
    avg_dist = np.mean(idxdist1)
    avg_dist_female.append(avg_dist)

plot(range(1,11), avg_dist_female)
show()

#infant mortality and GDP

avg_dist_infant = []
for i in range(1,11):
    centroids1,dist1 = kmeans(dfgim,i)
    idx1,idxdist1 = vq(dfgim,centroids1)
    avg_dist = np.mean(idxdist1)
    avg_dist_infant.append(avg_dist)

plot(range(1,11), avg_dist_infant)
show()

#Infant Mortality and GDP, sample k means, didn't include this for all of them because it would be to many
centroids1,dist1 = kmeans(dfgim,2)
idx1,idxdist1 = vq(dfgim,centroids1)

plot(dfgim[idx1==0,0],dfgim[idx1==0,1],'ob',
     dfgim[idx1==1,0],dfgim[idx1==1,1],'or')
plot(centroids1[:,0],centroids1[:,1],'sg',markersize=8)
show()

