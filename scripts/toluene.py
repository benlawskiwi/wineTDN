import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('../toluene.dat',delimiter=',',unpack=True)
x += 37477.4
y *=5

FWHM = 1

a,xw,yw,b = np.loadtxt('../data/nu038g_92.dat',unpack=True)
yw *=-1
xw += 0.1
xw = 1e7/(xw/2)
yw *= 1000/np.max(yw)

a,xw2,yw2,b = np.loadtxt('../data/nu038c_92.dat',unpack=True)
yw2 *=-1
xw2 += 0.1
xw2 = 1e7/(xw2/2)
yw2 *= 1000/np.max(yw2)
subr = np.logical_and(xw2>39294,xw2<50000)
xw2 = xw2[subr]
yw2 = yw2[subr]


def Gauss (E0,FWHM,E):
    alpha = FWHM/2/np.sqrt(np.log(2.0))
    return np.exp(-((E0-E)/alpha)**2)
Ev = np.arange(37477.4,37477.4+2000,0.1)
spec = np.zeros(np.size(Ev))

for i in range(0,np.size(x)):
    spec += y[i]*Gauss(x[i],FWHM,Ev)

plt.plot(Ev,spec,label='toluene')
plt.plot(xw,yw,'C2',label='mass92')
plt.plot(xw2,yw2,'C2')
plt.legend()
plt.xlabel('Energy (cm$^{-1}$')
plt.show()
