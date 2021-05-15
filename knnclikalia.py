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

def principal():
    print("Leyendo CSVs")
    ruta = './data/datos_pisos.csv'
    df = lee_data_set(ruta)
    print("CSVs converitdos a pd.dataframe")
    ####################################################################################
    from random import random, randint
    #escogemos la fila i como objetivo que lo hacemos aleatorio para nuestras pruebas
    #i = round(random() * len(df))
    i = randint(0, len(df)-1)
    target = df.iloc[[i]]
    df.index[i]
    #generamos un filtro aleatorio



    diccionario_pesos = {p : round(random(), 2) for p in pesos_finales}

    ####################################################################################
    ####################################################################################

    sim = similitud(df, target)
    df_ponderado_ordenado = pondera(sim, diccionario_pesos)
    return df_ponderado_ordenado

if __name__ == "__main__":
    principal()
