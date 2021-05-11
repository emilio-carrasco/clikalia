##Herramienta de recomendación para comerciales de Clikalia.

#Proyecto Mínimo Viable.
Aplicación en python que, dado un identificador de vivienda concreto devuelva una lista de k viviendas parecidas en la hoja de cálculo que acompaña la aplicación.

La información, por ahora, la tenemos contenida en tres ficheros csv:

Geolocalización: Contiene la información geográfica de cada inmueble, ubicación y sitios cercanos, además nos dice la planta del piso, siendo información de gran valor. El id de cada inmueble es su RK. 

Este fichero contiene información  por columnas de latitud y longitud, código postal, país, provincia, ciudad, distrito, barrio, calle, planta, puerta además de información de servicios circundantes: cercanías, centro comercial, escuela, parque, hospital y gimnasio.

De todos los datos, los más relevantes para nuestro proyecto son el barrio y la ubicación geográfica.

En general los datos de información técnica del piso están bastante limpios. Echamos de menos dos pisos sin coordenadas. El barrio habría que unificar lo mejor. Y la  información de servicios adyacentes es bastante.

Características: Contiene la información de las características de cada inmueble, aquí la rk es su identificador que está compuesta por el UV (identificador de localización) y por su estado (1 = sin reformar y 2 = reformado). Se divide pues podemos tener el mismo pisos con diferentes características según su estado. Si existe la entrada de piso reformado habría que desestimar el dato que contendría el mismo piso en versión 1=sin reformar.

Contiene estado, habitaciones, baños, metros, métrica, fecha de construcción, orientación, situación (interior/exterior) y más servicios propios de la vivienda (terraza, piscina, cuarto basura…)

Web: Aquí tenemos el UV y estado con el precio al que se comercializa cada vivienda (algunas viviendas tienen precio antiguo y precio actual con un descuento), para usar esa información de cara al presupuesto del cliente. Además tenemos tipo de vivienda (casa, piso, dúplex, oficina…) y los gastos comunitarios.






Desde la empresa nos comunican que los parámetros a considerar más importantes son: precio, zona, planta y  ascensor.
Mejoras:
#1 Acceso a Azure
Extraer información de las viviendas de la base de datos de Azure de la empresa. Para  ello desarrollaremos una maqueta de la base de datos en un servidor propio de Azure.Utilizaremos bien de la librería SQLalchemy, bien de la librería pyodbc. 

La primera ya la conocemos y no es mala opción (puede ser conveniente explorar la posibilidad de utilizar la BD a través de Alchemy como una clase con sus métodos). 

La segunda, viendo la documentación (es de microsoft) parece que está muy orientada a la comunicación con Azure y puede que le saquemos más rendimiento.

https://docs.microsoft.com/es-es/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver15

#2 Implementar BD propia en Azure
Implementar una base de datos propia para la aplicación, de tal manera que posteriormente se pueda enriquecer esta base de datos con información relevante de los diferentes inmuebles sin variar la base de datos propia de la empresa.

Esta opción incluiría la necesidad de mantener actualizada  la BD propia desde la BD de la empresa. Para ello habría que implementar el control tanto de nuevas añadidas a la BD de la empresa aparezcan en nuestra BD. De la misma manera si una vivienda es vendida o cambia su estado en la BD original, actualizar en consecuencia la propia. 


#3 Enriquecer la base de datos con la información de barrio que nos proporcionan desde clikalia con un shapefile.

Con esta base de datos podremos agrupar de manera precisa nuestros inmuebles y, junto con la información de precio del metro cuadrado por barrio, esta agrupación podrá ser entre viviendas de barrios diferentes pero similares. 

#4.1 Crear un frontend para comerciales
Desarrollar un frontend sencillo que, dada una vivienda concreta por la que se ha interesado un cliente, podamos obtener las viviendas similares del catálogo de la compañía.

#4.2 Implementar una API
Desarrollar una api con las características requeridas. Esto permitiría implementar nuestra aplicación en la web de la empresa o en las comunicaciones por mail con los clientes interesados.

En consecuencia, podríamos pensar en desployear esta api para que pudiera ser accesible por parte de los comerciales. 
#5 Mejora de interfaz.
Hacer una segunda versión mejorada de la interfaz con la que los comerciales trabajarán. De esta manera intentaría mejorar el siguiente flujo de comunicación con el cliente:

¿Qué vivienda ha atraído al cliente?
De esa vivienda qué es lo que  le ha atraído
¿Qué perfil tiene el cliente? Familia, pareja, soltero….
Sugerir viviendas similares a la que que ha atraído al cliente según sus características

#6 Ordenar las viviendas sugeridas en función del interés de venta de la empresa.

Ante resultados de sugerencias puntuadas muy similarmente sugerir al comercial las viviendas sobre las que la empresa tendría más interés en vender. Estos criterios podrían ser: tiempo desde que se cobró o reformó, gastos comunitarios, tiene o no tiene descuento.

#7 Enriquecer la base de datos con Apis. 
A la hora de presentar las sugerencias de nuestro algoritmo al cliente sería un punot a favor presentar directamente al cliente los servicios más interesantes que hay alrededor y qué a qué distancia están. Para ello, a la hora de agregar información en nuestra base de datos podría ser conveniente consultar una api con la que enriquecer la base de datos. 

8# Presentar información al cliente en función de su perfil.
Parece interesante que el comercial pudiera tener  información rápida sobre de 

