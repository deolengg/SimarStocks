import sqlite3

conn = sqlite3.connect('usaunem.db')
c = conn.cursor()

def create_base_table():
    c.execute('CREATE TABLE IF NOT EXISTS usaunemployment(monthlydates DATE , gvalue NUMERIC)')

def create_avg_table():
    c.execute('CREATE TABLE IF NOT EXISTS usaunemploymentavg(monthlydates DATE , gvalue NUMERIC , threemonthavg NUMERIC ,twelvemonthavg NUMERIC ,thirtysixmonthavg NUMERIC )')

def create_temp_table():
    c.execute('create table IF NOT EXISTS temptable (monthlydates DATE, tvalue NUMERIC)')

def clear_base_table():
    c.execute('DELETE FROM usaunemployment')
    conn.commit()

def clear_avg_table():
    c.execute('DELETE FROM usaunemploymentavg')
    conn.commit()


create_temp_table()