import sys
sys.path.insert(1, './src')
sys.path.insert(1, './tokens')
sys.path.insert(1, './data')
sys.path.insert(1, './config')
sys.path.insert(1, './tokens')

from src.knn import similitud, pondera
from src.IO_dataset import lee_data_set
from config.config import configuracion

####################################################################################
####################################################################################

print("Leyendo CSVs")
ruta = './data/datos_pisos.csv'
df = lee_data_set(ruta)
print("CSVs converitdos a pd.dataframe")

####################################################################################
import random
#escogemos la fila i como objetivo que lo hacemos aleatorio para nuestras pruebas
#i = round(random() * len(df))
i=7
target = df.iloc[[i]]
df.index[i]
#generamos un filtro aleatorio
from random import random

pesos= configuracion['agrupar']
lista_pesos = ['habitaciones', 'banos', 'metros', 'fecha_construccion', 'situacion',
       'planta', 'precio_k', 'gastos_comunitarios', 'geo', 'estado', 'NS',
       'EO', 'portal', 'ascensor', 'parque_infantil', 'terraza', 'trastero',
       'piscina_comunitaria', 'cuarto_de_basura', 'zonas_comunes', 'piscina',
       'garaje', 'tejado', 'calefaccion', 'jardin', 'aire_acondicionado']
diccionario_pesos = {p : round(random(), 2) for p in lista_pesos}

####################################################################################
####################################################################################

sim = similitud(df, target)
df_ponderado_ordenado = pondera(sim, diccionario_pesos)
print(df_ponderado_ordenado)