import numpy as np
from matplotlib import pyplot as plt
def dft(x,N):
	X=[]
	for k in np.arange(0,N):
		s=0
		for n in np.arange(0,N):
			s=s+x[n]*np.exp(-1j*2*np.pi*n*k/N)
		X.append(s)
	return X
a=[2,3,4,5,0,0]
b=[2,3,5,6,0,0]
c=[2,3,5,0,0,0]
x1=dft(a,6)
x2=dft(b,6)
x3=dft(c,6)
x1_mag=np.abs(x1)
x2_mag=np.abs(x2)
x3_mag=np.abs(x3)

plt.subplot(3,1,1)
plt.plot(x1_mag)
plt.subplot(3,1,2)
plt.plot(x2_mag)
plt.subplot(3,1,3)
plt.plot(x3_mag)
plt.show()


