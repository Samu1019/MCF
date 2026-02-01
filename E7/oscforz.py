import numpy as np
from  scipy import integrate 
import matplotlib.pyplot as plt
m_molla  = 0.2
k_molla  = 2  
c_visc   = 0.5 
gamma  = c_visc / (2 * m_molla)
omega0 = np.sqrt(k_molla/ m_molla)
omegaf=omega0
def F(t):
    return (2*np.sin(omegaf*t))
def drdt_molla(r,t, g, o,F):
    dxdt = r[1]
    dydt = -2 * g * r[1] - o**2 *r[0]+F(t)/m_molla
    return (dxdt, dydt)
time_vec = np.linspace(0, 10, 100000)
yinit = (0, 0)
yarr  = integrate.odeint(drdt_molla, yinit, time_vec, args=(gamma, omega0,F))

plt.plot(time_vec, yarr, markersize=4, color='red', 
         label='Ampiezza Massima (Numerica)')
plt.show()
def F1(t, omegaf_val):
    return (2 * np.sin(omegaf_val * t))
def drdt_molla1(r,t, omegaf_val, g, o, F1):
    dxdt = r[1]
    dydt = -2 * g * r[1] - o**2 *r[0] + F1(t, omegaf_val)/m_molla # Usa m_molla globale
    return (dxdt, dydt)
omegaf_vec = np.linspace(0.1, 2.0 * omega0, 50)
ampiezze_max_risultati = []
time_vec = np.linspace(0, 40, 2000)
yinit = (0, 0)
for omegaf_val in omegaf_vec:
    yarr1 = integrate.odeint(
        drdt_molla1, 
        yinit, 
        time_vec, 
        args=(omegaf_val, gamma, omega0, F1) 
    )
    x_posizioni = yarr1[:, 0]
    A_max = np.max(np.abs(x_posizioni))
    ampiezze_max_risultati.append(A_max)
plt.plot(omegaf_vec, ampiezze_max_risultati, markersize=4, color='red', 
         label='Ampiezza Massima (Numerica)')
plt.show()