import pandas as pd
import json
from math import radians
import numpy as np


def haversine(d, t):
    t = t.loc[t.index.repeat(len(d))]
    indice = d.index
    t.reset_index(drop=True, inplace=True)
    d.reset_index(drop=True, inplace=True)
    
    lon1 = d.long
    lat1 = d.lat
    lon2 = t.long
    lat2 = t.lat
    

    lat1 = lat1.map(radians)
    lon1 = lon1.map(radians)
    lat2 = lat2.map(radians)
    lon2 = lon2.map(radians)


    #lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 
    km = 6371* c
    return km

def calc_ascensor(da,dp,ta,tp):
    try:
        if da ==1 and ta ==1: 
            distancia_ascensor = 10
        elif da ==0 and ta == 0: 
            distancia_ascensor= (dp-tp) * ((dp-tp)>0)
        elif da==0 and ta==1:
            if dp < 2: 
                distancia_ascensor = 9
            else:
                distancia_ascensor = dp
        elif da==1 and ta==0:
            distancia_ascensor = 8
        else:
            distancia_ascensor= 7
    except:
        distancia_ascensor=6
    return distancia_ascensor


def normaliza(df):
    return df.abs()/df.max()
    

def get_top_similar(df,target, opciones, k):
    filtros=opciones['filtros']
    for f in filtros:
        if f!="bajo_no":
            dato = target.iloc[0][f]
            indice = df[ df[f] != dato ].index
        else:
            indice = df[df['planta'] == 0 ].index

        df.drop(indice, axis=0, inplace=True)
        #df.drop(f,axis=1, inplace=True)

    ###calculamos geo
    distancia_geo = haversine(df[['long','lat']], target[['long','lat']])

    distancia_normalizada=distancia_geo/distancia_geo.max()
    similitud_geo=1-distancia_normalizada
    similitud_geo.index=df.index
    similitud_geo=pd.DataFrame(similitud_geo)
    similitud_geo.columns=["geo"]

    ###calculamos asecensor
    distancia_ascensor=df.apply(lambda row: calc_ascensor(row['ascensor'], row['planta'], target.ascensor[0],target.planta[0]),axis=1)
    distancia_normalizada=normaliza(distancia_ascensor)
    similitud_ascensor=1-distancia_normalizada

    #binarias
    binarias =opciones['binarias']
    df_binarias=df[binarias]
    target_binarias = target[binarias].loc[target.index.repeat(len(df_binarias))]
    target_binarias.index=df_binarias.index
    iguales=target_binarias==df_binarias
    distintas=target_binarias!=df_binarias
    s_binarias=pd.Series(binarias)
    similitud_binarias= iguales.dot(s_binarias) + distintas.dot(1-s_binarias)

        #diferenca_positiva
    diferenca_positiva =opciones['diferenca_positiva']
    df_diferenca_positiva=df[diferenca_positiva]
    target_diferenca_positiva = target[diferenca_positiva].loc[target.index.repeat(len(df_diferenca_positiva))]
    target_diferenca_positiva.index=df_diferenca_positiva.index
    distancia_diferenca_positiva=(df_diferenca_positiva-target_diferenca_positiva)
    k=2
    distancia_diferenca_positiva[distancia_diferenca_positiva<0]=distancia_diferenca_positiva*k
    distancia_diferenca_positiva=distancia_diferenca_positiva.abs()
    distancia_normalizada=normaliza(distancia_diferenca_positiva)
    similitud_diferenca_positiva=1-distancia_normalizada

    ##diferenca_negativa
    diferenca_negativa =opciones['diferenca_negativa']
    df_diferenca_negativa=df[diferenca_negativa]
    target_diferenca_negativa = target[diferenca_negativa].loc[target.index.repeat(len(df_diferenca_negativa))]
    target_diferenca_negativa.index=df_diferenca_negativa.index
    distancia_diferenca_negativa=(df_diferenca_negativa-target_diferenca_negativa)
    k=2
    distancia_diferenca_negativa[distancia_diferenca_negativa>0]=distancia_diferenca_negativa*k
    distancia_diferenca_negativa=distancia_diferenca_negativa.abs()

    distancia_normalizada=normaliza(distancia_diferenca_negativa)
    similitud_diferenca_negativa=1-distancia_normalizada

    ##diferenca_lineal
    diferencia_lineal =opciones['diferencia_lineal']
    diferencia_lineal={k:v for k,v in diferencia_lineal.items() if  k!="geo"}
    df_diferencia_lineal=df[diferencia_lineal]
    target_diferencia_lineal = target[diferencia_lineal].loc[target.index.repeat(len(df_diferencia_lineal))]
    target_diferencia_lineal.index=df_diferencia_lineal.index
    distancia_diferencia_lineal=(df_diferencia_lineal-diferencia_lineal)
    distancia_diferencia_lineal=distancia_diferencia_lineal.abs()
    distancia_normalizada=normaliza(distancia_diferencia_lineal)
    similitud_diferencia_lineal=1-distancia_normalizada
    pesos_neg=pd.Series(opciones['diferenca_negativa'])
    pesos_pos=pd.Series(opciones['diferenca_positiva'])
    peso_lin=pd.Series(opciones['diferencia_lineal'])
    pesos=pd.concat([pesos_neg,pesos_pos,peso_lin], axis=0)
    pesos=pd.DataFrame(pesos).transpose()
    similitud=pd.concat([similitud_geo,similitud_diferencia_lineal,similitud_diferenca_positiva, similitud_diferenca_negativa], axis=1)
    pesos=pesos.sort_index(axis=1).reset_index(drop=True)
    similitud=similitud.sort_index(axis=1)
    simil_ordenada=similitud.fillna(0).dot(pesos.transpose())[0].sort_values(ascending=False)
    return df.loc[simil_ordenada[0:3].index]