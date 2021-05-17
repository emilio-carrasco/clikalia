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
import streamlit as st
dp.header()
opcion = dp.menu_seleccion()

if  opcion == "DATOS":
        df = dp.caja_browser('Archivo inmuebles')   
        dp.caja_precio_m2('Archivo precio m2')
else:
    try:
        filtro_columnas
    except:
        filtro_columnas = conf.filtro_busqueda

    filtro_columnas = dp.caja_filtros(filtro_columnas)

    try:
        df
    except:
        try:
            df = datos.lee_archivo_csv("./config/inmuebles.csv",sep=',')  
            df_preparados = datos.prepara_df(df)   
        except:
            "### ERROR DATOS"

    df_filtrados = datos.filtra(df_preparados,filtro_columnas)
    df_busqueda = dp.caja_boton_busqueda(df_filtrados)
    dp.caja_resultados_busqueda(df_busqueda) 
    try:
        if len(df_busqueda) == 1:
            target=df_preparados[df_preparados.index.isin(df_busqueda.index)]
            dp.bonito_df_busqueda(df)
            simili = knn.similitud(df_preparados,target)
       
            diccionario_pesos = dp.selector_pesos() 
            dp.barras_pesos(diccionario_pesos)
            col_simili='SIMILITUD'
            df_preparados[col_simili] = knn.pondera(simili,diccionario_pesos)
            df_final = knn.ordena(df_preparados,col_simili)
            df_filtrados = datos.filtra(df_final,filtro_columnas)
            "### INMUEBLES SIMILARES"
            dp.caja_resultados_busqueda(df_filtrados[1:])
        else:
            "### AFINA LA BÚSQUEDA PARA MOSTRAR SIMILITUDES"
    except Exception as e: 
        st.text(e)
        
    

       