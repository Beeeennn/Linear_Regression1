import numpy as np
def predict_val(x):
    f = open("parameters.txt","r")
    w,b = (f.read()).split(",")
    f.close
    print(w)
    print(b)
    w = float(w)
    b = float(b)
    prediction = w*x+b
    return prediction
print(predict_val(2.1))