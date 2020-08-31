import numpy as np
import matplotlib.pyplot as plt

ta = ['m','j','i','e','p','v','x']
tm = [0,47,82.17,146.3,229.6,314.6,417,600]
sa = ['n','k','h','b','q','u','x']

xn = []
yn = []

for i in range(0,np.size(ta)):
    a,b,x,y = np.loadtxt('../data/nu033'+ta[i]+'_mass.dat',unpack=True)
    subr = np.logical_and(x>tm[i],x<tm[i+1])
    x = x[subr]
    y = y[subr]
    if i ==3:
        y += 0.000308
    if i ==5:
        y += 0.00025
    xn.extend(x)
    yn.extend(y)
    plt.plot(x,y)

np.savetxt('nu033ta.dat',np.column_stack((xn,yn)))
plt.plot(xn,yn)
plt.show()

xn = []
yn = []
for i in range(0,np.size(sa)):
    a,b,x,y = np.loadtxt('../data/nu033'+sa[i]+'_mass.dat',unpack=True)
    subr = np.logical_and(x>tm[i],x<tm[i+1])
    x = x[subr]
    y = y[subr]
    if i ==2:
        y += 0.00062
    if i ==3:
        y -= 0.00083
    if i ==5:
        y -= 0.00042
    xn.extend(x)
    yn.extend(y)
    plt.plot(x,y)

np.savetxt('nu033sa.dat',np.column_stack((xn,yn)))
plt.plot(xn,yn)
plt.show()


