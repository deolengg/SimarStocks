from django.db import connections

class tablestructure:

    c = connections['usaunem'].cursor()


    def create_base_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS usaunemployment(monthlydates DATE , gvalue NUMERIC)')

    def create_avg_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS usaunemploymentavg( id INTEGER PRIMARY KEY AUTOINCREMENT,monthlydates VARCHAR , gvalue NUMERIC , threemonthavg NUMERIC ,twelvemonthavg NUMERIC ,thirtysixmonthavg NUMERIC )')

    def clear_base_table(self):
        self.c.execute('DELETE FROM usaunemployment')
        self.c.execute('DROP TABLE usaunemployment')

    def clear_avg_table(self):
        self.c.execute('DELETE FROM usaunemploymentavg')

    def delete_avg_table(self):
        self.c.execute("DROP TABLE usaunemploymentavg")

    def copy_data_by_desc(self):
        self.c.execute("INSERT INTO usaunemploymentavg (monthlydates,gvalue) SELECT Date,Value FROM usaunemployment ORDER BY Date DESC,Value DESC")

    def close_everything(self):
        self.c.close()
        print('Connection Closed')
