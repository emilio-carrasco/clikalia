
import pandas as pd
from json import load

def lee_archivos_csv(ruta):
    return pd.read_csv(ruta, sep=';')

def selecciona_columnas_interes(df):

    
    df_geo = df_geo[['rk', 'latitud', 'longitud', 'pais', 'provincia', 'ciudad', 'distrito', 'barrio', 'calle', 'planta']]
    df_geo.columns = ['uv', 'latitud', 'longitud', 'pais', 'provincia','ciudad', 'distrito', 'barrio', 'calle', 'planta']

    df_car = df_car[['uv', 'estado', 'habitaciones', 'banos','metros','fecha_construccion','orientacion','situacion', 'portal', 'ascensor', 'parque_infantil', 'terraza', 'trastero', 'piscina_comunitaria', 'cuarto_de_basura','zonas_comunes', 'piscina', 'garaje', 'tejado', 'calefaccion', 'jardin', 'aire_acondicionado']]
    
    df_web = df_web[['uv', 'tipo_vivienda', 'precio', 'gastos_comunitarios']]
    
    return df_geo, df_car, df_web
def lee_limpia_csv_pisos():
    df_pisos = lee_archivos_csv('./data/geolocalizacion.csv')
    df_geo, df_car,df_web = selecciona_columnas_interes(df_pisos)