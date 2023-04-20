import pandas as pd

import os
import pandas as pd

folder_path = 'C:/Users/FRANK-PC/Documents/GitHub/RNN_v1/Preprocessing'

df_list = []
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_excel(file_path)
        df_list.append(df)

def buscar_palabras(df, palabras):
    """
    Esta función busca las palabras dadas en el dataframe df y devuelve un nuevo dataframe con las líneas que contienen esas palabras.
    """
    # Crear un dataframe vacío para almacenar las líneas encontradas
    df_encontrado = pd.DataFrame(columns=df.columns)

    # Iterar sobre cada fila del dataframe
    for index in df_encontrado.index:
        # Convertir la fila a una cadena de texto
        texto = str(df_encontrado.iloc[index, 1])

        # Buscar las palabras en el texto
        if any(palabra in texto for palabra in palabras):
            # Agregar la fila al dataframe encontrado
            df_encontrado = df_encontrado.append(row)

    # Guardar el dataframe encontrado en un archivo Excel
    df_encontrado.to_excel('encontrado.xlsx', index=False)

    return df_encontrado

DISTANCE_PREFIX = ['Km.', 'KM.', 'Km', 'KM', 'K.', 'k.', 'kilometro', 'Kilometro', 'KILOMETRO', 'K\M', 'K/M', 'k/m',
                   'k\m']

df_encontrado = buscar_palabras(df_list[2], DISTANCE_PREFIX)
