def insertionSort1(array):
    n = len(array)

    for i in range(1, n):
        chave = array[i]
        j = i - 1

        # Move os elementos maiores que a chave apenas uma vez
        while j >= 0 and array[j] > chave:
            j -= 1

        # Usa slicing para reduzir movimentações
        array[j + 2:i + 1] = array[j + 1:i]
        array[j + 1] = chave

    print("Ordenados", array)

num = [3, 14, 8, 2, 16, 4, 28, 50, 33]
print("Desordenados", num)
insertionSort1(num)
