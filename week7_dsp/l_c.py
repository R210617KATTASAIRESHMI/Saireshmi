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
def idft(X,N):
	x=[]
	for n in np.arange(0,N):
		s=0
		for k in np.arange(0,N):
			s=s+X[k]*np.exp(1j*2*np.pi*n*k/N)
		d=s/N
		x.append(d)
	return x
a=[2,3]#l1=2
b=[2,3,5,6]#l2=4
a_zp=[2,3,0,0,0]
b_zp=[2,3,5,6,0]
x=np.array(dft(a_zp,5))
y=np.array(dft(b_zp,5))
z=x*y
result=idft(z,5)
print(np.real(result))


