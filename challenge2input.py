#Unit 1 Lesson 3 Challenge 2
import sqlite3 as lite
import pandas as pd
import sys

x = 0

cities = (('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA'))

weather = (('New York City', '2013', 'July', 'January', '62'),
  ('Boston', '2013', 'July', 'January', '59'),
  ('Chicago', '2013', 'July', 'January', '59'),
  ('Miami', '2013', 'August', 'January', '84'),
  ('Dallas', '2013', 'July', 'January', '77'),
  ('Seattle', '2013', 'July', 'January', '61'),
  ('Portland', '2013', 'July', 'December', '63'),
  ('San Francisco', '2013', 'September', 'December', '64'),
  ('Los Angeles', '2013', 'September', 'December', '75'))

month = ((1,'January'),(2,'February'),(3,'March'),(4,'April'),
  (5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December'))

con = lite.connect('getting_started.db')
rows = []
print("This script will show you which cities have an average warmest month of your choosing.")
while rows == []:
	with con:

		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS cities")
		cur.execute("CREATE TABLE cities(city TEXT, state TEXT)")
		cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
		cur.execute("DROP TABLE IF EXISTS weather")
		cur.execute("CREATE TABLE weather(city TEXT, year INT, warm_month TEXT, cold_month TEXT, average_high INT)")
		cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
		cur.execute("DROP TABLE IF EXISTS month")
		cur.execute("CREATE TABLE month(num INT, mon TEXT)")
		cur.executemany("INSERT INTO month VALUES(?,?)",month)
		
		response = 0
		while (response < 1 or response > 12):
			response = int(raw_input("Please Enter Month In Numeric Value: "))
			if (response < 1 or response > 12):
			  print("Error: Invalid Month")

		cur.execute("SELECT mon FROM month where num = ?", (response,))
		con.commit

		row1 = cur.fetchone()
		#print row1

		inp =''.join(row1)
		print("You entered the month: %s") %inp
	 
		cur.execute("SELECT weather.city, cities.state, year, warm_month, cold_month, average_high FROM weather JOIN cities ON weather.city = cities.city where warm_month = ?", (inp,))
		#con.commit

		rows = cur.fetchall()
		if rows == []:
			print("No Cities found with a Warm Month of %s") %inp

		
cols = [desc[0] for desc in cur.description]
df = pd.DataFrame(rows, columns=cols)
#df = df.set_index(['city'])

count = int(df['city'].count())

#print count

print "The cities that are the warmest in %s are:" %(inp)
for row in df.iterrows():
  index, data = row
  x += 1
  if x == count:
	print '%s' %(data['city'])        
  else:
	print '%s,' %(data['city'])