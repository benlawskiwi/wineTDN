import numpy as np
import matplotlib.pyplot as plt
import json
import glob
import os

with open('sfs.json') as json_file:
    data  = json.load(json_file)

mn = input('Molecule to compare (toluene): ')
mz = input('Mass to plot (92): ')

a,b = np.loadtxt('mainzSpec/'+str(mn)+'.txt',unpack=True)
plt.plot(1e7/a,b/max(b),lw=0.8,label=mn)

path = 'rempiSpec/' 
rg = []

print('REMPI spectra to plot: ')
for filename in glob.glob(os.path.join(path, str(mz)+'*')):
    print(filename)
    ra = filename[-11:]
    rb = ra[:-4].split('_')
    rg.append(rb[0])
    rg.append(rb[1])
    s = 1
    for i in data:
        if filename == path+str(i['fns'])+'.txt':
            #print(i['sf'])
            s = float(i['sf'])    
    x,y = np.loadtxt(filename,usecols=(1,2),unpack=True)
    x = x[:-1]
    y = y[:-1]
    plt.plot(2e7/x,y*s/min(y),label='mz = '+str(mz))

#a,b = np.loadtxt('mainzSpec/'+str(mn)+'.txt',unpack=True)
#plt.plot(a,b/max(b))
print(rg)
rm = 2e7/(int(max(rg)))-300
rx = 2e7/(int(min(rg)))+300
#print(rx)
#print(rm)
plt.xlim(rm,rx)
plt.legend()
plt.xlabel(r'Excitation Energy (cm$^{-1}$)')
plt.ylabel('Normalized intensity')

plt.show()

