"""
Um algoritmo recursivo para encontrar o maior valor em uma lista
"""

def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:])
    #lista[1:] retorna a lista sem o primeiro elemento
    return lista[0] if lista[0] > sub_max else sub_max
    # A função maximo(lista[1:]) vai retornar o maior valor da lista

print(maximo([24,54,76,23.7,1,65,8]))