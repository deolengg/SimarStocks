import sqlite3

conn = sqlite3.connect('usaunem.db')
c = conn.cursor()

def create_base_table():
    c.execute('CREATE TABLE IF NOT EXISTS usaunemployment(monthlydates DATE , gvalue NUMERIC)')

def create_avg_table():
    c.execute('CREATE TABLE IF NOT EXISTS usaunemploymentavg( id INTEGER PRIMARY KEY AUTOINCREMENT,monthlydates DATE , gvalue NUMERIC , threemonthavg NUMERIC ,twelvemonthavg NUMERIC ,thirtysixmonthavg NUMERIC )')
    conn.commit()

def clear_base_table():
    c.execute('DELETE FROM usaunemployment')
    conn.commit()

def clear_avg_table():
    c.execute('DELETE FROM usaunemploymentavg')
    conn.commit()

def delete_avg_table():
    clear_avg_table()
    c.execute("DROP TABLE usaunemploymentavg")

def close_everything():
    conn.commit()
    c.close()
    conn.close()

def copy_data_by_desc():
    c.execute("INSERT INTO usaunemploymentavg (monthlydates,gvalue) SELECT Date,Value FROM usaunemployment ORDER BY Date DESC,Value DESC")
    conn.commit()

clear_avg_table()
delete_avg_table()
create_avg_table()
copy_data_by_desc()
