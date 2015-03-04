from bs4 import BeautifulSoup
import requests
import sqlite3 as lite
import pandas as pd
import numpy as np
import csv
import pandas.io.sql as psql
import math
import statsmodels.formula.api as sm
from pandas.stats.api import ols

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)

soup = BeautifulSoup(r.content)
souper = soup('table')[6] #take the table where the data of interest is


#repeat the previous but using tr, which is the next leel of tag
#for row in souper('tr'):
#    print row
#doing this I identified that the tr at index 3 was what I was interest in
souperer = souper('tr')[3] #saving the data in a new variable
#souperer('td')[12] #this is afghanistan
list = []
for row in souperer('td'):
    list.append(row)

soupest = souperer('tr') # 4 and beyond are the countries
#from each of the tr's we are looking for the 0th, 4th, 7th, and 10th values
test = soupest[4]
countries = []
total = []
men = []
women = []
everything = []
test('td')
for i in soupest[4:]:
        countries.append((i('td')[0]).get_text("|"))
        total.append(int((i('td')[4]).get_text("|")))
        men.append(int((i('td')[7]).get_text("|")))
        women.append(int((i('td')[10]).get_text("|")))

index = np.arange(len(soupest[4:])) # array of numbers for the number of samples
d = {'Country name': countries, 'Men': men, 'Women': women, 'Avg': total} #make a dictionary, each column is a key and the list is the value
df = pd.DataFrame(data = d, index = index)
#df.describe()
con = lite.connect('education.db')
cur = con.cursor()
with con:
	cur.execute('CREATE TABLE gdp ( country_name str, _1999 INT, _2000 INT, _2001 INT, _2002 INT, _2003 INT, _2004 INT, _2005 INT, _2006 INT, _2007 INT, _2008 INT, _2009 INT, _2010 INT)')

with open('ny.gdp.mktp.cd_Indicator_en_csv_v2.csv','rU') as inputFile:
    next(inputFile) # skip the first two lines
    next(inputFile)
    header = next(inputFile)
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        with con:
            cur.execute('INSERT INTO gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[42:-6]) + '");')


con = lite.connect("education.db")
dftwo = pd.read_sql("SELECT * FROM gdp", con)

con.close()

#perform log transform
for col in dftwo.columns:
	if type(i) == float:
		for i in col[1:]:
			i = math.log(i)


dfthree = pd.merge(df, dftwo, how = 'left', left_on = 'Country name', right_on = 'country_name')

#dfthree['avg_gdp'] = df['_1999', '_2000', '_2001', '_2002', '_2003', '_2004', '_2005', '_2006', '_2007', '_2008', '_2009', '_2010'].mean()
result = ols(y = df['Avg'], x = df['_2010'])
print result