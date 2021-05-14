#from config.base_datos  import conectar_azure_principal
from collections import defaultdict
import sys
sys.path.insert(1, './src')
sys.path.insert(1, './tokens')
sys.path.insert(1, './data')
sys.path.insert(1, './config')

from src.data_set import lee_limpia_3csv2df
from src.knn import similitud, pondera


print("Leyendo CSVs")
df = lee_limpia_3csv2df()
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

lista_pesos = ['habitaciones', 'banos', 'metros', 'fecha_construccion', 'situacion',
       'planta', 'precio_k', 'gastos_comunitarios', 'geo', 'estado', 'NS',
       'EO', 'portal', 'ascensor', 'parque_infantil', 'terraza', 'trastero',
       'piscina_comunitaria', 'cuarto_de_basura', 'zonas_comunes', 'piscina',
       'garaje', 'tejado', 'calefaccion', 'jardin', 'aire_acondicionado']
diccionario_pesos = {p : round(random(), 2) for p in lista_pesos}

#########################################################################################

sim = similitud(df, target)
df_ponderado_ordenado = pondera(sim, diccionario_pesos)
print(df_ponderado_ordenado)