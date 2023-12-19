"""
SELECTION SORT

A ordenação por seleção faz uma busca pelo menor valor e adiciona um por vez ao array auxiliar
Assim, fazendo buscas recursivas pelo array original até que o segundo esteja ordenado

"""

def buscaMenor(array):
    menor=array[0] 
    menor_indice=0

    for i in range(1, len(array)):
        if array[i] < menor: 
            menor = array[i]
            menor_indice = i
    return menor_indice

def selectionSort(array):
    novoArray = []

    for i in range(len(array)):
        menor = buscaMenor(array)
        novoArray.append(array.pop(menor))
    return novoArray

print(selectionSort([2,6,43,86,23,57,1,9]))