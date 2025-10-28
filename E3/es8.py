import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_eso= pd.read_csv('/home/samu1019/E3/metodi3/ExoplanetsPars_2025.csv', comment='#')
print(df_eso)
df_eso.columns
ss_orbper  = np.array( [ 88, 225, 365, 687, 4333, 10759, 30687, 60190])
ss_orbsmax = np.array( [ 0.47, 0.73, 1.02, 1.67, 5.45, 10.07, 20.09, 30.32])
ss_bmasse = np.array( [ 0.06, 0.82, 1.0, 0.11, 317.89,  95.17, 14.56, 17.24, ] )
ss_bmassj = ss_bmasse/317.89
df_radvel=df_eso.loc[df_eso['discoverymethod']=='Radial Velocity']
df_transit=df_eso.loc[df_eso['discoverymethod']=='Transit']
plt.scatter(df_radvel['pl_bmassj'], df_radvel['pl_orbper'], 
            color='coral', alpha=0.4, label='Radial Velocity')
plt.scatter(df_transit['pl_bmassj'], df_transit['pl_orbper'], 
            color='skyblue', alpha=0.4, label='Transit')
plt.scatter(ss_orbper, ss_bmassj, color='slategray', label='Solar System')
plt.xlabel('Massa [M_J]')
plt.ylabel('Periodo [giorni]')
plt.legend(['Radial Velocity', 'Transit'])
plt.xscale('log')
plt.yscale('log')
plt.show()