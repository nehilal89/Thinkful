"""Working with Databases Challenge"""

import sqlite3 as lite

con = lite.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')
	data = cur.fetchone()
	print("SQLite version: %s" % data)

"""removing the previously created tables"""

import sqlite3 as lite

con = lite.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("DROP TABLE IF EXISTS weather")

"""creating new tables cities and weather"""
import sqlite3 as lite

con = lite.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.execute('''CREATE TABLE cities(name text, state text)''')
	cur.execute('''CREATE TABLE weather(City text, year integer, warm_month text, cold_month text, average_high integer)''')

"""inserting values into cities"""

import sqlite3 as lite

con = lite.connect('getting_started.db')

with con:

	cur = con.cursor()
	cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
	cur.execute("INSERT INTO cities VALUES('New York City', 'NY')")
	cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
	cur.execute("INSERT INTO cities VALUES('Boston', 'MA')")
	cur.execute("INSERT INTO cities VALUES('Chicago', 'IL')")
	cur.execute("INSERT INTO cities VALUES('Miami', 'FL')")
	cur.execute("INSERT INTO cities VALUES('Dallas', 'TX')")
	cur.execute("INSERT INTO cities VALUES('Seattle', 'WA')")
	cur.execute("INSERT INTO cities VALUES('Portland', 'OR')")
	cur.execute("INSERT INTO cities VALUES('San Francisco', 'CA')")
	cur.execute("INSERT INTO cities VALUES('Los Angeles', 'CA')")

"""inserting values into weather"""

import sqlite3 as lite

weather = (('Las Vegas', 2013, 'July', 'December', 70),
	('Atlanta', 2013, 'July', 'January', 80),
	('New york City', 2013, 'july', 'january', 62),
	('chicago', 2013, 'july', 'january', 59),
	('boston', 2013, 'july', 'january', 59),
	('miami', 2013, 'august', 'january', 84),
	('dallas', 2013, 'july', 'january', 77),
	('seattle', 2013, 'july', 'january', 61),
	('portland', 2013, 'july', 'december', 63),
	('san francisco', 2013, 'september', 'december', 64),
	('los angeles', 2013, 'september', 'december', 75))


con = lite.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

"""Join the data together"""
import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')

with con:

	cur = con.cursor()
	cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON name = city")

	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns=cols)
	














