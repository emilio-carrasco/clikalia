
import pandas as pd
from json import load

def codifica_estado(cadena):
    if not cadena: return '3'
    CADENA = cadena.upper()

    if CADENA !='1' and CADENA !='2': return '3'
    else: return CADENA

def codifica_NS(cadena):
    if not cadena: return ''
    CADENA=cadena.upper()
    if 'NOR' in CADENA: return 'N'
    elif 'SU' in CADENA: return 'S'
    else: return ''

def codifica_EO(cadena):
    CADENA=cadena.upper()
    if 'OES' in CADENA: return 'O'
    elif 'EST' in CADENA: return 'E'
    else: return ''

def codifica_situacion(cadena):
    if not cadena: return lista_situacion.index('OTRO')

    try:
        with open("./config/opciones.json") as archivo:
            opcionesjson = load(archivo)
        lista_situacion = opcionesjson['lista_situacion']
    except :
            raise("Error leyendo 'opciones.json'")
    
    CADENA = cadena.upper()
    if CADENA in lista_situacion: return lista_situacion.index(CADENA)
    else: return lista_situacion.index('OTRO')

    
def codifica_tipo_vivienda(cadena):
    """"
    Esta función abre  el archivo "./config/opciones.json" y obtiene el tipo de viviendas posibles en nuestra base de datos.
    Si no está en esa lista devuelve el valor "OTRO"
    Arg: cadena de tipo string

    Return: string conteniendo el tipo de vivienda permitida
    """
    try:
        with open("./config/opciones.json") as archivo:
            opciones = load(archivo)
        grupo_inmuebles = set(opciones['lista_inmuebles'])
    except :
            raise("Error leyendo 'opciones.json'")

    CADENA = cadena.upper()
    if CADENA in grupo_inmuebles: return CADENA
    elif CADENA == 'MORAIDA': return 'CASA' #alguna casa del dataset venía con la palabra MORAIDA y parece un error hemos decidido hardcodear por ser algo concreto.
    else: return 'OTRO'
    
def codifica_texto_mas_frecuente(x):
    if x.empty or x.isnull().all():
        return ''
    else: 
        x = x.dropna()
        return x.mode()
    
def lee_archivos_csv():
    df_geo = pd.read_csv('./data/geolocalizacion.csv', sep=';')
    df_car = pd.read_csv('./data/caracteristicas.csv', sep=';')
    df_web = pd.read_csv('./data/web.csv', sep=';')
    return df_geo, df_car,df_web

def selecciona_columnas_interes(df_geo, df_car, df_web):
    df_geo = df_geo[['rk', 'latitud', 'longitud', 'pais', 'provincia', 'ciudad', 'distrito', 'barrio', 'calle', 'planta']]
    df_geo.columns = ['uv', 'latitud', 'longitud', 'pais', 'provincia','ciudad', 'distrito', 'barrio', 'calle', 'planta']

    df_car = df_car[['uv', 'estado', 'habitaciones', 'banos','metros','fecha_construccion','orientacion','situacion', 'portal', 'ascensor', 'parque_infantil', 'terraza', 'trastero', 'piscina_comunitaria', 'cuarto_de_basura','zonas_comunes', 'piscina', 'garaje', 'tejado', 'calefaccion', 'jardin', 'aire_acondicionado']]
    
    df_web = df_web[['uv', 'tipo_vivienda', 'precio', 'gastos_comunitarios']]
    
    return df_geo, df_car, df_web



