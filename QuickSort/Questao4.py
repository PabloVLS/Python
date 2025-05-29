# Questão 4.– Critique a seguinte tentativa de resolver o problema da separação no algoritmo Quicksort:
# def sep ( array , left , right ) :
#     j = right
#     for i in range ( right - 1 , left - 1 , -1) :
#         if array [ i ] > array [ right ]:
#             array [ i ] , array [ right ] = array [ right ] , array [ i ]
#             j = i
#     return j
# A função acima tenta particionar o vetor array[left..right] utilizando array[right] como pivô.
# No entanto, a implementação apresenta falhas conceituais. Identifique os problemas dessa abordagem,
# comente sobre o funcionamento da lógica de troca e explique por que essa função pode comprometer a
# ordenação corre
import random
def quickSort(array, esquerda, direita):
    if(esquerda < direita):
        pivo = partition(array , esquerda, direita)
        quickSort(array, esquerda, pivo-1)
        quickSort(array, pivo+1, direita)
        return array
    
def partition(array, esquerda , direita):
    j = direita
    for i in range ( direita - 1 , esquerda - 1 , -1) :
        if array [ i ] > array [ direita ]:
            array [ i ] , array [ direita ] = array [ direita ] , array [ i ]
            #j = i
    return j


array =[random.randint(1, 900) for _ in range(900)]
ord = quickSort(array, 0, len(array)-1)
print(ord)


# o erro esta no j=i , pois toda vez fica trocando o pivo , ai da problema