import numpy as np
import scipy 
import matplotlib.pyplot as plt
def p(x):
    return (3*(x**2)/1000)
nsample = 100000
xhm = np.random.uniform(low=0, high=10, size=nsample) 
yhm = np.random.random(nsample) 
maskhm = yhm <= p(xhm)  
plt.scatter(xhm[maskhm], yhm[maskhm], marker='.', color='limegreen')
plt.xlabel('Hit or Miss Selected X')
plt.ylabel('Hit or Miss Selected Y')
plt.show()
def c(x):
    return x**3/1000
def c_inv(y):
    return (1000*y)**(1/3)
xcum = np.random.uniform(low=0, high=1, size=nsample) 
ycum = c_inv(xhm)
fig,ax = plt.subplots(1,1, figsize=(5,5))#, sharex=True)#, sharey=True)
plt.hist(ycum,    bins=100, color='darkorange', label='Valori Cumulativa')
plt.xlabel('Cumulative X')
plt.ylabel('Cumulative Y')
plt.show()
def random_walk2d(step, N):
    deltax = np.array([0])
    deltay = np.array([0])
    tmpx = 0
    tmpy = 0
    check = np.random.random(N)
    for c in check:
        if c >= 0.5:
            tmpx = tmpx+step*np.cos(tmpx)
        else:
            tmpx = tmpx-step*np.cos(tmpx)
        deltax = np.append(deltax, tmpx)
    check2 = np.random.random(N)
    for c in check2:
        if c >= 0.5:
            tmpy = tmpy+step*np.sin(tmpy)
        else:
            tmpy = tmpy-step*np.sin(tmpy)
        deltax = np.append(deltay, tmpy)
    return deltax, deltay
# Liste per gli array con le posizioni dei random walker
xx5 = []
yy5 = []
step=1
Nsteps5 = 100
# Ciclo per calcolo 5 random walk uniformi da 1000 passi 
plt.subplots(figsize=(9,8))
for i in range(5):
    x0,y0 = random_walk2d(step, Nsteps5)
    xx5.append(x0)
    yy5.append(y0)
plt.scatter(x0,y0, s=3)

plt.xlabel(r'$\Delta x$')
plt.ylabel(r'$\Delta y$')
plt.xlim(-200, 200)
plt.ylim(-200, 200)
plt.show()