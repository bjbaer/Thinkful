import requests
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as lite
# a package with datetime objects
import time
# a package for parsing a string into a Python datetime object
from dateutil.parser import parse 
import collections
import sched, time
import datetime

r = requests.get('http://www.citibikenyc.com/stations/json')
len(r.json()['stationBeanList'])

key_list = [] #unique list of keys for each station listing
for station in r.json()['stationBeanList']:
    for k in station.keys():
        if k not in key_list:
            key_list.append(k)
r.json()['stationBeanList'][0]
df = json_normalize(r.json()['stationBeanList'])


#storing the data in sqlite
#store the unchanging data
con = lite.connect('citi_bike.db')
cur = con.cursor()
#drop the tables so you can rerun
cur.execute('''DROP TABLE citibike_reference''')
cur.execute('''DROP TABLE available_bikes''')

with con:
    cur.execute('CREATE TABLE citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT )')
#a prepared SQL statement we're going to execute over and over again
sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

#for loop to populate values in the database
with con:
    for station in r.json()['stationBeanList']:
        #id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location)
        cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))

#extract the column from the DataFrame and put them into a list
station_ids = df['id'].tolist() 

#add the '_' to the station name and also add the data type for SQLite
station_ids = ['_' + str(x) + ' INT' for x in station_ids]

#create the table
#in this case, we're concatentating the string and joining all the station ids (now with '_' and 'INT' added)
with con:
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")



count = 0
starttime=time.time()

while count < 2: # will run the below code 60 times
	r = requests.get('http://www.citibikenyc.com/stations/json')
	exec_time = parse(r.json())['executionTime']
	cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%Y-%m-%dT%H:%M:%S'),))
	con.commit()

	id_bikes = collections.defaultdict(int)
	for station in r.json()['stationBeanList']:
		id_bikes[station['id']] = station['availableBikes']
	#iterate through the defaultdict to update the values in the database
	with con:
		for k, v in id_bikes.iteritems():
			cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + str((exec_time - datetime.datetime(1970,1,1)).total_seconds()) + ";")
	print "tick " + str(count)
	time.sleep(60.0 - ((time.time() - starttime) % 60.0))
	count +=1 # increment count 

