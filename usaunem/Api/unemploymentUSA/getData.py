import quandl as quandl
import numpy as np
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta


api = 'FRED/UNEMPLOY'
authkey = open('APIKEY.txt', 'r').read()


def getThreeMonthData():
    three_months = date.today().replace(day=1) + relativedelta(months=-3)
    dataForThreeMonths = quandl.get(api, authtoken=authkey, start_date=three_months)
    return dataForThreeMonths


def getTwelveMonthData():
    twelve_months = date.today().replace(day=1) + relativedelta(months=-12)
    dataForTwelveMonths = quandl.get(api, authtoken=authkey, start_date=twelve_months)
    return dataForTwelveMonths


def getThirthSixMonthData():
    thirtySix_months = date.today().replace(day=1) + relativedelta(months=-36)
    dataForThirtySixMonths = quandl.get(api, authtoken=authkey, start_date=thirtySix_months)
    return dataForThirtySixMonths


def getCustomMonthData(customStartDate,customEndDate):
    dataForThirtySixMonths = quandl.get(api, authtoken=authkey, start_date=customStartDate, end_date=customEndDate, collapse="monthly")
    return dataForThirtySixMonths


table1 = getThreeMonthData()

table1 = np.array(table1) #table1 values in array now.
result1 = sum(table1)/len(table1)
print(result1)

table2 = getTwelveMonthData()

table2 = np.array(table2) #table2 values in array now.
result2 = sum(table2)/len(table2)
print(result2)

table3 = getThirthSixMonthData()

table3 = np.array(table3) #table1 values in array now.
result3 = sum(table3)/len(table3)
print(result3)








#result1 = pd.DataFrame(np.array(getThreeMonthData()))
#result2 = pd.DataFrame(np.array(getTwelveMonthData()))
#result3 = pd.DataFrame(np.array(getThirthSixMonthData()))

#concat = pd.concat([result1, result2, result3])


#print(table1)