def limpia_car(df):
    df.estado=df.estado.apply(codifica_estado)
    df['NS']=df.orientacion
    df['EO']=df.orientacion

    df['NS']=df['orientacion'].apply(codifica_NS)
    df['EO']=df['orientacion'].apply(codifica_EO)
    df.drop(['orientacion'], axis=1, inplace= True)
    
    df[[ 'estado', 'habitaciones', 'banos', 'metros','fecha_construccion', 'tejado']] = df[[ 'estado', 'habitaciones', 'banos', 'metros','fecha_construccion', 'tejado']].fillna(0).astype(int)
    df[['portal', 'ascensor','parque_infantil', 'terraza', 'trastero', 'piscina_comunitaria', 'cuarto_de_basura', 'zonas_comunes', 'piscina', 'garaje', 'tejado','calefaccion','jardin', 'aire_acondicionado']] = df[['portal', 'ascensor','parque_infantil', 'terraza', 'trastero', 'piscina_comunitaria', 'cuarto_de_basura', 'zonas_comunes', 'piscina', 'garaje', 'tejado','calefaccion','jardin', 'aire_acondicionado']].fillna(0).astype(int)
    
    df.situacion=df.situacion.fillna('OTRO').apply(codifica_situacion)
    
    df = df.groupby('uv', as_index=False).agg(
    {
    'estado': 'max',
    'habitaciones': 'max',
    'banos': 'max',
    'metros': 'max',
    'fecha_construccion': 'max',
    'NS': codifica_texto_mas_frecuente,
    'EO': codifica_texto_mas_frecuente,
    'situacion': 'max',
    'portal': 'max',
    'ascensor': 'max',
    'parque_infantil': 'max',
    'terraza': 'max',
    'trastero': 'max',
    'piscina_comunitaria': 'max',
    'cuarto_de_basura': 'max',
    'zonas_comunes': 'max',
    'piscina': 'max',
    'garaje': 'max',
    'tejado': 'max',
    'calefaccion': 'max',
    'jardin': 'max',
    'aire_acondicionado': 'max',
    }
    )     
    df.drop(df.loc[df['estado']==3].index, inplace=True)
    #eliminamos los estado==3 (normalmente deberían ser los vendidos)
    df.set_index('uv', inplace=True)
    return df



def limpia_web(df):   
    df = df.groupby('uv', as_index=False).agg(
    {
    'tipo_vivienda': codifica_texto_mas_frecuente,
    'precio': 'max',
    'gastos_comunitarios': 'max',
    }
    )     
    #limpiamos el df fijando tipo de vivienda, poniendo el precio de la vivienda en miles de euros K, pasando estado a 1 sin reformar, 2 reformado, 3 vendido. usamos int
    df.tipo_vivienda = df.tipo_vivienda.apply(codifica_tipo_vivienda)
    df.precio =  df.precio.fillna(0)
    df.precio =  (df.precio/1000)

    df.gastos_comunitarios =  df.gastos_comunitarios.fillna(0).astype(int)
    #renombramos las nuevas variables
    df.columns=['uv', 'tipo_vivienda', 'precio_k', 'gastos_comunitarios']
    #las coordenadas vienen multiplicadas por 100
    #2do incluit este ajuste en el json
    df.set_index('uv', inplace=True)
    return df

def limpia_geo(df):
    df = df.groupby('uv', as_index=False).agg(
        {
        'latitud': 'max',
        'longitud': 'max',
        'pais': 'max',
        'ciudad': codifica_texto_mas_frecuente,
        'distrito': codifica_texto_mas_frecuente,
        'calle': codifica_texto_mas_frecuente,
        'barrio': codifica_texto_mas_frecuente,
        'planta': 'max',
        }
    )     

    df.set_index('uv', inplace=True)

    df[['latitud', 'longitud']]=df[['latitud', 'longitud']]/100
    return df

def une_df(df_car, df_web, df_geo):
    df=df_car.join(df_geo, how='outer').join(df_web, how='outer')
    #al hacer el join pueden aparecer nan que rellenamos con ceros y nos aseguramos de que mantenga el formato int.
    df.fillna(int(0), inplace= True)
    df.precio_k = df.precio_k.astype(int)
    return df

def lee_limpia_3csv2df():
    df_geo, df_car,df_web = lee_archivos_csv()
    df_geo, df_car,df_web = selecciona_columnas_interes(df_geo, df_car,df_web)
    df_car = limpia_car(df_car)
    df_web = limpia_web(df_web)
    df_geo = limpia_geo(df_geo)
    return une_df(df_car, df_web, df_geo)

