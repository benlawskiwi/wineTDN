import numpy as np
import matplotlib.pyplot as plt

#fn = ['35d','35e','35f','35g','35h']
#fn = ['37a','37b','37c','37d']
#fn = ['37d','35g']
fn = ['38a','38b','38d','38e']


for i in range(0,np.size(fn)):
    a,b,x,y = np.loadtxt('../data/nu0'+fn[i]+'_mass.dat',unpack=True)
    y += i*0.012
    plt.plot(x,y)

plt.show()
