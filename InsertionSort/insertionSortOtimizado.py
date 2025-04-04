from bisect import bisect_left
import time
def insertion_sort_otimizado(arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        pos = bisect_left(arr, val, 0, i)  # Busca binária para a posição correta
        arr[pos+1:i+1] = arr[pos:i]  #Faz a troca de forma eficiente
        arr[pos] = val  # Coloca o numero na posição correta
    print("Ordenados: ",arr)

    end = time.time()
    print(f"Tempo de execução: {end - start:.6f} segundos")

start = time.time()
teste = [5,2,9,1,5,6]
insertion_sort_otimizado(teste)

