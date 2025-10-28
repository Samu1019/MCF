import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_eso= pd.read_csv('/home/samu1019/ExoplanetsPars_2025.csv', comment='#')
print(df_eso)
df_eso.columns
plt.scatter( df_eso['pl_orbper'], df_eso['pl_bmassj'])
plt.xscale('log')
plt.yscale('log')
plt.show()
