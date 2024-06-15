import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
def returns_dydx(y,x):
      dydx=x**3-5*np.exp(y)-10*np.sin(x) 
      return dydx
y0=1
x=np.linspace(0,5)
y=odeint(returns_dydx,y0,x)
plt.plot(x,y)
plt.legend('y')
plt.show()
