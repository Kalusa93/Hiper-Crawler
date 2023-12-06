import pandas as pd

def combinar_csv(archivos_csv, archivo_salida):
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

archivos_a_combinar = [
    'Aire libre y jardín/Aire_libre_y_jardin_branch_id_12.csv',
    'Almacén/Almacen_branch_id_12.csv',
    'Bebés y Niños/Bebes_y_ninos_branch_id_12.csv',
    'Bebidas/bebidas_branch_id_12.csv', 
    'Carnes/Carnes_branch_id_12.csv',
    'Congelados/Congelados_branch_id_12.csv', 
    'Deportes/Deportes_branch_id_12.csv',
    'Electrodomésticos/Electrodomésticos_branch_id_12.csv', 
    'Hogar/Hogar_branch_id_12.csv',
    'Lácteos/Lácteos_branch_id_12.csv',
    'Limpieza/Limpieza_branch_id_12.csv',
    'Mascotas/Mascotas_branch_id_12.csv',
    'Papelería/libreria-y-papeleria_branch_id_12.csv',
    'Pastas frescas y tapas/Pastas_y_tapas_branch_id_12.csv',
    'Perfumería/Perfumeria_branch_id_12.csv',
    'Quesos y Fiambres/Quesos_fiambres_branch_id_12.csv',
    'Taeq/Taeq_branch_id_12.csv',
    'Tecnología/Tecnología_branch_id_12.csv',
    'Vehículos/Vehículos_branch_id_12.csv'
    ]

archivo_salida_combinado = 'Hiper_Libertad_Sucursal_SDE_completo.csv'

combinar_csv(archivos_a_combinar, archivo_salida_combinado)
