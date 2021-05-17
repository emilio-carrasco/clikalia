
import pandas as pd
from config import variables_en_df, variables_a_calcular, diccionario_agregar, variables_tras_calculos
import columnas_limpieza
import columnas_calculo


###########################################################################################################################
###########################################################################################################################


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
        
#####################################################
def calcula_variables(df):
    for var in variables_a_calcular:
        calculador = getattr(columnas_calculo, var)
        df = calculador(df)
    return df
#####################################################
def agrupar_estado(df):
    def actualiza_diccionario(diccionario):
        return {clave: (pd.Series.mode  if cadena == "mode" else cadena) for clave, cadena in diccionario.items()}
    diccionario = actualiza_diccionario(diccionario_agregar)
    return df.groupby('uv', as_index = True).agg(diccionario)


###########################################################################################################################
###########################################################################################################################
def lee_data_set(ruta):
    df = lee_archivo_csv(ruta)
    df = df.set_index('uv')
    df_limpio = columnas_limpias(df)
    df_calculado = calcula_variables(df_limpio)
    return  agrupar_estado(df_calculado)[variables_tras_calculos]

def limpia_df(df):
    df = df.set_index('uv')
    df_limpio = columnas_limpias(df)
    df_calculado = calcula_variables(df_limpio)
    return  agrupar_estado(df_calculado)[variables_tras_calculos]

