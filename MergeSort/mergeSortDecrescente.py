def merge_sort(array):
    if len(array)<= 1:
        return array

    meio = len(array) // 2
    metade_esquerda = array[:meio]
    metade_direita = array[meio:]

    ord_esquerda = merge_sort(metade_esquerda)
    ord_direita = merge_sort(metade_direita)

    return merge(ord_esquerda, ord_direita)

def merge(ord_esquerda, ord_direita):
    i=0
    j=0
    c=[]

    while(i < len(ord_esquerda) and j < len(ord_direita)):
        if(ord_esquerda[i] > ord_direita[j]):
            c.append(ord_esquerda[i])
            i+=1
        else:
            c.append(ord_direita[j])
            j+=1

    while(i < len(ord_esquerda)):
        c.append(ord_esquerda[i])
        i+=1

    while(j < len(ord_direita)):
        c.append(ord_direita[j])
        j+=1

    return c



array = [32,45,74,12,41,23,21,56,87,96,23,45,13]
dec = merge_sort(array)
print(dec)