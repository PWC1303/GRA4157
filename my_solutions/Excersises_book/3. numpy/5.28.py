import numpy as np 
import matplotlib.pyplot as plt 


x = np.linspace(-4,4,100)

t = 0

def wawe_packet(x,t):
    y = np.exp(np.power(-(x-3*t),2))*np.sin(3*np.pi*(x-t))
    return y


plt.plot(x,wawe_packet(x,t))
plt.show()


##### some cool shit chat showed me 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define x values
x = np.linspace(-4, 4, 400)

# Wave packet function
def wave_packet(x, t):
    return np.exp(-(x - 3*t)**2) * np.sin(3*np.pi*(x - t))

# Set up the figure and axis
fig, ax = plt.subplots()
line, = ax.plot(x, wave_packet(x, 0))
ax.set_ylim(-1, 1)  # keep y-axis fixed

# Update function for animation
def update(frame):
    t = frame / 20  # controls speed
    line.set_ydata(wave_packet(x, t))
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
