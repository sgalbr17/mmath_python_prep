import numpy as np
import matplotlib.pyplot as plt

#Parameters
L = 1.0
N = 100
dx = L/(N-1)
D = 0.01

dt = 0.4 * (dx**2)/D #ensures dt < dx^2/2D
t_final = 1.0
n_step = int(t_final/dt)

x = np.linspace(0,L,N)

#Initial conditions
u = np.exp(-100*(x-0.5)**2)
u_initial = u.copy()

#Main code
gamma = D*dt/(dx**2) #dimensionless parameter

checkpoints = [0, int(n_step*0.1), int(n_step*0.3), n_step]
saved_states = {}

for n in range(n_step+1):
    if n in checkpoints:
        saved_states[n] = u.copy()
    u_new = u.copy()

    #Interior update
    u_new[1:-1] = u[1:-1] + gamma*(u[2:]-2*u[1:-1]+u[:-2])
    #Boundary conditions: u_0 = u_1 and u_N = u_{N-1}
    u_new[0] = u_new[1]
    u_new[-1] = u_new[-2]
    u = u_new

for step, state in saved_states.items():
    time_val = step*dt
    plt.plot(x, state, label = f't = {time_val:.3f} s')

plt.xlabel("Spatial Position ($x$)")
plt.ylabel("Temperature ($u$)")
plt.grid(True, linestyle = '--', alpha =0.6)
plt.legend()
plt.tight_layout()
plt.show()
