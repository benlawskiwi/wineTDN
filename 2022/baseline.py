import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from scipy.optimize import curve_fit
from scipy import interpolate

x,y = np.loadtxt('174spec.dat',delimiter=',',unpack=True)

step = 15
w = 5 # window must be odd!

subr = np.logical_and(x>36360,x<40000)
xr = x[subr]
yr = y[subr]

n = round(np.size(xr)/step)

xx = []
yy = []
for i in range(0,n-1):
    s = slice(step*i,step*i+step,1)
    a = np.mean(xr[s])
    b = min(yr[s])
    xx.append(a)
    yy.append(b)

sg = savgol_filter(yy,w,3)
f = interpolate.interp1d(xx,sg,fill_value='extrapolate')
ynew = f(xr)
i = yr-ynew
i += 890

plt.plot(xx,yy)
plt.plot(x,y)
plt.plot(xx,sg)
plt.plot(xr,ynew,'--')
plt.show()

subr2 = np.logical_and(x<36360,x>0)
x2 = x[subr2]
y2 = y[subr2]

xt = np.append(x2,xr)
yt = np.append(y2,i)
data = np.column_stack((xt,yt))
np.savetxt('base-174spec.dat',data,delimiter=',')

plt.plot(x,y+14000)
#plt.plot(xr,i)
#plt.plot(x2,y2)
plt.plot(xt,yt)
plt.show()
