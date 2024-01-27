import numpy as np
import matplotlib.pyplot as plt
from Utils import *

def compute_cost(x,y,w,b):

    m = len(x)

    cost = 0

    for i in range(m):
        cost += (w*x[i]+b-y[i])**2
    cost = (cost/(m*2))

    return cost


def grad_desc(x,y,w,b):
    m = len(x)
    dj_dw = 0
    dj_db = 0
    for i in range(m):
        dj_dw += (w*x[i]+b-y[i])*x[i]
        dj_db += (w*x[i]+b-y[i])
    dj_db /= m
    dj_dw /= m
    return dj_dw,dj_db


def update_values(x,y,w,b,rate):
    dj_dw,dj_db = grad_desc(x,y,w,b)
    wt = w - rate*(dj_dw)
    bt = b - rate*(dj_db)
    w = wt
    b = bt
    return w,b

def train_model(x,y,w,b,rate,itterations):
    costs = []
    itts = []
    for i in range(itterations):
        if i%1 == 0:
            cost = compute_cost(x,y,w,b)
            print(cost)
            costs += [cost]
            itts += [i]
        w,b = update_values(x,y,w,b,rate)
    plt.plot(itts,costs)
    plt.show()
    savedvals = str(w)+","+str(b)
    f = open("parameters.txt","w")
    f.write(savedvals)
    f.close()
    print("Trained!")
    return(w,b)

def predict_value(inp,w,b):
    return w*inp+b

w = 0
b = 0

x,y = convert_csv_single("Salary_dataset.csv",2,0)
w,b = train_model(x,y,w,b,0.001,150)

