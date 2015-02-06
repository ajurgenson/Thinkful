#Unit 1 Lesson 3 Challenge 1
import sqlite3 as lite
import pandas as pd

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

con = lite.connect('getting_started.db')

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("CREATE TABLE cities(city TEXT, state TEXT)")
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.execute("DROP TABLE IF EXISTS weather")
    cur.execute("CREATE TABLE weather(city TEXT, year INT, warm_month TEXT, cold_month TEXT, average_high INT)")
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
    cur.execute("SELECT weather.city, cities.state, year, warm_month, cold_month, average_high FROM weather JOIN cities ON weather.city = cities.city where warm_month = 'July'")

    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)
    #df = df.set_index(['city'])

    count = int(df['city'].count())

    #print count

    print "The cities that are the warmest in July are:" 
    for row in df.iterrows():
      index, data = row
      x += 1
      if x == count:
        print '%s' %(data['city'])        
      else:
        print '%s,' %(data['city'])