import sqlite3 as lite
import pandas as pd

cities = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December', '100'),
                     ('Atlanta', 2013, 'July', 'January', '45'))

con = lite.connect('getting_started.db')

def print_result(city, state):
    print("The city with the warmest month is {0}, {1}.".format(city, state))


with con:
    cur = con.cursor()
    #set up cities and weather tables
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")
    cur.execute("CREATE TABLE cities (name text, state text)")
    cur.execute("INSERT INTO cities (name, state) VALUES ('New York City', 'NY'),('Boston', 'MA'),('Chicago', 'IL'),('Miami', 'FL'),('Dallas', 'TX'),('Seattle', 'WA'),('Portland', 'OR'),('San Francisco', 'CA'),('Los Angeles', 'CA')")
    cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
    cur.execute("INSERT INTO weather (city, year, warm_month, cold_month, average_high) VALUES ('New York City',2013,'July','January',62),('Boston',2013,'July','January',59),('Chicago',2013,'July','January',59),('Miami',2013,'August','January',84),('Dallas',2013,'July','January',77),('Seattle',2013,'July','January',61),('Portland',2013,'July','December',63),('San Francisco',2013,'September','December',64),('Los Angeles',2013,'September','December',75)")
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', '86')")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', '88')")
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
    
    #query data
    cur.execute("SELECT city, state, average_high FROM cities INNER JOIN weather ON name = city ORDER BY average_high DESC")

    #display query results
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)
    #filter for first row
    result_df = df[0:1]
    #get city and state values from dataframe
    city = result_df.iloc[0]['city']
    state = result_df.iloc[0]['state']
    #call funtion to output result
    print_result(city, state)