from datetime import datetime

def hora():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M)")
    return timestampStr
    
def buscar(lista_busqueda,lista_datos):
    for b in lista_busqueda:
        if not any(b.upper() in d.upper() for d in lista_datos):
            return False            
    return True

