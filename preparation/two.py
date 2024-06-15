import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
def returns_dydx(y,x):
      dydx=x*np.exp(x**2)
      return dydx
y0=1
x=np.linspace(0,5)
y=odeint(returns_dydx,y0,x)
plt.plot(x,y)
plt.show()
