"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    
    #Retorne la suma de la segunda columna.

    total = 0
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("\t")  # asumo que el separador es tabulación (\t)
            if len(parts) > 1:  # asegurarse que hay al menos dos columnas
                total += int(parts[1])  # sumar la segunda columna
    return total
    #Rta/
    #214

    
