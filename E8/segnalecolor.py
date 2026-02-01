import sys, os
import numpy as np
import pandas as pd
from scipy import constants, fft, optimize
import matplotlib.pyplot  as plt
import argparse
def noisef(f, N, beta):    
    return N/f**beta
df1 = pd.read_csv('/home/samu1019/MCF/MCF/E8/data_sample1.csv')
df2 = pd.read_csv('/home/samu1019/MCF/MCF/E8/data_sample2.csv')
df3 = pd.read_csv('/home/samu1019/MCF/MCF/E8/data_sample3.csv')

print('DF1', df1.columns)
print('DF2', df2.columns)
print('DF3', df3.columns)

plt.plot(df1['time'], df1['meas'])
#plt.show()
plt.plot(df2['time'], df2['meas'])
#plt.show()
plt.plot(df3['time'], df3['meas'])
#plt.show()
dt1 = df1['time'][1]-df1['time'][0]
dt2 = df2['time'][1]-df2['time'][0]
dt3 = df3['time'][1]-df3['time'][0]
c1  = fft.fft(df1['meas'].values)
f1  = fft.fftfreq(len(c1), d=dt1)
c2  = fft.fft(df2['meas'].values)
f2  = fft.fftfreq(len(c2), d=dt2)
c3  = fft.fft(df3['meas'].values)
f3  = fft.fftfreq(len(c3), d=dt3)

pv1, pc1 = optimize.curve_fit(noisef , f1[2:len(c1)//2], np.absolute(c1[2:len(c1)//2])**2, p0=[1, 1])
print('Parameters Fit Sample 1', pv1)
pv2, pc2 = optimize.curve_fit(noisef , f2[5:len(c2)//2], np.absolute(c2[5:len(c2)//2])**2, p0=[1, 1])
print('Parameters Fit Sample 2', pv2)
pv3, pc3 = optimize.curve_fit(noisef , f3[5:len(c3)//2], np.absolute(c3[5:len(c3)//2])**2, p0=[1, 1])
print('Parameters Fit Sample 3', pv3)
plt.style.use('dark_background')
fig,ax = plt.subplots(figsize=(9,6))
plt.plot( f1[:len(c1)//2], np.absolute(c1[:len(c1)//2])**2, color='white',  label=r'Sample 1 - $\beta$ = {:1.2f} $\pm$ {:1.2f}'.format(pv1[1], np.sqrt(pc1[1,1])) )
plt.plot( f2[:len(c2)//2], np.absolute(c2[:len(c2)//2])**2, color='pink'  , label=r'Sample 2 - $\beta$ = {:1.2f} $\pm$ {:1.2f}'.format(pv2[1], np.sqrt(pc2[1,1])) )
plt.plot( f3[:len(c3)//2], np.absolute(c3[:len(c3)//2])**2, color='tomato', label=r'Sample 3 - $\beta$ = {:1.2f} $\pm$ {:1.2f}'.format(pv3[1], np.sqrt(pc3[1,1])) )

plt.plot( f1[1:len(c1)//2], noisef(f1[1:len(c1)//2], pv1[0], pv1[1] ), color='slategray' )
plt.plot( f2[1:len(c2)//2], noisef(f2[1:len(c2)//2], pv2[0], pv2[1] ), color='magenta'   )
plt.plot( f3[1:len(c3)//2], noisef(f3[1:len(c3)//2], pv3[0], pv3[1] ), color='darkred'   )

plt.legend(fontsize=14, frameon=False)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('f [Hz]')
plt.ylabel(r'$\left| c_k\right|^2$')
plt.show()

