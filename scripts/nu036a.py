import numpy as np
import matplotlib.pyplot as plt

fn = ['116','128','154','94']

for i in range (0,np.size(fn)):
    a,x,y,b = np.loadtxt('../data/nu036a_'+fn[i]+'.dat',unpack=True)
    ax = plt.subplot(2,2,i+1)
    x = x[:-1]
    y = y[:-1]
    y *=-1
    ax.plot(x,y,label=fn[i])
    ax.legend()
    

plt.show()
