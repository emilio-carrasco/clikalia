from  json import load
import pandas as pd

def lee_archivo_json(ruta):
    
    try:
        with open(ruta) as archivo:
            opcionesjson = load(archivo)
            return opcionesjson
            
    except Exception as ex :
        plantilla = "Ocurrió una excepción de tipo {0}. Argumentos:\n{1!r}"
        mensaje = plantilla.format(type(ex).__name__, ex.args)
        print(mensaje)
        print("Ruta: ",ruta)
        print("Error en: lee_archivo_json")


configuracion = lee_archivo_json('./config/opciones.json')

variables_solo_generadoras = configuracion['variables_solo_generadoras']
variables_geo = configuracion['variables_geo']

variables_en_df_numericas = [k for k,v in configuracion['variables_en_df'].items() if v== 'numerica']
variables_en_df_categoricas = [k for k,v in configuracion['variables_en_df'].items() if v== 'categorica']
variables_en_df = variables_en_df_numericas + variables_en_df_categoricas

variables_a_calcular_numericas = [k for k,v in configuracion['variables_a_calcular'].items() if v== 'numerica']
variables_a_calcular_categoricas = [k for k,v in configuracion['variables_a_calcular'].items() if v== 'categorica']
variables_a_calcular = variables_a_calcular_numericas +variables_a_calcular_categoricas

variables_tras_calculos_numericas = variables_a_calcular_numericas + [v for v in variables_en_df_numericas if not v in set(variables_solo_generadoras)]
variables_tras_calculos_catergoricas = variables_a_calcular_categoricas + [v for v in variables_en_df_categoricas if not v in set(variables_solo_generadoras)]
variables_tras_calculos = variables_tras_calculos_numericas + variables_tras_calculos_catergoricas

variables_finales_numericas = [v for v in variables_tras_calculos_numericas if not v in set(variables_geo)]
variables_finales_categoricas = [v for v in variables_tras_calculos_catergoricas if not v in set(variables_geo)]
variables_finales = variables_finales_numericas + variables_finales_categoricas

pesos_finales = variables_finales + ['geo']
diccionario_agregar = configuracion['agrupar']

filtro_busqueda = configuracion['filtro_busqueda']

tipo_vivienda  = configuracion['tipo_vivienda']
dicc_pais = configuracion['dicc_pais']
dicc_provincia = configuracion['dicc_provincia']
dicc_num_situ = configuracion['dicc_num_situ']
dicc_situ_num = configuracion['dicc_situ_num']
dicc_num_estado = configuracion['dicc_num_estado']