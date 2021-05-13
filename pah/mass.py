import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('ny024c.dat',usecols=(2,3),unpack=True)

plt.plot(x,y)
plt.show()
