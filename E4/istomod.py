import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mod1=pd.read_csv('/home/samu1019/MCF/MCF/E4/moduli/hit_times_M0.csv')
mod2=pd.read_csv('/home/samu1019/MCF/MCF/E4/moduli/hit_times_M1.csv')
mod3=pd.read_csv('/home/samu1019/MCF/MCF/E4/moduli/hit_times_M2.csv')
mod4=pd.read_csv('/home/samu1019/MCF/MCF/E4/moduli/hit_times_M3.csv')
plt.hist(
    mod1['hit_time'], 
    bins=10000,
    color='skyblue',
    edgecolor='black'
)
plt.xscale('log')
plt.xlabel('Istante Hit')
plt.ylabel('Numero di Hit (Frequenza)')
plt.show()
