
import numpy as np
from django.db import connections


c = connections['usaunem'].cursor()
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
    am = counter + 12
    an = counter + 13
    ao = counter + 14
    ap = counter + 15
    aq = counter + 16
    ar = counter + 17
    aas = counter + 18 #as is a keyword so using aas
    at = counter + 19
    au = counter + 20
    av = counter + 21
    aw = counter + 22
    ax = counter + 23
    ay = counter + 24
    az = counter + 25
    ba = counter + 26
    bb = counter + 27
    bc = counter + 28
    bd = counter + 29
    be = counter + 30
    bf = counter + 31
    bg = counter + 32
    bh = counter + 33
    bi = counter + 34
    bj = counter + 35

    mylist = []
    c.execute("SELECT gvalue FROM usaunemploymentavg WHERE id IN (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
              (aa, ab, ac, ad ,ae ,af ,ag ,ah ,ai ,aj ,ak ,al,
               am, an, ao, ap, aq, ar, aas, at, au, av, aw, ax,
               ay, az, ba, bb, bc, bd, be, bf, bg, bh, bi, bj))
    mylist = c.fetchall()
    return mylist



def do_mean_pass_mean_value_for_id(counter_id, mylist=[]):
    print("checkpoint 4")
    avg_num = np.mean(mylist)
    mean = np.around(avg_num, decimals=3)
    print(mylist)
    print(counter_id)
    c.execute("UPDATE usaunemploymentavg SET thirtysixmonthavg = (?) WHERE id = (?)", (mean, counter_id))



def populate_avg_column_for_thirtysix(value):
    print('checkpoint 1')
    count_till = counting_till(value)
    print(count_till)
    counter = 0
    while (count_till > counter): #823 == 823 loop will work
        counter = counter + 1
        xlist = get_three_values(counter)
        do_mean_pass_mean_value_for_id(counter, xlist)
    return print('Success')


populate_avg_column_for_thirtysix(for_thirty_six_months)
close_everything()




