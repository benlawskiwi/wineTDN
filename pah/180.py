import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('ny025a_180.dat',usecols=(1,2),unpack=True)
x=x[:-1]
y=y[:-1]
y *=-1
x *=0.5
y -= y[-1]

plt.plot(x,y,'C3',label='m/z 180')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (mV)')
plt.legend()
plt.xlim(290,298)
plt.ylim(-20,255)

plt.savefig('p180.png',dpi=400,bbox_inches='tight')
plt.show()
