dt = 0.0005 # grid size for time (s)
dy = 0.0005 # grid size for space (m)
viscosity = 2*10**(-4) # kinematic viscosity of oil (m2/s)
y_max = 0.04 # in m
t_max = 1 # total time in s
V0 = 10 #velocity inm/s

# function to calculate velocity profiles based on a
# finite difference approximation to the 1D diffustion
# equation and FTCS scheme:
def diffusion_FTCS(dt,dy,t_max,y_max,viscosity,V)):
    #diffusion number (has to be less than 0.5 for the
    # solution to be stable):
    s = viscosity*dt/dy**2
    y = np.arange(0,y_max+dy,dy)
    t = np.arange(0,t_max+dt,dt)
    r = len(t)
    c = len(y)
    V = np.zeros([r,c])
    V[:,0] = V0
    for n in range(0,r-1): #time
        for j in range(1,c-1): #space
            V[n+1,j] = V[n,j] + s*(V[n,j-1] -
                2*V[n,j] + V[n,j+1])
