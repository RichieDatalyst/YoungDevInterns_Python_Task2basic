import matplotlib.pyplot as plt
import numpy as np
import math

angles = np.arange(0, 2*math.pi, 0.01)

x = np.sin(4*angles) - 3 
y = np.cos(4*angles) - 3

plt.figure(figsize=(8, 6))
plt.plot(angles, x, label='Sine(4*a) - 3')
plt.plot(angles, y, label='Cosine(4*b) - 3')
plt.title('Sine and Cosine Graphs')
plt.xlabel('Angle (radians)')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()