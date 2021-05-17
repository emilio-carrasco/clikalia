
import pandas as pd
from config import variables_en_df, variables_a_calcular, diccionario_agregar, variables_tras_calculos
import columnas_limpieza
import columnas_calculo
import columnas_display
import datos


def lee_archivo_csv(ruta, sep = ';'):
    try:
        return pd.read_csv(ruta,sep)
    except Exception as ex :
        plantilla = "Ocurrió una excepción de tipo {0}. Argumentos:\n{1!r}"
        mensaje = plantilla.format(type(ex).__name__, ex.args)
        print(mensaje)
        
def columnas_limpias(df):
    try:
        for var in variables_en_df:
            limpiador = getattr(columnas_limpieza, var)
            df[var] = df[var].apply(limpiador)    
        return df[variables_en_df]
    except Exception as ex :
        plantilla = "Ocurrió una excepción de tipo {0}. Argumentos:\n{1!r}"
        mensaje = plantilla.format(type(ex).__name__, ex.args)
        print(mensaje)
        print("Error en 'columnas_limpias'")
        
def columnas_texto(df):
    columnas = df.columns
    try:
        columnas = df.columns
        for c in columnas:
            NUEVA=c.upper()
            
            limpiador = getattr(columnas_display, NUEVA)
            df[NUEVA] = df[c].apply(limpiador) 
            #if c==NUEVA:
            #    df[NUEVA.lower] = df[c].apply(limpiador).copy 
             
        return df
    except Exception as ex :
        plantilla = "Ocurrió una excepción de tipo {0}. Argumentos:\n{1!r}"
        mensaje = plantilla.format(type(ex).__name__, ex.args)
        print(mensaje)
        print("Error en 'columnas_texto'")
        
def prepara_df(df):
    df = df.set_index('uv')
    df = datos.columnas_limpias(df)
    df = datos.calcula_variables(df)
    df = datos.agrupar_estado(df)
    df = datos.columnas_texto(df)
    return df

def filtra(df,filtro):
    columnas = [k for k,v in filtro.items() if v]
    return df[columnas]
    
def calcula_variables(df):
    for var in variables_a_calcular:
        calculador = getattr(columnas_calculo, var)
        df = calculador(df)
    return df
    
def agrupar_estado(df):
    def actualiza_diccionario(dicc,col):
        return {c:pd.Series.mode if c in dicc.keys() else 'max' for c in col}

    columnas = df.columns
    diccionario = actualiza_diccionario(diccionario_agregar,columnas)
    return df.groupby('uv', as_index = True).agg(diccionario)

def limpia_df(df):
    df = df.set_index('uv')
    df_limpio = columnas_limpias(df)
    df_calculado = calcula_variables(df_limpio)
    return  agrupar_estado(df_calculado)[variables_tras_calculos]

