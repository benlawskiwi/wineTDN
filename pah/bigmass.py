import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.signal import savgol_filter

th = -0.0040
plt.figure(figsize=(10,5))
mz = []
mzi = []

#Load paths for lab books
NO = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NO/'
NP = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NP/'
NT = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NT/'
NU = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NU/'
NX = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NX/'
NY = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NY/'
#print('load lab book paths')
#print('-- NO\n-- NP\n-- NT\n-- NU\n-- NX\n-- NY')

#x,y = np.loadtxt(NU+'nu071b.dat',usecols=(2,3),unpack=True)
x,y = np.loadtxt('ny024c.dat',usecols=(2,3),unpack=True)
#sg = savgol_filter(y,5,2)
#y = sg

#Frist, baseline subtraction
subr = np.logical_and(x>198,x<200)
yr = y[subr]
ym = np.mean(yr)
y -= ym

#Second, select threshold for peaks.
xc = 0
for i in range(0,np.size(x)):
    if x[i] <= xc: continue
    if y[i] <= th:
        for j in range (i,np.size(x)):
            if y[j] >= th:
                xp = x[i-1:j]
                yp = y[i-1:j]
                ym = min(yp)
                ind = np.argmin(yp)
                xm = xp[ind]
                if round(xm) in mz: continue
                mz.append(round(xm))
                mzi.append(float('%.2g' % ym))
                xc = x[j]
                break
            
print(mz)
print(mzi)
for i in range(0,np.size(mz)):
    xx = mz[i]
    yy = mzi[i]-0.008
    plt.annotate(mz[i],(xx,yy),ha='center',fontsize=8)

plt.plot(x,y,'C0',label='Phenanthrene HV Discharge')
plt.xlabel('m/z')
plt.yticks([])
plt.legend(loc=4)
#plt.xlim(75,235)
plt.ylim(-0.22,0.005)
plt.savefig('massBig.png',dpi=400,bbox_inches='tight')
plt.show()
