import sqlite3

conn = sqlite3.connect('usaunem.db', timeout=10)
c = conn.cursor()

class tableStructure:

    def create_base_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS usaunemployment(monthlydates DATE , gvalue NUMERIC)')

    def create_avg_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS usaunemploymentavg( id INTEGER PRIMARY KEY AUTOINCREMENT,monthlydates DATE , gvalue NUMERIC , threemonthavg NUMERIC ,twelvemonthavg NUMERIC ,thirtysixmonthavg NUMERIC )')

    def clear_base_table(self):
        self.c.execute('DELETE FROM usaunemployment')

    def clear_avg_table(self):
        self.c.execute('DELETE FROM usaunemploymentavg')

    def delete_avg_table(self):
        self.c.execute("DROP TABLE usaunemploymentavg")

    def copy_data_by_desc(self):
        self.c.execute("INSERT INTO usaunemploymentavg (monthlydates,gvalue) SELECT Date,Value FROM usaunemployment ORDER BY Date DESC,Value DESC")

    def copy_data_by_desc_graph_table(self):
        self.c.execute("INSERT INTO graphtable (monthlydates,gvalue,threemonthavg,twelvemonthavg,thirtysixmonthavg) SELECT monthlydates,gvalue,threemonthavg,twelvemonthavg,thirtysixmonthavg FROM usaunemploymentavg ORDER BY monthlydates DESC,gvalue DESC, threemonthavg DESC,twelvemonthavg DESC,thirtysixmonthavg DESC ")

    def close_everything(self):
        self.conn.commit()
        self.c.close()
        self.conn.close()
        print('Connection Closed')

