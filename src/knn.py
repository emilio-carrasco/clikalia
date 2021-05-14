import sys
from numpy.lib.function_base import diff


import pandas as pd
import numpy as np

from src.data_set import lee_limpia_3csv2df


def similitud_numericas(df,target):
    var_numericas = ['habitaciones', 'banos', 'metros', 'fecha_construccion', 'situacion', 'planta', 'precio_k','gastos_comunitarios']
    df_num = df[var_numericas]
    target_num  = target[var_numericas]
    diferencia= df_num.sub(target_num.iloc[0,:]).abs()
    diferencia_normalizada = diferencia/diferencia.sum()
    similitud = 1 - diferencia_normalizada
    return similitud

def haversine_vectorize(d, t):
    t = t.loc[t.index.repeat(len(d))]
    indice = d.index
    t.set_index(indice, inplace=True)

    lon1 = d.longitud
    lat1 = d.latitud

    lon2 = t.longitud
    lat2 = t.latitud
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 
    
    km = 6371* c
    return km

def similitud_geo(df, target):
    var_geo = ['latitud','longitud']
    df_geo = df[var_geo]
    target_geo = target[var_geo]
    distancia = haversine_vectorize(df_geo, target_geo)
    distancia_normalizada = distancia / distancia.max()
    similitud = 1 - distancia_normalizada
    return similitud

def similitud_categoricas(df,target):
    var_categoricas=['estado', 'NS','EO', 'portal', 'ascensor', 'parque_infantil', 'terraza','trastero', 'piscina_comunitaria', 'cuarto_de_basura','zonas_comunes','piscina', 'garaje', 'tejado', 'calefaccion', 'jardin','aire_acondicionado']
    df_cat = df[var_categoricas]
    target_cat = target[var_categoricas]
    target_cat = target_cat.loc[target_cat.index.repeat(len(df))]
    indice=df_cat.index
    target_cat.set_index(indice, inplace=True)
    return (df_cat == target_cat).astype(int)

def similitud(df,target):
    sim_num = similitud_numericas(df,target)
    sim_geo = similitud_geo(df, target)
    sim_cat = similitud_categoricas(df,target)
    sim_num['geo'] = sim_geo
    similitud = sim_num.join(sim_cat)   
    return similitud
    

def pondera(df,pesos):
    serie_pesos = pd.Series(pesos)
    serie_pesos_normalizados = serie_pesos/serie_pesos.sum()
    df['similitud']=round(df.dot(serie_pesos_normalizados),3)
    return df.sort_values(by='similitud', ascending= False)