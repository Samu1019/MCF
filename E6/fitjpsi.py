import numpy as np
import pandas as pd
import scipy
from scipy import optimize as optimize
import matplotlib.pyplot as plt
dataset = pd.read_csv('/home/samu1019/MCF/MCF/E6/Jpsimumu.csv')
print(dataset)
def invmass(E1,E2,px1,px2,py1,py2,pz1,pz2):
    return np.sqrt(np.power(E1+E2,2)-(np.power(px1+px2,2)+np.power(py1+py2,2)+np.power(pz1+pz2,2)))
invmassdf = pd.DataFrame(invmass(dataset['E1'],dataset['E2'],dataset['px1'],dataset['px2'],dataset['py1'],dataset['py2'],dataset['pz1'],dataset['pz2']))
print(invmassdf)
indice_max = invmassdf[0].idxmax()
limite_inferiore = indice_max - 500
limite_superiore = indice_max + 499
fig, ax = plt.subplots(figsize=(8, 6))
N1, BINS1, _ = ax.hist(invmassdf[0], bins=1000, range=(2, 4), color='gray', alpha=0.6, label='Istogramma Massa Invariante')
#plt.show()
print(invmassdf.loc[limite_inferiore:limite_superiore, 0])
N2, BINS2, _ = ax.hist(invmassdf.loc[limite_inferiore:limite_superiore, 0], bins=1000, range=(2, 4), color='gray', alpha=0.6, label='Istogramma Massa Invariante')
#plt.show()
X_FIT = (BINS1[:-1] + BINS1[1:]) / 2
Y_FIT = N1
def gausslin(x, A, m, sigma,p1, p0):
    gauss= A * np.exp(-((x - m)**2) / (2 * sigma**2))
    lin = p1 * x + p0
    return gauss + lin
A_start = Y_FIT.max()                       # Altezza del picco (Conteggio)
m_start = X_FIT[Y_FIT.argmax()]             # Posizione X del picco (Massa)
sigma_start = 0.05                          # Stima ragionevole della larghezza in GeV
p1_start = 0.0                              # Pendenza (stimata a zero)
p0_start = 1
pstart = np.array([A_start, m_start, sigma_start, p1_start,p0_start])
params, params_covariance = optimize.curve_fit(gausslin, X_FIT, Y_FIT, p0=pstart)
y=gausslin(X_FIT, params[0], params[1], params[2], params[3],params[4])
print('params', params )
print('params_cov', params_covariance)
print('errori params', np.sqrt(params_covariance.diagonal()))
ax.plot(X_FIT, y)
ax.plot(X_FIT, invmassdf.loc[limite_inferiore:limite_superiore, 0])
plt.show()