from pylab import *
from scipy.integrate import odeint
import numpy as np

N = 1000
y = zeros ([2])

L_o = 1.0 # unstretched spring length
#L= 1.0 # inital stretch of spring
v_o = 0.0 # initial velocity
omega_o = 0.0 # initial angular velocity
theta_o = 0.3

y[0] = theta_o # set initial state
y[1] = v_o

time = linspace(0, 10, N)

gravity = 9.8

def pendulum (y, time):
    g0 = y[1]
    g1 = -gravity/L_o *sin(y[0])
    return np.array([g0,g1])

answer = odeint (pendulum, y, time)

plt.plot(time,answer[:,0],label='numeric solution')
plt.plot(time, theta_o * np.cos(np.sqrt(gravity/L_o) * time), label="simple harmonic montion")
plt.xlabel('Time',fontsize=12)
plt.ylabel('Amplitud',fontsize=12)
plt.legend(loc='upper right', shadow=False, fontsize = 10)
plt.show()

