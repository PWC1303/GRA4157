import numpy as np 
import matplotlib.pyplot as plt
F_arr = np.linspace(-20,120,500)

def inexcact(F_arr):
    C_arr = (F_arr-20)/2
    return C_arr

def excact(F_arr):
    C_arr = (F_arr-20)*(5/9)
    return C_arr

plt.plot(F_arr,inexcact(F_arr),label = "inexcact")

plt.plot(F_arr,excact(F_arr),label = "Excact")
plt.title("Excact vs inexcact conversion of celsius to fahrenheit")
plt.show()
