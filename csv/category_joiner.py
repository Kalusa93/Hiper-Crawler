import os
import pandas as pd

def combinar_csv(archivos_csv, archivo_salida):
    # Lista para almacenar los DataFrames de cada archivo CSV
    dataframes = []

    # Leer cada archivo CSV y agregar su DataFrame a la lista
    for archivo in archivos_csv:
        if archivo.endswith('.csv'):
            df = pd.read_csv(archivo)
            dataframes.append(df)

    # Combinar todos los DataFrames en uno solo
    resultado = pd.concat(dataframes, ignore_index=True)

    # Guardar el DataFrame combinado en un nuevo archivo CSV
    resultado.to_csv(archivo_salida, index=False)
    print(f'Se ha combinado correctamente en "{archivo_salida}".')

# Lista de archivos CSV que quieres combinar
archivos_a_combinar = ['Aire libre y jardín/Aire_libre_y_jardin_branch_id_12.csv', 'Bebidas/bebidas_branch_id_12.csv']

# Nombre del archivo de salida combinado
archivo_salida_combinado = 'archivo_combinado.csv'

# Llamar a la función para combinar los archivos
combinar_csv(archivos_a_combinar, archivo_salida_combinado)
