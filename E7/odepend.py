import numpy as np
from  scipy import integrate 
import matplotlib.pyplot as plt
l  = 0.5
theta_0  = 45
omega_0=0
def drdt_pendolo(r,t):
    dxdt = r[1]
    dydt = -(9.8/l)*np.sin(r[0])
    return (dxdt, dydt)
time_vec = np.linspace(0, 10, 100000)
yinit = (theta_0, omega_0)
yarr  = integrate.odeint(drdt_pendolo, yinit, time_vec)
plt.plot(time_vec, yarr[:,0], markersize=4, color='red', 
         label='Ampiezza Massima (Numerica)')
plt.show()