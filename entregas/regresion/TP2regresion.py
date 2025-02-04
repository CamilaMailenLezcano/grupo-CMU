import pandas as pd
import numpy as np
import statsmodels.api as sm

!pip install pyreadstat

import pyreadstat
file_path ='entregas/BASEDATOS_ARGENTINA_122.sav'

df_diputados, meta = pyreadstat.read_sav(file_path)

df_diputados = df_diputados.loc[~((df_diputados['ID101'] == 98) |
                                   (df_diputados['ID101'] == 99) |
                                   (df_diputados['PRO102'] == 98) |
                                   (df_diputados['PRO112'] == 99))]
                                   
print (df_diputados.columns.tolist()) #Se pide el nombre de todas las columnas
print(meta.column_labels) #¿Cuales son las etiquetas de las columnas?


##REGRESIÓN 1 ##
# Quiero saber cuales son las preguntas para  cada columna
columnas_interes = ['PRO109', 'DEM5']
for columna in columnas_interes:
    if columna in df_diputados.columns:
        print(f"{columna}: {meta.column_labels[df_diputados.columns.get_loc(columna)]}")
    else:
        print(f"La columna {columna} no existe en el DataFrame.")

Y = df_diputados['PRO109'] #importancia corrupcion
X = df_diputados['DEM5'] #funcionamiento democracia 

X = sm.add_constant (X)

modelo = sm.OLS(Y, X). fit()

print(modelo.summary())

##REGRESIÓN 2 ##

#cuales son las preguntas para  cada columna

columnas_interes = ['CLIMA201', 'SOCD5']
for columna in columnas_interes:
    if columna in df_diputados.columns:
        print(f"{columna}: {meta.column_labels[df_diputados.columns.get_loc(columna)]}")
    else:
        print(f"La columna {columna} no existe en el DataFrame.")


Y = df_diputados['CLIMA201'] #clima
X = df_diputados['SOCD5'] # edad

X = sm.add_constant (X)

modelo = sm.OLS(Y, X). fit()

print(modelo.summary())

##REGRESIÓN 3##

#Quiero saber cuales son las preguntas para  cada columna 

columnas_interes = ['SOCD4', 'RE1']
for columna in columnas_interes:
    if columna in df_diputados.columns:
        print(f"{columna}: {meta.column_labels[df_diputados.columns.get_loc(columna)]}")
    else:
        print(f"La columna {columna} no existe en el DataFrame.")

Y = df_diputados['RE1']   #Si es religioso
X = df_diputados['SOCD4'] # Sexo

X = sm.add_constant (X)

modelo = sm.OLS(Y, X). fit()

print(modelo.summary())
