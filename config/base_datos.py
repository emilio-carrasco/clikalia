from tokens.contrasenas import usuario_azure, contrasena_azure
from json import load
import pyodbc

import os

def conectar_azure(selector_base_datos):
    """Esta función conectará con la BD de Azure. 
    Para ello recurrira al archivo config.ajuste_db.json datos para determinar el server a conectar. 
    
    Además recurrirá a las variables de entorno almacenadas en .env para obtener el password de la
    conexión.

    config.ajuste_db.json debería contener:
    {
        "principal": {  
                        "servidor": "clikalia-sql.database.windows.net",
                        "base_datos":"Clickalia"
                    },
                    
        "metadatos":{  
                        "servidor": "clikalia-sql.database.windows.net",
                        "base_datos":"Metadatos"
                    }
    }
    Args:       
        base_datos (tipo string): Esta cadena debe contener la clavea acceder en el diccionario 
        de config.ajuste_bd.json para elegir a qué base de datos conectarser
            Valores: "principal" / "metadatos"

    Returns:
        cursor: manejador de la base de datos que se ha abierto
    """
    with open("./config/ajustes_db.json") as archivo:
        configuracion = load(archivo)

    servidor = configuracion[selector_base_datos]["servidor"]
    base_datos = configuracion[selector_base_datos]["base_datos"]
    drivers=pyodbc.drivers()
    conexion_cadena="DRIVER={"+ drivers[-1] + "}; Server=" + servidor + "; Database=" + base_datos + "; UID=" + usuario_azure + "; PWD=" + contrasena_azure + "; " 
    print(conexion_cadena)
    conexion = pyodbc.connect(conexion_cadena)
    return conexion.cursor()

def conectar_azure_principal():
    """Esta funcion llama a la función 'conectar_azure' para conectarse a la base de datos con metadatos
    
    Returns:
        cursor: manejador de la base de datos que se ha abierto
    """
    return conectar_azure("principal")

def conectar_azure_metadatos():
    """Esta funcion llama a la función 'conectar_azure' para conectarse a la base de datos con metadatos

    Returns:
        cursor: manejador de la base de datos que se ha abierto
    """
    return conectar_azure("metadatos")
