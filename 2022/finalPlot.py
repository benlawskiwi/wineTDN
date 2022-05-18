import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt('base-174spec.dat',delimiter=',',unpack=True)

#Plotting Settings
width = 3.487*2
height = width/1.4
width *=1.8
one_col = (width,height)
fig,ax = plt.subplots(figsize=one_col)

plt.plot(x,y)

ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.yticks([])
plt.xticks([36000,36500,37000,37500,38000])
ax.set_xticklabels(['36000','36500','37000','37500','38000'],fontsize=14)
plt.minorticks_on()
plt.xlabel('Excitation Energy (cm$^{-1}$)',fontsize=14)
ax.tick_params(width=1.5)

ax.tick_params(width=1.5)
plt.setp(ax.spines.values(), linewidth=1.5)
plt.annotate(r'm/z = 174',(37700,14000),fontsize=12)

plt.savefig('174-plot.png', dpi=600,bbox_inches='tight')
plt.show()
