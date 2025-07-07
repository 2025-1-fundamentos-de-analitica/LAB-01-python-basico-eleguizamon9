"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_por_letra = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) >= 5:
                letra = parts[0]           # columna 1
                pares = parts[4].split(",")  # columna 5
                suma_valores = sum(int(par.split(":")[1]) for par in pares)

                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + suma_valores

    return dict(sorted(suma_por_letra.items()))