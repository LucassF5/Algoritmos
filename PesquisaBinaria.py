"""
A pesquisa binária é um algoritmo de busca eficiente utilizado em conjuntos de dados ordenados. 
O processo ocorre da seguinte forma:

Condição Inicial: O algoritmo começa com todo o conjunto de dados ordenado.

Comparação: O algoritmo compara o elemento a ser encontrado com o elemento no meio do conjunto.

Divisão do Conjunto: Se o elemento for igual ao do meio, a busca é concluída. 
Caso contrário, o conjunto é dividido ao meio, e a busca continua na metade apropriada, 
descartando a metade onde o elemento não pode estar.

Repetição: Os passos 2 e 3 são repetidos na metade restante do conjunto 
até que o elemento seja encontrado ou o conjunto seja reduzido a zero.

A principal vantagem da pesquisa binária é a sua eficiência, 
pois a cada comparação, o conjunto de dados é reduzido pela metade. 
No entanto, é importante notar que a pesquisa binária só funciona em conjuntos de dados ordenados.
"""

def pesquisaBinaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1,3,5,6,7,8,9,10,11]

teste = pesquisaBinaria(minha_lista,1)

print(teste)
