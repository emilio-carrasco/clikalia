from math import ceil
from columnas_limpieza import barrio
import  config  as conf

#####################################################
def PAIS(p):
    try:return conf.dicc_pais.get(str(p))
    except:return ' '

#####################################################
def PROVINCIA(p):
    try:return conf.dicc_provincia.get(str(int(p)))
    except:return ' '
#####################################################
def DISTRITO(dis):
    try:return dis.upper()
    except:return ' '
#####################################################
def BARRIO(bar):
    try:return bar.upper()
    except:return ' '
#####################################################
def CALLE(c):
    try:return c.upper()
    except:return ' '
#####################################################
def CIUDAD(c):
    try:return c.upper()
    except:return ' '
#####################################################
def PRECIO(p):
    try:return str(int(p)).upper()
    except:return ' '

########################################################
def GASTOS_COMUNITARIOS(g):
    try:return str(int(g)).upper()
    except:return ' '

########################################################
def PLANTA(p):
    try:return str(int(p)).upper()
    except:return ' '

########################################################
def HABITACIONES(h):
    try:return str(int(h)).upper()
    except:return ' '
########################################################
def BANOS(b):
    try:return str(int(b)).upper()
    except:return ' '

########################################################
def METROS(m):
    try:return str(int(m)).upper()
    except:return ' '

########################################################
def FECHA_CONSTRUCCION(a):
    try:return str(int(a)).upper()
    except:return ' '

########################################################
def SITUACION(tipo):
    try:
        situaciones = conf.dicc_num_situ
        tipo = str(int(tipo))
        return situaciones.get(tipo)
    except:
        return ' '

########################################################
def CUSEC(c):
    try:return str(int(c)).upper()
    except:return ' '
########################################################
def PRECIO_M2(p):
    try:return str(int(p)).upper()
    except:return ' '

###################################################################
def GEO(g):
    try:return str(round(g)).upper()
    except:return ' '
##################################################################
def LONG(l):
    try:return str(round(l,3)).upper()
    except:return ' '
########################################################################
def LAT(l):
    try:return str(round(l,3)).upper()
    except:return ' '
########################################################################
def UV(id):
    try:return str(id).upper()
    except:return ' '
########################################################################
def ESTADO_X(e):
    try:return conf.dicc_num_estado.get(str(int(e)))
    except:return ' '
########################################################################
def TIPO_VIVIENDA(t):
    try:return str(t).upper()
    except:return ' '
########################################################################
def ORIENTACION(nseo):
    try:return str(nseo).upper()
    except:return ' '
########################################################################
def NS(ns):
    try:return str(ns).upper()
    except:return ' '
########################################################################
def EO(eo):
    try:return str(eo).upper()
    except:return ' '
########################################################################
def PORTAL(p):
    try:
        if int(p) == 1: return'PORTERO'
        else: return ' '
    except:
        return ' '
########################################################################
def ASCENSOR(a):
    try:
        if int(a) == 1: return'ASCENSOR'
        else: return ' '
    except:
        return ' '

########################################################################
def PARQUE_INFANTIL(p):
    try:
        if int(p) == 1: return'PARQUE INFANTIL'
        else: return ' '
    except:
        return ' '

########################################################################
def TERRAZA(t):
    try:
        if int(t) == 1: return'TERRAZA'
        else: return ' '
    except:
        return ' '

########################################################################
def TRASTERO(T):
    try:
        if int(t) == 1: return'TRASTERO'
        else: return ' '
    except:
        return ' '

########################################################################
def PISCINA_COMUNITARIA(p):
    try:
        if int(p) == 1: return'PISCINA COMUNITARIA'
        else: return ' '
    except:
        return ' '

########################################################################
def CUARTO_DE_BASURA(b):
    try:
        if int(b) == 1: return'CUARTO BASURA'
        else: return ' '
    except:
        return ' '
########################################################################
def ZONAS_COMUNES(z):
    try:
        if int(z) == 1: return'ZONAS COMUNES'
        else: return ' '
    except:
        return ' '
########################################################################
def PISCINA(p):
    try:
        if int(p) == 1: return'PISCINA'
        else: return ' '
    except:
        return ' '
########################################################################
def GARAJE(g):
    try:
        if int(g) == 1: return'GARAJE'
        else: return ' '
    except:
        return ' '

########################################################################
def TEJADO(t):
    try:
        if int(t) == 1: return'TECHO BUARDILLA'
        else: return ' '
    except:
        return ' '
########################################################################
def CALEFACCION(c):
    try:
        if int(c) == 1: return'CALEFACCIÓN'
        else: return ' '
    except:
        return ' '
########################################################################
def JARDIN(j):
    try:
        if int(j) == 1: return'JARDÍN'
        else: return ' '
    except:
        return ' '
########################################################################
def AIRE_ACONDICIONADO(a):
    try:
        if int(a) == 1: return'AIRE ACONDICIONADO'
        else: return ' '
    except: 
        return ' '

########################################################################
def MONEDA(m):
    try: return str(m)
    except: return ' '


########################################################################
def CODIGO_POSTAL(cp):
    try: return str(cp)
    except: return ' '
