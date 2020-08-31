import numpy as np
import matplotlib.pyplot as plt

fn = ['116','128','135','154','186','190','206','210','220','230','94']

for i in range (0,np.size(fn)):
    a,x,y,b = np.loadtxt('../data/nu037e_'+fn[i]+'.dat',unpack=True)
    ax = plt.subplot(3,4,i+1)
    x = x[:-1]
    y = y[:-1]
    y *=-1
    x *=0.5
    ax.plot(x,y,label=fn[i])
    ax.legend()
    
plt.show()
