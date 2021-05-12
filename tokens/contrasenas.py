import sys
import os
from dotenv import load_dotenv, find_dotenv

###Este archivo contiene las funciones y configuraciones para manejar las contraseñas

#cargamos las varibles de entorno
load_dotenv()                       

#añadimos la ruta actual para que sea visible desde la raiz de nuestros archivos
module_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(module_path)


usuario_azure = os.environ.get("usuario_azure")
contrasena_azure = os.environ.get("contrasena_azure")
