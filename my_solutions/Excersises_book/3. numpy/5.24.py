
import numpy as np 
x_sq = [0, 1, 1, 0, 0]
y_sq = [0, 0, 1, 1, 0]

x_rt = [0, 2, 0, 0]
y_rt = [0, 0, 1, 0]

x_pol = [0, 1, 2, 1.5, 0.5, 0]
y_pol = [0, 0, 1, 2, 2, 1]



def polygon_area(x,y):
    x = np.array(x); y = np.array(y)
  
    Area = (1/2)*(np.dot(x[:-1],y[1:])- np.dot(y[:-1],x[1:]))
    return Area
print(polygon_area(x_pol,y_pol))