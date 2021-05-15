import sys
sys.path.insert(1, './src')
sys.path.insert(1, './tokens')
sys.path.insert(1, './data')
sys.path.insert(1, './config')
sys.path.insert(1, './tokens')

from src.knn import similitud, pondera
from src.IO_dataset import lee_data_set
from config import *

####################################################################################
####################################################################################

print("Leyendo CSVs")
ruta = './data/datos_pisos.csv'
df = lee_data_set(ruta)
print("CSVs converitdos a pd.dataframe")
####################################################################################
from random import random
#escogemos la fila i como objetivo que lo hacemos aleatorio para nuestras pruebas
#i = round(random() * len(df))
i=7
target = df.iloc[[i]]
df.index[i]
#generamos un filtro aleatorio



diccionario_pesos = {p : round(random(), 2) for p in pesos_finales}

####################################################################################
####################################################################################

sim = similitud(df, target)
df_ponderado_ordenado = pondera(sim, diccionario_pesos)
print(df_ponderado_ordenado)