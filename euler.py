import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

dt = 0.5
t = np.arange(0,5,dt)
y = np.zeros(len(t))

y[0] = 1

for i in range(len(t)-1):
    f = -2*y[i]
    y[i+1] = y[i] + f*dt

exact_sol = np.exp(-2*t) #exact solution

plt.plot(t,y, 'o-', label = 'Euler\'s Method')
plt.plot(t, exact_sol, '--', label = 'Exact Solution')
plt.legend()
plt.show()