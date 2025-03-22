def SelectionSortOtimizado(array):
    n = len(array)

    for i in range(n-1):
        menorNumero = array[i]
        menorPos = i
        for j in range(i+1,n):
            if menorNumero > array[j]:
                menorPos = j
        if menorPos !=i:
            array[i], array[menorPos] = array[menorPos], array[i]

    print("Ordenados:",array)


numeros = [6,2,4,8,5,9,1]
SelectionSortOtimizado(numeros)