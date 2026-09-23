import numpy as np
import matplotlib.pyplot as plt

#let y = (density of rabbits/sq.km, density of foxes/sq.km)

#initial conditions
y0 = [10.0,10.0]

#parameters
alpha = 1.1
beta = 0.4
delta = 0.1
gamma = 0.4

#ode
def lotka_volterra(_, state, alpha=1.1, beta=0.4, gamma=0.4, delta=0.1):
    x,y = state
    dxdt = alpha*x - beta*x*y
    dydt = -gamma*y + delta*x*y
    return np.array([dxdt,dydt])

def rk4(f, y0, h):
    t = np.arange(0,100,h)
    n_step = len(t)
    y_values = np.zeros((n_step,len(y0)))
    y_values[0] = y0
    for i in range(n_step -1):
        y = y_values[i]

        k1 = f(t,y)
        k2 = f(t + 0.5*h, y + 0.5*k1*h)
        k3 = f(t + 0.5*h, y + 0.5*k2*h)
        k4 = f(t + h, y + k3*h)

        y_values[i+1] = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    return y_values

solution = rk4(lotka_volterra, y0, 0.05)

plt.figure(figsize=(10,4))
t = np.arange(0,100,0.05)
plt.subplot(1,2,1)
plt.plot(t, solution[:,0], label = 'Prey ($x$)', color = 'blue')
plt.plot(t, solution[:,1], label = 'Predator ($y$)', color = 'red')
plt.xlabel("Time $t$")
plt.ylabel("Time Evolution (RK4)")
plt.grid(True)
plt.legend()

plt.subplot(1,2,2)
plt.plot(solution[:,0], solution[:,1], color="purple")
plt.xlabel("Prey ($x$)")
plt.ylabel("Predator ($y$)")
plt.grid(True)

plt.show()