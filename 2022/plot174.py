import numpy as np
import matplotlib.pyplot as plt

print("Imported Numpy as np")
print("Imported Matplotlib.pyplot as plt")

#Load paths for lab books
NO = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NO/'
NP = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NP/'
NT = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NT/'
NU = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NU/'
NX = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NX/'
NY = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NY/'
NZ = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/NZ/'

fna = ['nz007g','nz007h','nz008a','nz008b','nz008c','nz008d','nz008e']


for i in range(0,np.size(fna)):
    #fn = input("Enter file name: ")
    fn = fna[i]+'_174'
    fd = fn[:2].upper()
    pth = '/Users/ben/Dropbox/Radical Spectroscopy/REMPI/'+fd+'/'+fn+'.dat'
    if '_' in fn:
        x,y = np.loadtxt(pth,usecols=(1,2),unpack=True)
        x = x[:-1]
        y = y[:-1]
        y *=-1
    if '_' not in fn:
        x,y = np.loadtxt(pth,usecols=(2,3),unpack=True)
    lab = fn[2:6]
    x *= 0.5
    x = 1e7/x
    plt.plot(x,y,label=lab)
plt.xlabel('wavenumbers (cm$^{-1}$)')
plt.legend()
plt.show()

