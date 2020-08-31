import numpy as np
import matplotlib.pyplot as plt

width=3.33*3
height=width/1.4
one_col=(1.5*width,height)
fig,ax = plt.subplots(figsize=one_col)

xt,yt = np.loadtxt('nu033ta_base.dat',unpack=True)
xs,ys = np.loadtxt('nu033sa_base.dat',unpack=True)


plt.plot(xt,yt+0.01,label='266nm + 275nm')
plt.plot(xs,ys,label='266nm only')
plt.yticks([])
plt.xlabel('mass (amu)')
plt.ylabel('ion signal (mV)')
plt.title('2012 Riesling Mass Spec')
plt.legend()

m = [20,40,94,116,128,154,178,186,192,202,206,209,220,228,246,262,395,410,484]
for i in range (0,np.size(m)):
    subr = np.logical_and(xt>m[i]-1,xt<m[i]+1)
    l = max(yt[subr])+0.0105
    if m[i] == 220 or m[i] == 206 or m[i] == 186:
        l += 0.0005
    plt.annotate(str(m[i]),(m[i],l),ha='center')
    if m[i] == 128:
        plt.annotate('naphthalene',(m[i],l+0.0015),ha='center',va='bottom',rotation=90)
    if m[i] == 154:
        plt.annotate('acenaphthene',(m[i],l+0.0015),ha='center',va='bottom',rotation=90)
plt.savefig('nu033FinalPlot.png',dpi=400,bbbox_inches='tight')
plt.show()
