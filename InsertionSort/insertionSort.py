def insertionSort(array):
    n= len(array)

    for i in range(1,n):
        chave = array[i]
        j=i-1;
        while j>=0 and array[j]>chave:
            array[j+1] = array[j]
            j=j-1
        array[j+1] = chave


    print("Ordenados: ",array)

num = [11, 4, 30, 22, 7, 26, 4]
insertionSort(num)


