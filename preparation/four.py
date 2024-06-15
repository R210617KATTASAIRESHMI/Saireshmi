import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
f=2
x=np.sin(2*f*np.pi*t)
y=np.cos(2*f*np.pi*t)
plt.subplot(1,2,1)
plt.plot(x)
plt.subplot(1,2,2)
plt.plot(y)
plt.show()
