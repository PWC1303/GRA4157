import numpy as np 


import matplotlib.pyplot as plt 

x_arr = np.linspace(-4,4,41)

def h(x_arr):
    h_arr = (1/np.sqrt(2*np.pi))*np.exp(-|1*np.power(x_arr,2)/2)
    return h_arr


h_arr = h(x_arr)
print(h_arr)

plt.plot(x_arr,h_arr)
plt.show()