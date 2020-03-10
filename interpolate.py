import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import calendar
import datetime


def inter():
    #Год начала выплат
    year = 2019
    #Месяц начала выплат
    month = 7
    #День ежемесячных выплат
    day = 27

    #Минимальная выплата
    tmin = 22300
    #Максимальная выплата
    tmax = 120000
    #Сумма долга
    v = 2629605
    #Ставка
    q = 9.5
    #Шаг увелечения выплаты для просчета
    k = 1000

    X = []
    Y = []

    t = tmin
    while t < tmax:
        t += k
        Y.append(i1(year=year, month=month, day=day, t=t, v=v, q=q))
        X.append(t)

    print(X)
    print(Y)

    plt.plot(X, Y)
    plt.xticks(np.arange(min(X), max(X)+1, k), rotation='vertical')
    plt.yticks(np.arange(min(Y), max(Y)+1, 5.0))
    plt.grid(color='gray', linestyle='dashed')
    plt.show()

def i1(year,month,day,t,v,q):
    long = 300
    start = 0
    s = start
    while s < start+long:
        b = (month+s) % 12
        b = 12 if b == 0 else b
        # year+=1 if b == 1 else year
        if b == 1: year += 1

        # print(y,b , "::")
        a2 = test(d0=datetime.date(year, b, day), s=v, q=q)

        v -= t-a2
        s += 1
        if v < 0:
            break
    return s

def test(d0,s,q):
    y = d0.year
    m = d0.month
    d = d0.day

    dy = datetime.date(y-1, m, d)
    if m > 1:
        dm = datetime.date(y, m-1, d)
    else:
        dm = datetime.date(y-1, 12, d)

    # print(d0, dm, dy)
    V = s*(d0-dm)/((d0-dy)*100)
    V*=q
    # V = s*q*(d0-dm)/((d0-dy)*100)
    # print(period+1,'%.1f'%((period+1)/12), d0,'%.2f'%(t-V),'%.2f'%V,'%.2f'%s,d0-dy, d0-dm)
    return(V)


