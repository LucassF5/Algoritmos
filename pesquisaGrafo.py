from collections import deque
#  Deque = Double Ended Queue

"""
Um grafo é uma estrutura matemática que consiste em um conjunto de vértices 
(também chamados de nós) e um conjunto de arestas que conectam esses vértices. 
Ele é usado para representar relações entre objetos. 

A pesquisa em largura (BFS) explora todos os vizinhos de um nó 
antes de avançar para os vizinhos dos vizinhos, 
usando uma fila para garantir essa ordem. 

O código fornece uma função chamada pessoa_e_vendedor(nome) que retorna True 
se o último caractere do nome dado for "m", indicando que é um vendedor.

A função pesquisa(nome) realiza uma busca em largura (BFS) em um grafo
para encontrar um vendedor. Começando com a pessoa inicial 
especificada pelo nome, ela itera sobre as conexões do grafo usando uma 
fila de pesquisa (fila_de_pesquisa). A cada iteração, retira um elemento da 
fila e verifica se é um vendedor usando a função pessoa_e_vendedor(nome). 
Se for um vendedor, a função retorna True; caso contrário, adiciona os vizinhos 
dessa pessoa à fila de pesquisa e marca a pessoa como verificada.

Se não encontrar nenhum vendedor após percorrer todas as conexões possíveis, 
a função retorna False.
"""

grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggym"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

def pessoa_e_vendedor(nome):
    return nome[-1] == "m"

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(f"{pessoa} é um(a) vendedor(a)")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False
    
pesquisa("voce")