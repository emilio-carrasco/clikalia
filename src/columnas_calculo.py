from config import diccionario_precios_m2


def precio_m2(df):
    def saca_precio(num):
        return diccionario_precios_m2.get(num)
    df['precio_m2'] = df.cusec.apply(saca_precio)
    return df

def NS(df):
    def es_NS(cadena):
        try:
            CADENA = cadena.upper()
            if 'N' in CADENA: return 'N'
            elif 'S' in CADENA: return 'S'
            else: return ''
        except:
            return ''
    df['NS'] = df.orientacion.apply(es_NS)
    return df

def EO(df):
    def es_EO(cadena):
        try:
            CADENA = cadena.upper()
            if 'E' in CADENA: return 'E'
            elif 'O' in CADENA: return 'O'
            else: return ''
        except:
            return ''

    df['EO'] = df.orientacion.apply(es_EO)
    return df