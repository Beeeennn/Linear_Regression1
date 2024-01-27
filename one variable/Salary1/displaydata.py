import matplotlib.pyplot as plt
import numpy as np
import Utils
import predict_val

x,y = Utils.convert_csv_single("Salary_dataset.csv",2,0)
f = open("parameters.txt","r")
w,b = (f.read()).split(",")

x1 = np.linspace(0, 10, 100)
y1 = float(w) * x1 + float(b)


plt.plot(x1,y1)
plt.scatter(x,y,color = "r")
plt.show()