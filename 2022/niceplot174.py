import numpy as np
import matplotlib.pyplot as plt

NZ = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NZ/'

fna = ['nz007g','nz007h','nz008a','nz008b','nz008c','nz008d','nz008e']
br = [36410,37037,37212,37270,37383,37734,38200]

xx = []
yy = []

x,y = np.loadtxt(NZ+fna[6]+'_174.dat',usecols=(1,2),unpack=True)
x=x[:-1]
y=y[:-1]
y *=-1
x *=0.5
x = 1e7/x

subr = np.logical_and(x<br[0],x>0)
xr = x[subr]
yr = y[subr]
xa=np.append(xx,xr)
ya=np.append(yy,yr)

plt.plot(xr,yr,'C0')

x,y = np.loadtxt(NZ+fna[4]+'_174.dat',usecols=(1,2),unpack=True)
x=x[:-1]
y=y[:-1]
y *=-1
x *=0.5
x = 1e7/x

subr = np.logical_and(x>br[0],x<br[1])
xr = x[subr]
yr = y[subr]
xa=np.append(xa,xr)
ya=np.append(ya,yr)
plt.plot(xr,yr,'C1')

x,y = np.loadtxt(NZ+fna[3]+'_174.dat',usecols=(1,2),unpack=True)
x=x[:-1]
y=y[:-1]
y *=-1
x *=0.5
x = 1e7/x

subr = np.logical_and(x>br[1],x<br[2])
xr = x[subr]
yr = y[subr]-300
xa=np.append(xa,xr)
ya=np.append(ya,yr)
subr2 = np.logical_and(x>br[3],x<br[4])
xr2 = x[subr2]
yr2 = y[subr2]-400
#xa=np.append(xa,xr2)
#ya=np.append(ya,yr2)

plt.plot(xr,yr,'C2')
plt.plot(xr2,yr2,'C3')

x,y = np.loadtxt(NZ+fna[5]+'_174.dat',usecols=(1,2),unpack=True)
x=x[:-1]
y=y[:-1]
y *=-1
x *=0.5
x = 1e7/x

subr = np.logical_and(x>br[2],x<br[3])
xr = x[subr]
yr = y[subr]-400
xa=np.append(xa,xr)
ya=np.append(ya,yr)
xa=np.append(xa,xr2)
ya=np.append(ya,yr2)

plt.plot(xr,yr,'C4')

x,y = np.loadtxt(NZ+fna[2]+'_174.dat',usecols=(1,2),unpack=True)
x=x[:-1]
y=y[:-1]
y *=-1
x *=0.5
x = 1e7/x

subr = np.logical_and(x>br[4],x<br[5])
xr = x[subr]
yr = y[subr]
xa=np.append(xa,xr)
ya=np.append(ya,yr)
plt.plot(xr,yr,'C5')

x,y = np.loadtxt(NZ+fna[0]+'_174.dat',usecols=(1,2),unpack=True)
x=x[:-1]
y=y[:-1]
y *=-1
x *=0.5
x = 1e7/x

subr = np.logical_and(x>br[5],x<br[6])
xr = x[subr]
yr = y[subr]+100
xa=np.append(xa,xr)
ya=np.append(ya,yr)
plt.plot(xr,yr,'C6')

plt.show()

data = np.column_stack((xa,ya))
np.savetxt('174spec.dat',data,delimiter=',')
plt.plot(xa,ya)
plt.show()

