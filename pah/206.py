import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('ny024f_206.dat',usecols=(1,2),unpack=True)
x=x[:-1]
y=y[:-1]
y *=-1
x *=0.5
plt.plot(x,y,'C4',label='m/z 206')
x,y = np.loadtxt('ny024e_206.dat',usecols=(1,2),unpack=True)
x=x[:-1]
y=y[:-1]
y *=-1
x *=0.5
y += 30

subr = np.logical_and(x>287.5,x<1000)
xn = x[subr]
yn = y[subr]


plt.plot(xn,yn,'C4')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (mV)')
plt.legend()

plt.savefig('p206.png',dpi=400,bbox_inches='tight')
plt.show()
