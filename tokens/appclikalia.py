import sys
sys.path.insert(1, './src')
sys.path.insert(1, './tokens')
sys.path.insert(1, './data')
sys.path.insert(1, './config')
sys.path.insert(1, './tokens')
sys.path.insert(1, './display')
sys.path.insert(1, './display')

import display as dp
import config as conf
import knn
import datos

#abre el wexplorador al abrir la app
import explorador

dp.header()
try:
    filtro_cajas 
except:
    filtro_cajas = conf.filtro_busqueda

filtro_cajas = dp.caja_filtros(filtro_cajas)

df = dp.caja_browser('Archivo inmuebles')   
dp.caja_precio_m2('Archivo precio m2')
try:
    df_preparados = datos.prepara_df(df)
    df_mostrar_busqueda = dp.bonito_df_busqueda(df_preparados)
    df_mostrar_busqueda = dp.caja_boton_busqueda(df_mostrar_busqueda)
    dp.caja_resultados_busqueda(df_mostrar_busqueda)
except: pass

try:
    l= len(df_mostrar_busqueda)
except:
    l=int(0)

if l == 1:
    target=df_preparados.iloc[df_mostrar_busqueda.index]
    df_mostrar_busqueda = dp.bonito_df_busqueda(df)
    simili = knn.similitud(df_preparados,target)

    ################################################################################
    from random import random, randint
    #escogemos la fila i como objetivo que lo hacemos aleatorio para nuestras pruebas
    #generamos un filtro aleatorio
    diccionario_pesos = {p : round(random(), 2) for p in conf.pesos_finales}
    ####################################################################################
 
    col_simili='SIMILITUD'
    df_preparados[col_simili] = knn.pondera(simili,diccionario_pesos)
    df_final = knn.ordena(df_preparados,col_simili)
    "# INMUEBLES SIMILARES"
    dp.caja_resultados_busqueda(df_final[1:])