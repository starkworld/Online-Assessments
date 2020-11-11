import datetime, time
from sklearn.linear_model import LinearRegression
import numpy as np


def predictTemperature(startDate, endDate, temparature, n):
    p = int(len(temparature) / 24)
    x = []
    for i in range(1, ((24 * p) + 1)):
        x.append(i)
    y = temparature
    lm = LinearRegression()
    lm.fit(np.asarray(x).reshape(-1, 1), y)

    f = x[-1] + 1
    z = []
    for i in range(24 * n):
        z.append(f)
        f += 1
    return lm.predict(np.asarray(z).reshape(-1, 1)).tolist()


import datetime
from sklearn.linear_model import LinearRegression
import pandas as pd
import random


# predict temperature method
def predictTemperature(startDate, endDate, temps, n):
    startDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")

    endDate = datetime.datetime.strptime(endDate, "%Y-%m-%d")
    endDate = endDate + datetime.timedelta(days=1)
    dates = []
    # create datetime objects between start and end dates
    while startDate < endDate:
        dates.append(startDate)
        startDate = startDate + datetime.timedelta(hours=1)

    # create 24*n test data dates
    testdates = [endDate + datetime.timedelta(hours=x) for x in range(24 * n)]
    X_test = pd.DataFrame(testdates, columns=['datetime'])
    X_test.set_index('datetime', inplace=True)  # set datetime as index t pandas dataframe
    # add seperate entities of datetime object as features/columns
    X_test['Year'] = X_test.index.year
    X_test['Month'] = X_test.index.month
    X_test['Day'] = X_test.index.day
    X_test['Hour'] = X_test.index.hour
    # change dataframe to array
    X_test = X_test.values
    # make dataframe for training datetime and temperature
    df = pd.DataFrame({'datetime': dates, 'temperature': temps})
    df.set_index('datetime', inplace=True)
    # add seperate entities of datetime object as features/columns
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df['Day'] = df.index.day
    df['Hour'] = df.index.hour
    # change dataframe to array
    df = df.values
    # seperation of array into features and target columns
    X_train = df[:, 1:]
    y_train = df[:, 0:1]
    # create a linear reggresion object
    clf = LinearRegression()
    clf.fit(X_train, y_train)  # fit ovr training data
    y_pred = clf.predict(X_test)  # predict and save result
    return y_pred  # return the result


def main():
    # take strt and end date
    startDate = input()
    endDate = input()
    temps = []
    # take temperature values
    strt = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    end = datetime.datetime.strptime(endDate, "%Y-%m-%d")
    end = end + datetime.timedelta(days=1)
    while strt < end:
        temps.append(float(input()))
        strt = strt + datetime.timedelta(hours=1)
    # take n number of days to predict
    n = int(input())
    # make prediction
    prediction = predictTemperature(startDate, endDate, temps, n)
    # output prediction
    for x in prediction:
        print("%.2f" % x)


if __name__ == "__main__":
    main()
