import reco
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mod1=pd.read_csv('/home/samu1019/MCF/MCF/E4/moduli/hit_times_M0.csv')
mod2=pd.read_csv('/home/samu1019/MCF/MCF/E4/moduli/hit_times_M1.csv')
mod3=pd.read_csv('/home/samu1019/MCF/MCF/E4/moduli/hit_times_M2.csv')
mod4=pd.read_csv('/home/samu1019/MCF/MCF/E4/moduli/hit_times_M3.csv')
def modarray(modulo,sensore,time):
    return reco.hit(modulo,sensore,time)

hits_mod1 = [modarray(mod1['mod_id'][i], mod1['det_id'][i], mod1['hit_time'][i]) for i in range(len(mod1))]
hits_mod2 = [modarray(mod2['mod_id'][i], mod2['det_id'][i], mod2['hit_time'][i]) for i in range(len(mod2))]
hits_mod3 = [modarray(mod3['mod_id'][i], mod3['det_id'][i], mod3['hit_time'][i]) for i in range(len(mod3))]
hits_mod4 = [modarray(mod4['mod_id'][i], mod4['det_id'][i], mod4['hit_time'][i]) for i in range(len(mod4))]
defi=hits_mod1+hits_mod2+hits_mod3+hits_mod4
arraydef=np.array(defi)
np.sort(arraydef)
print(arraydef)
tdiff=np.diff(arraydef)
plt.hist(
    tdiff,
    bins=1000,
    color='skyblue',
    edgecolor='black'
)
plt.xlabel('Istante Hit')
plt.ylabel('Numero di Hit (Frequenza)')
plt.show()



