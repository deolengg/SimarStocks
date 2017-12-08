from django.db import connections

class graphify:
    c = connections['usaunem'].cursor()

    def __int__(self):
        pass

    def getdates(self):
        self.c.execute("SELECT strftime('%Y-%m-%d',monthlydates) FROM usaunemploymentavg")
        datelist = self.c.fetchall()
        datelist.reverse()
        datelist = [str(i).replace("(", "").replace(")", "").replace(",", "").replace("u'", "").replace("'", "") for i in datelist]
        return datelist

    def getthreemonthavg(self):
        self.c.execute("SELECT threemonthavg FROM usaunemploymentavg")
        threemontlist = self.c.fetchall()
        threemontlist.reverse()
        threemontlist = [str(i).replace("(", "").replace(")", "").replace("None", "0").replace(",", "") for i in threemontlist]
        return threemontlist

    def gettwelvemonthavg(self):
        self.c.execute("SELECT twelvemonthavg FROM usaunemploymentavg")
        twelvemontlist = self.c.fetchall()
        twelvemontlist.reverse()
        twelvemontlist = [str(i).replace("(", "").replace(")", "").replace("None", "0").replace(",", "") for i in twelvemontlist]
        return twelvemontlist

    def getthirtysixmonthavg(self):
        self.c.execute("SELECT thirtysixmonthavg FROM usaunemploymentavg")
        thirtysixmontlist = self.c.fetchall()
        thirtysixmontlist.reverse()
        thirtysixmontlist = [str(i).replace("(", "").replace(")", "").replace("None", "0").replace(",", "") for i in thirtysixmontlist]
        return thirtysixmontlist
