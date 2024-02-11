"""
Algoritmo de Dijkstra

O algoritmo de Dijkstra é um algoritmo de busca em grafos que busca 
o caminho mais curto de um vértice origem para todos os outros vértices 
em um grafo com arestas de peso não negativo.

O algoritmo mantém uma lista de vértices para os quais o menor caminho
desde a origem já foi determinado. A cada passo, ele explora um vértice
não incluído na lista, que tem a menor distância da origem.

"""

grafo = {} # Grafo
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = {}

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}


custos = {} # Dicionário de custos
custos["a"] = 6
custos["b"] = 2
custos["fim"] = float("inf") # Infinito

pais = {} # Dicionário de pais
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None


processados = [] # Lista de nós processados


# Função para encontrar o caminho mais curto
def achar_custo_mais_baixo(custos):
    custo_mais_baixo = float('inf')
    no_custo_mais_baixo = None
    for no in custos:
        custo = custos[no]
        if custo < custo_mais_baixo and no not in processados:
            custo_mais_baixo = custo
            no_custo_mais_baixo = no
    return no_custo_mais_baixo


nodo = achar_custo_mais_baixo(custos) # Encontra o nó com o menor custo
while nodo is not None: # Enquanto houver nós para processar
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys(): 
        # Verifica se é mais barato chegar a n vizinho passando por nodo
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo: # Se for, atualiza custo e pai
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo) # Marca nodo como processado
    nodo = achar_custo_mais_baixo(custos) 
    # Encontra o próximo nodo a ser processado

print("Custo do caminho mais curto: ", custos["fim"]) 
# Custo do caminho mais curto