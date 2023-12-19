def buscaMenor(array):
    menor=array[0] #Seta como o primeiro índice do array
    menor_indice=0 #seta 0 para ser um elemento menor inicial

    for i in range(1, len(array)):
        if array[i] < menor: 
# Se o elemento da posição for menor do que o da variável menor ele define as variáveis com seu valor
            menor = array[i]
            menor_indice = i
    return menor_indice