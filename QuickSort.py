"""
QuickSort simplificado

Escolhe-se um elemento para ser o pivô
A partir dele deivide-se o array
Números menores que o pivô para a esquerda e maiores para a direita

Fazendo isso recursivamente até que esteja ordenado
"""

def QuickSort(array):
    if len(array) < 2:
        return array
    else:
        print("\nEntrando no Quicksort")
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [j for j in array[1:] if j > pivo]
        print(f"Pivô {pivo}",
              f"\nMenores {menores}",
              f"\nMaiores {maiores}")
        return QuickSort(menores) + [pivo] + QuickSort(maiores)
    
print(QuickSort([5,8,4,6,2,7,3,1,9]))