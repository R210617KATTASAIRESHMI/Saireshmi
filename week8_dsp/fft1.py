import cmath
import numpy as np
from matplotlib import pyplot as plt

def fft(x):
	N = len(x)
	if N <= 1:
        		return x
	else:
		even_terms = fft(x[0::2])  
		odd_terms = fft(x[1::2])  
		combined = [0] * N
		for k in range(N//2):
			twiddle = np.exp(-2j *np.pi * k / N) * odd_terms[k]
			combined[k] = even_terms[k] + twiddle
			combined[k + N//2] = even_terms[k] - twiddle
		return combined

input_data = [1,-1,2,4]
N = len(input_data)
output = fft(input_data)
print("FFT Result:")
for value in output:	
	print(value)


def dft(x,N):
	X=[]
	for k in np.arange(0,N):
		s=0
		for n in np.arange(0,N):
			l=k/N
			s=s+x[n]*np.exp(-1j*2*np.pi*n*l)
		X.append(s)
	return X


Y=dft(input_data,N)

X=fft(input_data )
X_magnitude=np.abs(X)
X_phase=np.angle(X)
plt.subplot(4,1,1)
plt.stem(X_magnitude)
plt.subplot(4,1,2)
plt.stem(X_phase)

Y_magnitude=np.abs(Y)
Y_phase=np.angle(Y)
plt.subplot(4,1,3)
plt.stem(Y_magnitude)
plt.subplot(4,1,4)
plt.stem(Y_phase)
plt.show() 



