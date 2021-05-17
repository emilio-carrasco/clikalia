import sys
sys.path.insert(1, './src')
sys.path.insert(1, './tokens')
sys.path.insert(1, './data')
sys.path.insert(1, './config')
sys.path.insert(1, './tokens')


import display as dp
import config as conf
import knn
import datos

#abre el wexplorador al abrir la app
import explorador

dp.header()
opcion = dp.menu_seleccion()

if  opcion == "DATOS":
        df = dp.caja_browser('Archivo inmuebles')   
        dp.caja_precio_m2('Archivo precio m2')
else:
    try:
        filtro_cajas 
    except:
        filtro_cajas = conf.filtro_busqueda
    filtro_cajas = dp.caja_filtros(filtro_cajas)
    try:
        df
    except:
        try:
            df = datos.lee_archivo_csv("./config/inmuebles.csv",sep=',')  
            #df = dp.caja_boton_busqueda(df) 
            df_preparados = datos.prepara_df(df)
            
        except:
            "#NO HAY DATOS CARGADOS"   
    df_mostrar_busqueda = dp.bonito_df_busqueda(df_preparados)
    df_mostrar_busqueda = dp.caja_boton_busqueda(df_mostrar_busqueda)
    dp.caja_resultados_busqueda(df_mostrar_busqueda) 
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
        import streamlit as st
        st.text(diccionario_pesos)
        
        ####################################################################################
        col_simili='SIMILITUD'
        df_preparados[col_simili] = knn.pondera(simili,diccionario_pesos)
        df_final = knn.ordena(df_preparados,col_simili)
        "# INMUEBLES SIMILARES"
        dp.caja_resultados_busqueda(df_final[1:])