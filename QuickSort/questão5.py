# Questão 5.– Seja array[1..4] o vetor 77 55 33 99. Se executar quicksort(array, left, right),
# você verá a seguinte sequência de invocações:
# quicksort(array,1,4)
# quicksort(array,1,2)
# quicksort(array,1,0)
# quicksort(array,2,2)
# quicksort(array,4,4)
# Repita o exercício com o vetor array[1..6] = 55 44 22 11 66 33.
def quickSort(array, esquerda, direita):
    print(f"quicksort(array, {esquerda+1}, {direita+1})")
    
    if esquerda < direita:
        pivo = partition(array, esquerda, direita)
        quickSort(array, esquerda, pivo - 1)
        quickSort(array, pivo + 1, direita)
    return array

def partition(array, esquerda, direita):
    pivo = array[direita]
    i = esquerda - 1

    for j in range(esquerda, direita):
        if array[j] <= pivo:
            i += 1
            array[j], array[i] = array[i], array[j]

    array[i + 1], array[direita] = array[direita], array[i + 1]
    return i + 1

array = [55, 44, 22 ,11, 66, 33]
#array = [77 ,55 ,33 ,99]
quickSort(array, 0, len(array) - 1)
print("Resultado final:", array)

#as saidas foram essas:
# quicksort(array, 1, 6)
# quicksort(array, 1, 2)
# quicksort(array, 1, 0)
# quicksort(array, 2, 2)
# quicksort(array, 4, 6)
# quicksort(array, 4, 4)
# quicksort(array, 6, 6)