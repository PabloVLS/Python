# Questão 2.– Utilize a versão iterativa do Quick Sort e compare-a com a versão recursiva. Faça testes
# com vetores de tamanhos variados, meça o tempo de execução de ambas as versões e apresente os
# resultados em uma tabela. Em seguida, discuta as vantagens e desvantagens observadas entre as duas
# abordagens.
import time
import random

def quickSortIterativo(array):
    pilha = []

    pilha.append((0, len(array)-1))

    while(pilha):

        esquerda, direita = pilha.pop()
        pivo = partition(array , direita , esquerda)
        
        if pivo -1 > esquerda:
            pilha.append((esquerda, pivo-1))
        if pivo +1 < direita:
            pilha.append((pivo + 1, direita))

    return array

def partition(array, direita, esquerda):
    pivo = array[direita]
    i = esquerda -1

    for j in range(esquerda, direita):
        if(array[j] <= pivo):
            i+=1
            array[i], array[j] = array[j], array[i]

    array[i +1], array[direita] = array[direita], array[i+1]
    return i+1

array =[random.randint(1, 100000000) for _ in range(100000000)]
start_time = time.time()

ord = quickSortIterativo(array)

end_time = time.time()
# execution_time = end_time - start_time
print("Quick Iterativo = ",ord)
print(F"Tempo de execução ITERATIVO = {end_time - start_time}")


def quickSort(array, esquerda=0, direita= None ):
    if(direita is None):
        direita = len(array)-1
    if esquerda < direita:
        pivo = partition(array,esquerda,direita)
        quickSort(array , esquerda, pivo-1)
        quickSort(array, pivo+1, direita)
        return array

def partition(array, esquerda, direita):
    pivo = array[direita]
    i = esquerda - 1

    for j in range(esquerda, direita):
        if(array[j] <= pivo):
            i+=1
            array[i], array[j] = array[j], array[i]

    array[i+1] , array[direita] = array[direita] , array[i+1]
    return i+1


array =[random.randint(1, 100000000) for _ in range(100000000)]
start_time = time.time()

ord = quickSort(array)

end_time = time.time()
# execution_time = end_time - start_time
print("Quick Recursivo = ",ord)
print(F"Tempo de execução RECURSIVO = {end_time - start_time}")


# O TEMPO DE EXECUÇÃO DO ITERATIVO FOI MELHOR EM ALGUNS CASOS - COM 1000 NUMEROS ALEATORIOS O ITERATIVO FEZ 0.01670694351196289
# JA O TEMPO DO RECURSIVO FOI DE : 0.023319721221923828

# O TEMPO DE EXECUÇÃO DO ITERATIVO FOI MELHOR EM ALGUNS CASOS - COM 1000000 NUMEROS ALEATORIOS O ITERATIVO FEZ 3.2011992931365967
# JA O TEMPO DO RECURSIVO FOI DE : 3.406301736831665