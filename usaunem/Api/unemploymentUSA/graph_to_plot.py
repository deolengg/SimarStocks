import sqlite3

conn = sqlite3.connect('usaunem.db')
c = conn.cursor()

def getdates():
    c.execute("SELECT strftime('%Y-%m-%d', monthlydates) FROM usaunemploymentavg")
    datelist = c.fetchall()
    datelist.reverse()
    return datelist

def getthreemonthavg():
    c.execute("SELECT threemonthavg FROM usaunemploymentavg")
    threemontlist = c.fetchall()
    threemontlist.revere()
    return threemontlist

def gettwelvemonthavg():
    c.execute("SELECT twelvemonthavg FROM usaunemploymentavg")
    twelvemontlist = c.fetchall()
    twelvemontlist.reverse()
    return twelvemontlist

def getthirtysixmonthavg():
    c.execute("SELECT thirtysixmonthavg FROM usaunemploymentavg")
    thirtysixmontlist = c.fetchall()
    thirtysixmontlist.reverse()
    return thirtysixmontlist
