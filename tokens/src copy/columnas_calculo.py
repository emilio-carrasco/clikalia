
from os import device_encoding
import json

def precio_m2(df):
    with open("./config/preciom2.json") as archivojson:
        dicc = json.load(archivojson)
    dicc={int(k):v for k,v in dicc.items()}
    df['precio_m2'] = df.cusec.replace(dicc)

    return df

def ns(df):
    def es_NS(cadena):
        try:
            CADENA = cadena.upper()
            if 'N' in CADENA: return 'N'
            elif 'S' in CADENA: return 'S'
            else: return ''
        except:
            return ''
    df['ns'] = df.orientacion.apply(es_NS)
    return df

def eo(df):
    def es_EO(cadena):
        try:
            CADENA = cadena.upper()
            if 'E' in CADENA: return 'E'
            elif 'O' in CADENA: return 'O'
            else: return ''
        except:
            return ''

    df['eo'] = df.orientacion.apply(es_EO)
    return df