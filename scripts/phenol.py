import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('nu075i_94.dat',usecols=(1,2),unpack=True)

ptl.plot(x,y)
plt.show()
