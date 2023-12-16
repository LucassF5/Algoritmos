"""
Implementando código de pesquisa binária

Este método consiste em dividir a lista escolhida ao meio e buscar em sublistas
Diminuindo o tempo de busca e evitando uma procura no array inteiro

O método de pesquisa binária recebe a lista a ser percorrida e o elemento a ser procurado
Faz uma busca na lista da sequinte forma:
Inicia com duas variáveis, alto e baixo
Na qual a variável "alto" significa o tamanho do array a ser percorrido por vez
O método entra no laço while, o qual vai percorrer o array de busca
Este que será uma metade da lista requisitada
Ele reparte o array pela metade gerando a variável meio

A função usa a variável chute, que vai ser o elemento central
Se o elemento a ser procurado for achado ele retorna a posição deste
Caso o chute estiver acima, ele atualiza a variável alto e novamente testa o meio dessa sublista
Caso for menor, atualiza a variável alto e faz o mesmo procedimento
E caso o elemento não esteja na lista, retorna None

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
