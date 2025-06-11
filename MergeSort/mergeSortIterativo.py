def mergeSort(array):
    if(len(array)<=1):
        return array

    meio = len(array)//2
    metadeEsquerda = array[:meio]
    metadeDireita = array[meio:]

    esquerda = mergeSort(metadeEsquerda)
    direita = mergeSort(metadeDireita)

    return merge(esquerda, direita)

def merge(esquerda ,direita):
    i=0
    j=0
    c=[]

    while(i < len(esquerda) and j< len(direita)):
        if(esquerda[i]< direita[j]):
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

array = [5,7,4,12,36,5,8,24,56,20,51]
ord = mergeSort(array)
print(ord)