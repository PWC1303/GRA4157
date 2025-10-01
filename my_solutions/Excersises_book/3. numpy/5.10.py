import numpy as np
import sys 
import matplotlib.pyplot as plt 
arg = (sys.argv[1:])
v0_arr = np.array((arg),dtype = float)


def y(t,v0):
        g=9.81
        y = v0 *t -(1*g*np.power(t,2))/2
        return y 
for v0 in v0_arr:
    g = 9.81
    t_max = 2*v0/g
    t_arr1 = np.linspace(0,t_max,10)
    plt.plot(t_arr1,y(t_arr1,v0),label = f"v0: {v0}")
    
plt.legend()   
plt.xlabel("time")
plt.ylabel("height?")
plt.show()


for v0 in v0_arr:
    g = 9.81
    t_max = 2*v0/g
    t_arr1 = np.linspace(0,t_max,10)
    plt.plot(t_arr1,y(t_arr1,v0),label = f"v0: {v0}")
    
plt.legend()   
plt.xlabel("time")
plt.ylabel("height?")
plt.show()

