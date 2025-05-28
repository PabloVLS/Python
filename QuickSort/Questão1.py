# Questão 1.– Escreva uma versão recursiva do algoritmo Quick Sort que ordene um vetor array[incio..f im]
# em ordem decrescente. Sua função deve conter o código da função "partition", considerando que
# os subvetores array[incio..lef t] e array[right..f im] já estejam ordenados de forma decrescente. O
# resultado final também deve ser um vetor decrescente.

def quickSort(array, esquerda=0, direita= None ):
    if(direita is None):
        direita = len(array)-1
    if esquerda < direita:
        pivo = partition(array,esquerda,direita)
        quickSort(array , esquerda, pivo-1)
        quickSort(array, pivo+1, direita)
        return array

def partition(array, esquerda, direita):
    pivo = array[direita]
    i = esquerda - 1

    for j in range(esquerda, direita):
        if(array[j] >= pivo):
            i+=1
            array[i], array[j] = array[j], array[i]

    array[i+1] , array[direita] = array[direita] , array[i+1]
    return i+1



array = [5, 8, 6, 22, 4, 6, 23, 42, 15, 65, 989, 45, 21, 14, 51, 6, 63, 58, 484, 242]
ord = quickSort(array)  
print(ord)