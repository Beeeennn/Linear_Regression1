import matplotlib.pyplot as plt
import numpy as np
import Utils
import predict_val

x,y = Utils.convert_csv_single("Sheet1.csv",1,-1)
f = open("parameters.txt","r")
w,b = (f.read()).split(",")

x1 = np.linspace(0, 300, 100)
y1 = float(w) * x1 + float(b)


plt.plot(x1,y1)
print(len(x))
print(len(y))
plt.scatter(x,y,color = "r")
plt.show()