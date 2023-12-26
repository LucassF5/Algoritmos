"""
Utilizando recursão, podemos fazer uma função que soma os elementos de uma lista
Esta função vai iterar sobre a lista até que esta esteja vazia
"""

def sumList(lista):
    if lista == []:
        return 0
    else:
        print(lista[1:])
        #lista[1:] retorna a lista sem o primeiro elemento
        #Vai iterar nos elementos restantes da lista até que esta esteja vazia
        return lista[0] + sumList(lista[1:])
        #lista[0] retorna o primeiro elemento da lista e soma com o retorno da função sumList(lista[1:])
        #que retorna a soma dos elementos restantes da lista
    
print(sumList([1,2,3,4,5,6,7,8,9,10]))
print()
print(sumList([10,20,30,40,50]))
