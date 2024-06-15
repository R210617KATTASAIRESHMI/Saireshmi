import numpy as np 
from scipy.integrate import odeint 
from matplotlib import pyplot as plt 
def returns_dydt(y,t): 
   dydt = -y * t + 13
   return dydt  
# initial condition 
y0 = [1,2]
# values of time 
t = np.linspace(0,5) 
# solving ODE 
y = odeint(returns_dydt, y0, t)  
# plot results 
plt.plot(t,y) 

plt.xlabel("Time") 
plt.ylabel("Y") 
plt.show()
plt.legend('y')
