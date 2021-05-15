from math import ceil
from config import configuracion

#####################################################
def precio(cantidad, redondeo = 1000):
    try:
        if not cantidad or cantidad < redondeo: return None
        else: return float(ceil(cantidad/redondeo))

    except:
        return None

########################################################
def gastos_comunitarios(gastos):
    try:
        return float(gastos)

    except:
        return None

########################################################
def planta(num_planta):
    try:
        return float(num_planta)
    except:
        return None

########################################################
def habitaciones(num_habitaciones):
    try:
        if not num_habitaciones: return None
        else: return float(num_habitaciones)

    except:
        return None
    
########################################################
def banos(num_banos):
    try:
        if not num_banos: return None
        else: return float(num_banos)

    except:
        return None

########################################################
def metros(num_metros):
    try:
        if not num_metros: return None
        else: return float(num_metros)

    except:
        return None

########################################################
def fecha_construccion(ano):
    try:
        if not ano or ano < 1900: return None
        else: return float(ano)

    except:
        return None

########################################################
def situacion(tipo):
    try:
        situaciones = configuracion['diccionario_situacion']
        TIPO = tipo.upper()
        if TIPO in situaciones.keys(): return situaciones.get(TIPO)
        else: return None
    except:
        return None

########################################################
def cusec(num_cusec):
    try:
        if not num_cusec: return None
        else: return int(num_cusec)
    except:
        return None

########################################################
def precio_m2():
    return None

###################################################################
def geo():
    return None
##################################################################
def long(l):
    try:
        if not l: return None
        else: return float(l)
    except:
        return None
########################################################################
def lat(l):
    try:
        if not l: return None
        else: return float(l)
    except:
        return None
########################################################################
def uv(id):
    try:
        #2do aquí podríamos hacerle un regex
        if not id: return None
        else: return id
    except:
        return None
########################################################################
def estado_x(estado):
    try:
        if int(estado) != 1 and int(estado) != 2: 
            return None
        else: 
            
            return int(estado)
    except:
        return None
########################################################################
def tipo_vivienda(tipo):
    try:
        TIPO = tipo.upper()
        conjunto_tipos = configuracion.get('tipo_vivienda')
        if TIPO == 'MORAIDA': return 'CASA' #alguna casa del dataset venía con la palabra MORAIDA y parece un error hemos decidido hardcodear por ser algo concreto.
        if not TIPO or TIPO not in conjunto_tipos: return None
        else: return TIPO
    except:
        return None
########################################################################
def orientacion(nseo):
    ori=str()
    try:
        NSEO = nseo.upper()
        if not NSEO: return None
        if 'NOR' in NSEO: ori+='N'
        elif 'SU' in NSEO: ori+='S'

        if 'OES' in NSEO: ori+='O'
        elif 'EST' in NSEO: ori+='E'

        return ori
    except:
        return None
########################################################################
def NS():
    return None

########################################################################
def EO():
    return None

########################################################################
def portal(portero):
    try:
        if int(portero) != 1 and int(portero) != 0: return None
        else: return int(portero)
    except:
        return 
        
########################################################################
def ascensor(asc):
    try:
        if int(asc) != 1 and int(asc) != 0: return None
        else: return int(asc)
    except:
        return None

########################################################################
def parque_infantil(parque):
    try:
        if int(parque) != 1 and int(parque) != 0: return None
        else: return int(parque)
    except:
        return None

########################################################################
def terraza(terra):
    try:
        if int(terra) != 1 and int(terra) != 0: return None
        else: return int(terra)
    except:
        return None

########################################################################
def trastero(tras):
    try:
        if int(tras) != 1 and int(tras) != 0: return None
        else: return int(tras)
    except:
        return None

########################################################################
def piscina_comunitaria(pisci):
    try:
        if int(pisci) != 1 and int(pisci) != 0: return None
        else: return int(pisci)
    except:
        return None

########################################################################
def cuarto_de_basura(bas):
    try:
        if int(bas) != 1 and int(bas) != 0: return None
        else: return int(bas)
    except:
        return None
########################################################################
def zonas_comunes(zona):
    try:
        if int(zona) != 1 and int(zona) != 0: return None
        else: return int(zona)
    except:
        return None
########################################################################
def piscina(pisci):
    try:
        if int(pisci) != 1 and int(pisci)!= 0: return None
        else: return int(pisci)
    except:
        return None
########################################################################
def garaje(gar):
    try:
        if int(gar) != 1 and int(gar) != 0: return None
        else: return int(gar)
    except:
        return None
########################################################################
def cuarto_de_basura(bas):
    try:
        if int(bas) != 1 and int(bas) != 0: return None
        else: return int(bas)
    except:
        return None
########################################################################
def tejado(bua):
    try:
        if int(bua) != 1 and int(bua)!= 0: return None
        else: return int(bua)
    except:
        return None
########################################################################
def calefaccion(cal):
    try:
        if int(cal) != 1 and int(cal) != 0: return None
        else: return int(cal)
    except:
        return None
########################################################################
def jardin(jar):
    try:
        if int(jar) != 1 and int(jar) != 0: return None
        else: return int(jar)
    except:
        return None
########################################################################
def aire_acondicionado(air):
    try:
        if int(air) != 1 and int(air) != 0: return None
        else: return int(air)
    except:
        return None

