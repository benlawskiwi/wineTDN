import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('ny024f_178.dat',usecols=(1,2),unpack=True)
x=x[:-1]
y=y[:-1]
y *=-1
x *=0.5


plt.plot(x,y,'C1',label='m/z 178')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (mV)')
plt.legend()

plt.savefig('p178.png',dpi=400,bbox_inches='tight')
plt.show()
