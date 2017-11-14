import sqlite3

conn = sqlite3.connect('usaunem.db')
c = conn.cursor()

def copy_data_by_desc():
    c.execute("INSERT INTO usaunemploymentavg (monthlydates,gvalue) SELECT * FROM usaunemployment ORDER BY Date DESC,Value DESC")
    conn.commit()
    c.close()
    conn.close()

copy_data_by_desc()

def calculate_avg(value):
    count = c.execute("SELECT COUNT (monthlydates) FROM usaunemploymentavg")
    last_count = count - value
