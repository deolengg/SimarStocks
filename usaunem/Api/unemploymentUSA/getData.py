import quandl as quandl
import sqlite3

conn = sqlite3.connect('usaunem.db')
c = conn.cursor()

api = 'FRED/UNEMPLOY'
authkey = open('APIKEY.txt', 'r').read()


def get_data():
    from_the_start = "1949-01-01"
    datafromthestart = quandl.get(api, authtoken=authkey, start_date=from_the_start)
    return datafromthestart

def data_entry():
    table1.to_sql('usaunemployment', conn, if_exists='replace', dtype={'Date': 'DATE', 'Value': 'FLOAT'})
    conn.commit()
    c.close()
    conn.close()

table1 = get_data()
data_entry()
