
import numpy as np 
import matplotlib.pyplot as plt
data = np.loadtxt("xy.dat",dtype=float)
print(data)
x = data[:,0]
y = data[:,1]
print(f"mean of x is {np.mean(x)}")
print(f"mean of y is {np.mean(y)}")
plt.plot(x,y)
plt.show()