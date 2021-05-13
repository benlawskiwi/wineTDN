import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('nu073h_110.dat',usecols=(1,2),unpack=True)
y *= -1
x *= 0.5


plt.plot(x,y,'C4',label='m/z 110')
#plt.xticks([283.5,284,284.5,285])
plt.yticks([])
plt.xlabel('Wavelength (nm)')
plt.legend()
plt.savefig('110.png',dpi=400,bbox_inches='tight')
plt.show()
