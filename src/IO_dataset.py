
import pandas as pd
from config.config import lee_archivo_csv, configuracion
import src.columnas_limpieza
import src.columnas_calculo


###########################################################################################################################
###########################################################################################################################

def columnas_limpias(df):
    try:
        lista_variables = configuracion['variables_en_df']
        for var in lista_variables:
            limpiador = getattr(src.columnas_calculo, var)
            df[var] = df[var].apply(limpiador)    
        return df[lista_variables]
    except Exception as ex :
        plantilla = "Ocurrió una excepción de tipo {0}. Argumentos:\n{1!r}"
        mensaje = plantilla.format(type(ex).__name__, ex.args)
        print(mensaje)
        print("Error en 'columnas_limpias'")
        
#####################################################
def calcula_variables(lista_var,df):
    for var in lista_var:
        calculador = getattr(src.calculo_columnas, var)
        df = calculador(df)
    return df
#####################################################
def agrupar_estado(df):
    def actualiza_diccionario(diccionario):
        return {clave: (pd.Series.mode  if cadena == "mode" else cadena) for clave, cadena in diccionario.items()}
    diccionario = actualiza_diccionario(configuracion['agrupar'])
    return df.groupby('uv', as_index = True).agg(diccionario)


###########################################################################################################################
###########################################################################################################################
def lee_data_set(ruta):
    
    df = lee_archivo_csv(ruta)
    df = df.set_index('uv')

    df_limpio = columnas_limpias(df)
    df_calculado = calcula_variables(configuracion['variables_a_calcular'], df_limpio)
    return  agrupar_estado(df_calculado)