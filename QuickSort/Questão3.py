def qsrt ( array , left , right ) :
    j = partition ( array , left , right )
    if ( left < j - 1) :
        qsrt ( array , left , j - 1)
    if ( j + 1 < right ) :
        qsrt ( array , j + 1 , right )
    return array

def partition(array, esquerda , direita):
    pivo = array[direita]
    i = esquerda - 1

    for j in range(esquerda , direita):
        if(array[j] <= pivo):
            i+=1
            array[i], array[j] = array[j] , array[i]

    array[i+1], array[direita] = array[direita], array[i+1]
    return i+1



array = [5,8,9,21,14,12,3,6,65,114,10,2,13]
ord = qsrt(array , 0, len(array)-1)
print(ord)

# um dos erros que podem dar e se não for declarado 0 e len(array)-1 antes de entra no quickSort vai dar erro
# de resto esta funcionando normalmente