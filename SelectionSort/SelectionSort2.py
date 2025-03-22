def selectionSort2(array):
    n = len(array)
    for i in range(n):
        posicaoMenor = i
        menorValor = array[i]
        for j in range(i,n):
            if(menorValor > array[j]):
                menorValor = array[j]
                posicaoMenor = j
        array[i],array[posicaoMenor] = array[posicaoMenor], array[i]


numeros = [6,2,4,8,5,9,1]
selectionSort2(numeros)