import sys
import os

# Aggiunge il percorso relativo alla cartella che contiene serie.py e libserie.so
sys.path.append('/home/samu1019/MCF/MCF/E10')

# Ora puoi importare il tuo file serie.py come un modulo normale
import serie

# Esempio di utilizzo
n = 10
print(f"Fn: {serie.fib(n)}")
print(f"Rapporto: {serie.fib_ratio(n)}")