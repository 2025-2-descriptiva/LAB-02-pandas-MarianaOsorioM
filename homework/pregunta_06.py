"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_06():

    import pandas as pd 

    df_1 = pd.read_csv(r"files/input/tbl1.tsv", sep="\t")

    #unique devuelve arreglos de numpy, por eso convertí a lista
    return sorted(list(df_1['c4'].str.upper().unique()))

    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
print(pregunta_06())