import numpy as np
import matplotlib.pyplot as plt

width=3.33*3
height=width/1.4
one_col=(1.5*width,height)
fig,ax = plt.subplots(figsize=one_col)

xt,yt = np.loadtxt('nu035g_base.dat',unpack=True)
xs,ys = np.loadtxt('nu035e_base.dat',unpack=True)


plt.plot(xt,yt+0.01,label='after replacing wine')
plt.plot(xs,ys,label='before replacing wine')
plt.yticks([])
plt.xlabel('mass (amu)')
plt.ylabel('ion signal (mV)')
plt.title('2008 Riesling Mass Spec')
plt.legend()

m = [94,102,108,121,128,134,142,154,169,186,191,202,206,210,220]
for i in range (0,np.size(m)):
    subr = np.logical_and(xt>m[i]-1,xt<m[i]+1)
    l = max(yt[subr])+0.0105
    if m[i] == 220 or m[i] == 206 or m[i] == 186:
        l += 0.0005
    plt.annotate(str(m[i]),(m[i],l),ha='center')
    if m[i] == 1128:
        plt.annotate('naphthalene',(m[i],l+0.0015),ha='center',va='bottom',rotation=90)
    if m[i] == 1154:
        plt.annotate('acenaphthene',(m[i],l+0.0015),ha='center',va='bottom',rotation=90)
plt.savefig('nu035eFinalPlot.png',dpi=400,bbbox_inches='tight')
plt.show()
