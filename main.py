#from config.base_datos  import conectar_azure_principal
from src.data_set import lee_limpia_3csv2df

print("Leyendo CSVs")
df=lee_limpia_3csv2df()
print("CSVs converitdos a pd.dataframe")


