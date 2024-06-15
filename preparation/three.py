import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
def returns_dydt(y,t):
     dydt=np.sqrt((2*t-np.exp(y))/4*y)
     return dydt
y0=1
t=np.linspace(0,5)
y=odeint(returns_dydt,y0,t)
plt.plot(t,y)
plt.show()
