import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import calendar
import datetime



def inter():
    t = 22300
    v = 2629605
    k = 1000
    X = []
    Y = []

    while t < v-2570000 :
        t+=k
        Y.append(i1(t))
        X.append(t)
        # print(t)
    print(X)
    print(Y)

    plt.plot(X, Y)
    plt.show()

def i1(t):
    v=2629605

    day = 27
    month = 7
    y = 2019

    # t = 65300
    long = 300
    start = 0
    s = start
    while s < start+long:
        b = (month+s) % 12
        b = 12 if b == 0 else b
        # year+=1 if b == 1 else year
        if b == 1 : y += 1

        # print(y,b , "::")
        a1,a2 = test(d0 = datetime.date(y,b,day),s = v, t=t,period = s)
        v-=t-a2

        s += 1
        if v<0:
            break
    return a1

def test(d0,s,t,period):
    q=9.5


    D = datetime.datetime.today()
    d  = D.__format__('%Y-%m-%d')

    y = d0.year
    m = d0.month
    d = d0.day

    dy = datetime.date(y-1,m,d)
    if m > 1:
        dm = datetime.date(y,m-1,d)
    else:
        dm = datetime.date(y-1,12,d)
    # delta = datetime.timedelta(years = 4)
    # print()
    V = s*q*(d0-dm)/((d0-dy)*100)
    # print(period+1,'%.1f'%((period+1)/12), d0,'%.2f'%(t-V),'%.2f'%V,'%.2f'%s,d0-dy, d0-dm)
    return(period,V)
