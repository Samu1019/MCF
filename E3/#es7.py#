import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_eso= pd.read_csv('/home/samu1019/E3/metodi3/ExoplanetsPars_2025.csv', comment='#')
print(df_eso)
df_eso.columns
df_eso_mol=pd.DataFrame(columns=['r2'])
df_eso_mol['r2']=(np.power((df_eso['pl_orbsmax']),2)/(df_eso['st_mass']))
plt.scatter( df_eso_mol['r2'], df_eso['pl_orbper'])
plt.xscale('log')
plt.yscale('log')
plt.show()

