import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_kplr= pd.read_csv('/home/samu1019/kplr010666592-2011240104155_slc.csv')
print(df_kplr)
df_kplr.columns
df_kplr_min = df_kplr.loc[ (df_kplr['TIME'] >= 945.36) & (df_kplr['TIME'] <= 946.61)]
plt.errorbar(df_kplr_min['TIME'],df_kplr_min['SAP_FLUX'],df_kplr_min['SAP_FLUX_ERR'],fmt='.' )
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
