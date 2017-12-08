import numpy as np
from django.db import connections


c = connections['usaunem'].cursor()
for_twelve_months =12
for_thirty_six_months=36

def close_everything():
    c.close()

def counting_till(value):
    last_count = c.execute("SELECT COUNT (monthlydates) FROM usaunemploymentavg")
    count_till = last_count.fetchone()[0] - value
    print('checkpoint 2')
    return count_till #returns till which row we have to calculate mean

def get_three_values(counter):
    print('checkpoint 3')
    aa = counter
    ab = counter + 1
    ac = counter + 2
    ad = counter + 3
    ae = counter + 4
    af = counter + 5
    ag = counter + 6
    ah = counter + 7
    ai = counter + 8
    aj = counter + 9
    ak = counter + 10
    al = counter + 11

    mylist = []
    c.execute("SELECT gvalue FROM usaunemploymentavg WHERE id IN (?,?,?,?,?,?,?,?,?,?,?,?)",
              (aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al))
    mylist = c.fetchall()
    return mylist



def do_mean_pass_mean_value_for_id(counter_id, mylist=[]):
    print("checkpoint 4")
    avg_num = np.mean(mylist)
    mean = np.around(avg_num, decimals=3)
    print(mylist)
    print(counter_id)
    c.execute("UPDATE usaunemploymentavg SET twelvemonthavg = (?) WHERE id = (?)", (mean, counter_id))



def populate_avg_column_for_twelve(value):
    print('checkpoint 1')
    count_till = counting_till(value)
    print(count_till)
    counter = 0
    while (count_till > counter): #823 == 823 loop will work
        counter = counter + 1
        xlist = get_three_values(counter)
        do_mean_pass_mean_value_for_id(counter, xlist)
    return print('Success')


populate_avg_column_for_twelve(for_twelve_months)
close_everything()




