from  json import load
import pandas as pd

def lee_archivo_json(ruta):
    try:
        with open(ruta) as archivo:
            opcionesjson = load(archivo)
            return opcionesjson
            
    except Exception as ex :
        plantilla = "Ocurrió una excepción de tipo {0}. Argumentos:\n{1!r}"
        mensaje = plantilla.format(type(ex).__name__, ex.args)
        print(mensaje)
        print("Error en: lee_archivo_json")

def lee_archivo_csv(ruta, sep=';'):
    try:
        return pd.read_csv(ruta,sep)
    except Exception as ex :
        plantilla = "Ocurrió una excepción de tipo {0}. Argumentos:\n{1!r}"
        mensaje = plantilla.format(type(ex).__name__, ex.args)
        print(mensaje)

def lee_diccionario_m2(ruta):
    df = pd.read_csv(ruta, sep='|')
    diccionario={}
    for _,r in df.iterrows():
        diccionario[int(r[0])]=float(r[1])
    return diccionario

configuracion = lee_archivo_json('./config/opciones.json')
diccionario_precios_m2 = lee_diccionario_m2('./data/precio_sscc_scrapping.csv')


