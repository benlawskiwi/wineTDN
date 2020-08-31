import numpy as np
import matplotlib.pyplot as plt

fn = ['36a_94','37f_138','37f_94','38c_115','38c_154']
lab = ['94','138','94','115','154']

for i in range(0,np.size(fn)):
    x,y = np.loadtxt('nu0'+fn[i]+'base.dat',unpack=True)
    x *=0.5
    ax = plt.subplot(2,3,i+1)
    ax.plot(x,y,label='Mass '+lab[i])
    plt.xlabel ('wavelength (nm)')
    plt.legend()
plt.show()
