import numpy as np
import matplotlib.pyplot as plt

#Parameters
L = 1
N = 100
dx = L/(N-1)
dy = dx
D = 0.01 #diffusion coeff.

#2D stability condition: dt < dx^2/(4D)
dt = 0.2*(dx**2) / (4*D)
t_final = 0.
n = int( t_final /dt)

#Grid
x = np.linspace(0,L,N)
y = np.linspace(0,L,N)
X, Y = np.meshgrid(x,y)

#Initial condition
u = np.exp(-50*((X-0.5)**2 + (Y-0.5)**2))

for step in range(n):
    u_new = u.copy()
    laplacian = ( u[2:,1:-1] + u[:-2,1:-1] + u[1:-1, :-2] - 4*u[1:-1, 1:-1])/(dx**2)
    u_new[1:-1,1:-1] = u[1:-1, 1:-1] = u[1:-1,1:-1] + dt*D*laplacian
    u_new[0,:] = u_new[-2,:]
    u_new[-1,:] = u_new[1,:]
    u_new[:,0] = u_new[:, -2]
    u_new[:,-1] = u_new[:,1]

    u = u_new


plt.imshow(u, extent=[0,L,0,L], origin = 'lower', cmap ='inferno')
plt.colorbar(label = 'Concentration ($u$)')
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.show()
