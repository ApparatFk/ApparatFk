# Definimos una lista de tuplas
lista_tuplas = [(1, 1), (1, 2), (7, 1), (0, 1)]

# Ordenamos la lista de tuplas por la suma de los elementos de cada tupla
lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda x: sum(x))

print(lista_tuplas_ordenada)

