import pickle 
import numpy as np
t=np.arange(0,1,0.01)
f=3
x=np.sin(2*np.pi*f*t)
with open("pickle.pkl","wb")as k:
	pickle.dump(x,k)
