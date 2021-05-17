import streamlit as st
from PIL import Image

import pandas as pd
import src.utilidades as ut
import config as conf
import json
import matplotlib.pyplot as plt

def header():
    st.set_page_config(page_title="RECOMENDADOR CLIKALIA", page_icon='./img/clikalia_icono.png', layout='wide', initial_sidebar_state= 'expanded')
    #st.sidebar.text(ut.hora())
    imagen = Image.open("img/clikalia_logo.png")
    st.image(imagen, width=150)
    
def menu_seleccion():
    return st.sidebar.selectbox("MENÜ",("PRINCIPAL","DATOS"))
    
def caja_browser(id):
    archivo = st.file_uploader(id, type=['csv'], key =id)
    if archivo:
        df = pd.read_csv(archivo, sep=";")
        df.to_csv("./config/inmuebles.csv", index=False)
    return

def caja_precio_m2(id):
    archivo = st.file_uploader(id, type=['csv'], key =id)
    if archivo:
        df = pd.read_csv(archivo, sep="|")
        diccionario = dict()
        for _,r in df.iterrows():
            diccionario[int(r[0])] = float(r[1])
        with open("./config/preciom2.json", "w") as archivojson: 
            json.dump(diccionario, archivojson)       

def caja_resultados_busqueda(df):
    if df is None: 
        st.text("No hay Información ")
    else:
        try:
            df_show = df.set_index('uv') #2dohay que arreglar
        except: 
            df_show = df
        #colum_maysc = [c for c in df.columns if c.lower() != c]
        #colum_maysc = [k for k,v in filtro.items() if v]
        colum_maysc = df.columns #2do esto se podría quitar
        st.dataframe(df_show[colum_maysc])
        
def bonito_df_busqueda(df):
    try:
        claves = df.columns
        claves = [c for c in claves if c.lower() != c]
        
        df =  df.applymap(str)[claves] 
        return df.reset_index(level=0)
    except: return None

def caja_filtros(filtro):
    "# FILTROS:"  
    l = len(filtro)
    num_max_columnas = conf.max_filtros
    num_columnas = (l if l <= num_max_columnas else num_max_columnas)
    cols = st.beta_columns(num_columnas)
    for i, (k,v) in enumerate(filtro.items()):
        filtro.update({k:cols[ (i % num_columnas)].checkbox(k,v, key=k, help=None)})
    return filtro

def caja_boton_busqueda(df):
    busqueda = st.sidebar.text_input("Buscar:", "")
    if busqueda: 
        try:     
            df = df.reset_index()
            busqueda = busqueda.split(' ')
            df = df[df.apply(lambda x: ut.buscar(busqueda,list(x)), axis=1 )]
            boton_busqueda=False
            df = df.set_index('uv')
        except:
            "No se puede ejecuatar la búsqueda"
    return df

def barras_pesos(pesos):
    s  = pd.Series(pesos,index=pesos.keys())
    s.sort_values(ascending= False, inplace= True)
    x_values = s.index .str.upper()
    y_values = s.values * 5
    fig = plt.figure(figsize = (20, 2))
    plt.style.use('dark_background')
    plt.xticks(rotation=60)
    plt.ylim([0,5])
    plt.bar(x_values, y_values, color='#F5405C')
    ax = plt.gca()
    ax.patch.set_alpha(0)
    fig.patch.set_alpha(0)
    st.pyplot(fig)
    

def selector_pesos():
    st.sidebar.selectbox("PERFILES",("FAMILIA","PAREJA JOVEN", "SOLTERO"),key='perfiles')
    diccionario_pesos=dict()
    pesos= conf.pesos_finales
    for p in pesos:
        diccionario_pesos[p]=st.sidebar.slider(p.upper(), min_value=0, max_value=5,value= 1,step= 1, key=p)/5
    return diccionario_pesos
