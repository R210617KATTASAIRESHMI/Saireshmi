f=@(t,y)13*exp(t)+y
y0=1
t=linspace(0,5)
[t,y]=ode45(f,t,y0)
plot(t,y)
