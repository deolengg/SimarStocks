from django.db import connections

import sqlite3

c = connections['usaunem'].cursor()


def create_base_table():
    c.execute('CREATE TABLE IF NOT EXISTS usaunemployment(monthlydates DATE , gvalue NUMERIC)')

def create_avg_table():
    c.execute('CREATE TABLE IF NOT EXISTS usaunemploymentavg( id INTEGER PRIMARY KEY AUTOINCREMENT,monthlydates VARCHAR , gvalue NUMERIC , threemonthavg NUMERIC ,twelvemonthavg NUMERIC ,thirtysixmonthavg NUMERIC )')

def clear_base_table():
    c.execute('DELETE FROM usaunemployment')
    c.execute('DROP TABLE usaunemployment')

def clear_avg_table():
    c.execute('DELETE FROM usaunemploymentavg')

def delete_avg_table():
    c.execute("DROP TABLE usaunemploymentavg")

def copy_data_by_desc():
    c.execute("INSERT INTO usaunemploymentavg (monthlydates,gvalue) SELECT Date,Value FROM usaunemployment ORDER BY Date DESC,Value DESC")

def close_everything():
    c.close()
    print('Connection Closed')
