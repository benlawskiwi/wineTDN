import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from scipy.optimize import curve_fit
from scipy import interpolate


a,b,x,y = np.loadtxt('../data/nu038d_mass.dat',unpack=True)

y *=-1
step = 50
w = 11 # window must be odd!

n = round(np.size(x)/step)

xx = []
yy = []
for i in range(0,n-1):
    s = slice(step*i,step*i+step,1)
    a = np.mean(x[s])
    b = min(y[s])
    xx.append(a)
    yy.append(b)

sg = savgol_filter(yy,w,3)
f = interpolate.interp1d(xx,sg,fill_value='extrapolate')
ynew = f(x)
i = y-ynew

plt.plot(xx,yy)
plt.plot(x,y)
plt.plot(xx,sg)
plt.plot(x,ynew,'--')
plt.show()

plt.plot(x,y)
plt.plot(x,i)
plt.show()
np.savetxt('nu038d_base.dat',np.column_stack((x,i)))
#print(np.size(sg))
#print(np.size(x))
