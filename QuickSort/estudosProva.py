def quickSort(array, esquerda, direita):
    if esquerda < direita:
        pivo = partitionH(array, esquerda, direita)
        quickSort(array, esquerda, pivo)
        quickSort(array, pivo + 1, direita)

def partitionH(array, esquerda, direita):
    pivo = array[esquerda]  
    i = esquerda - 1
    j = direita + 1

    while True:
        i += 1
        while array[i] < pivo:
            i += 1

        j -= 1
        while array[j] > pivo:
            j -= 1

        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]

array = [38, 27, 43, 3, 9, 82, 10, 44]
quickSort(array, 0, len(array) - 1)
print("Quick Sort (Hoare):", array)



def quickSort(array, esquerda, direita):
    if(esquerda < direita):
        pivo = partition(array, esquerda, direita)
        quickSort(array, esquerda, pivo-1)
        quickSort(array, pivo+1, direita)
        return array
    
def partition(array, esquerda, direita):
    pivo = array[direita]
    i = esquerda - 1

    for j in range(esquerda, direita):
        if(array[j] < pivo):
            i+=1
            array[i], array[j]= array[j], array[i]
    
    array[i+1], array[direita] = array[direita] , array[i+1]
    return i+1



array = [38, 27, 43, 3, 9, 82, 10, 44,12]
ord = quickSort(array, 0, len(array)-1)
print("Quick Sort :", array)


def mergeSort(array):
    if(len(array)<=1):
        return array
    
    meio = len(array) // 2
    metadeEsquerda = array[:meio]
    metadeDireita = array[meio:]

    esquerda = mergeSort(metadeEsquerda)
    direita = mergeSort(metadeDireita)
    return merge(esquerda, direita)

def merge(esquerda, direita):
    i=0
    j=0
    c=[]

    while(i<len(esquerda) and  j < len(direita)):
        if( esquerda[i] < direita[j]):
            c.append(esquerda[i])
            i+=1
        else:
            c.append(direita[j])
            j+=1

    while(i < len(esquerda)):
        c.append(esquerda[i])
        i+=1

    while(j < len(direita)):
        c.append(direita[j])
        j+=1

    return c

array = [38, 27, 43, 3, 9, 82, 10, 44]
ord = mergeSort(array)
print("Merge Sort :", ord)