def selectionSort(array):
    n= len(array)
    aux = 0

    for i in range(n):
        menor = array[i]
        posMenor = i
        for j in range(i,n):
            if(array[j] < menor):
                menor = array[j]
                posMenor = j

        array[i] , array[posMenor] = array[posMenor] , array[i]
        #menor = j

    print("Ordenados: ",array)

num = [11, 4, 30, 22, 7, 26]
selectionSort(num)


# 11 04 30 22 07 26