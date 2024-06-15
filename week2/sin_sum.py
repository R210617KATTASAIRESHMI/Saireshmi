import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
f1=5
x=np.sin(2*np.pi*f1*t)
f2=3
y=np.sin(2*np.pi*f2*t)
k=x+y
plt.plot(t,k)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('sine wave')
plt.show()
