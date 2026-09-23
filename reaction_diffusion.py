import numpy as np
import matplotlib.pyplot as plt
#Fisher-KPP Equation

#Parameters
L = 100.0
N = 500
dx = L/(N-1)
D = 1.0 #Diffusion coeff.
r = 1.0 #Growth rate

c = 2*np.sqrt(D*r) #Theoretical minimum wave speed
print(f"Theoretical minimum wave speed c = {c:.3f}")

#Time step satisfying the von Neumann stability for diffusion
dt = 0.4*(dx**2)/(2*D)
t_final = 25.0
n_step = max(1,int(t_final/dt))

x = np.linspace(0,L,N)

#Initial Conditions
u = np.zeros(N)
u[x<=10] = 1 #Population density u=1 in x \in [0,10] and u=0 everywhere else

#Main code
gamma = D*dt/(dx**2)
interval  = int(n_step/5)
saved = {}

for n in range(n_step +1):
    if n%interval == 0:
        saved[n] = u.copy()
    u_new = u.copy()
    #Diffusion term
    diffusion = gamma*(u[2:] - 2*u[1:-1] + u[:-2])
    #Reaction term
    reaction = dt*r*u[1:-1]*(1-u[1:-1])

    u_new[1:-1] = u[1:-1] + diffusion + reaction

    #Boundary conditions
    u_new[0] = u_new[1]
    u_new[-1] = u_new[-2]

    u = u_new

print(f"DEBUG: Shape of x is {x.shape}")
for step, state in saved.items():
    print(f"DEBUG: Shape of state at step {step} is {state.shape}")


for step, state in saved.items():
    time_val = step * dt
    plt.plot(x, state, label = f't = {time_val:.1f} s', linewidth = 2)


plt.xlabel("Spatial Position ($x$)")
plt.ylabel("Population Density ($u$)")
plt.grid(True, linestyle = '--', alpha = 0.6)
plt.legend()
plt.tight_layout()
plt.show()