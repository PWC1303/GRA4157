import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace((5*np.pi)/6,(13*np.pi)/6,10000)


plt.plot(x,np.sin(3*x))
plt.show()
