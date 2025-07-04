def merge_sort(array):
    if len(array)<= 1:
        return array

    meio = len(array)//2
    metade_esquerda = array[:meio]
    metade_direita = array[meio:]

    ordenaEsquerda = merge_sort(metade_esquerda)
    ordenaDireita = merge_sort(metade_direita)
    return merge(ordenaEsquerda, ordenaDireita)

def merge(esquerda, direita):
    i=0
    j=0
    c=[]

    while(i < len(esquerda) and j < len(direita)):
        if(esquerda[i] < direita[j]):
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


array = [1,8,6,4,2,22,36,74,65,42,63,95,86,7,41,122,321,547,11,23,45,68,17,19,12,87]
ord = merge_sort(array)
print(ord)