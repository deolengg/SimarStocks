import sqlite3

conn = sqlite3.connect('usaunem.db')
c = conn.cursor()

def create_base_table():
    c.execute('CREATE TABLE IF NOT EXISTS usaunemployment(monthlydates DATE , gvalue NUMERIC)')

def create_avg_table():
    c.execute('CREATE TABLE IF NOT EXISTS usaunemploymentavg(monthlydates DATE , gvalue NUMERIC , threemonthavg NUMERIC ,twelvemonthavg NUMERIC ,thirtysixmonthavg NUMERIC )')


def clear_base_table():
    c.execute('DELETE FROM usaunemployment')

def clear_avg_table():
    c.execute('DELETE FROM usaunemploymentavg')



