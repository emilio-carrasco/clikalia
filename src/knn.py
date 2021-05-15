import pandas as pd
import numpy as np
from config import *

def similitud_numericas(df,target):
    df_num = df[variables_finales_numericas].copy()

    target_num  = target[variables_finales_numericas]
    diferencia= df_num.sub(target_num.iloc[0,:]).abs()
    diferencia_normalizada = diferencia/diferencia.sum()
    similitud = 1 - diferencia_normalizada
    return similitud

def haversine(d, t):
    t = t.loc[t.index.repeat(len(d))]
    indice = d.index
    t.set_index(indice, inplace=True)

    lon1 = d.long
    lat1 = d.lat

    lon2 = t.long
    lat2 = t.lat
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 
    
    km = 6371* c
    return km

def similitud_geo(df, target):

    df_geo = df[variables_geo]
    target_geo = target[variables_geo]
    distancia = haversine(df_geo, target_geo)
    distancia_normalizada = distancia / distancia.max()
    similitud = 1 - distancia_normalizada
    return similitud

def similitud_categoricas(df,target):
    df_cat = df[variables_finales_categoricas]
    target_cat = target[variables_finales_categoricas]
    target_cat = target_cat.loc[target_cat.index.repeat(len(df))]
    indice=df_cat.index
    target_cat.set_index(indice, inplace=True)
    return (df_cat == target_cat).astype(int)

def similitud(df,target):
    print(df.columns)
    sim_num = similitud_numericas(df,target)
    sim_geo = similitud_geo(df, target)
    sim_cat = similitud_categoricas(df,target)
    try:
        sim_num['geo'] = sim_geo
    except:
        pass
    similitud = sim_num.join(sim_cat)   
    return similitud
    

def pondera(df,pesos):
    serie_pesos = pd.Series(pesos)
    serie_pesos_normalizados = serie_pesos/serie_pesos.sum()

    df['similitud'] = df.fillna(0).dot(serie_pesos_normalizados)
    return df.sort_values(by = 'similitud', ascending= False)