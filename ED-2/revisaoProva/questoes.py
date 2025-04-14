#Questão 1.– Escreva uma função que verifique se um vetor v[0..n-1] está em ordem crescente. (Este
#exercício põe em prática a estratégia de escrever os testes antes de inventar algoritmos para o problema.)
def verificacaoCrescente(array):
    trava = False
    n= len(array)
    primeira = array[0]
    for i in range(n-1):
        if primeira > array[i]:
            print("DESORDENADO",array)
            trava = True
            break
        primeira = array[i]
    if trava == False:
        print("ORDENADO",array)
    
        

array = [1,2,3,4,5,6,7]
verificacaoCrescente(array)


#Questão 2.– Escreva uma função que receba um inteiro x e um vetor v[0..n-1] de inteiros em ordem
#crescente e insira x no vetor de modo a manter a ordem crescente.

def inserirXCrescente(x, array):
    n = len(array)
    array.append(0)#adicionou mais 1 posição no final do vetor
    i=n-1

    while(i>=0 and array[i]>x):#ai vai de tras pra frente 
        array[i+1] = array[i]  #vai colocando as posições maiores pro final do vetor
        i-=1

    array[i+1] = x#coloca o valor na posição que parou
    print("Insertion Sort Incrementando X",array)
x = 3
array = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
inserirXCrescente(x, array)


#Questão 3.– Escreva uma versão recursiva do algoritmo de ordenação por inserção.

#def insertionSort(array):
#   n = len(array)

#    for i in range(n):
#        chave = array[i]
#        j = i-1
#        while(j>=0 and chave<array[j]): 
#            array[j+1] = array[j]
#            j-=1
#        array[j+1] = chave
#       print("Insertion Sort :",array)

def insertionSortRecursivo(array , n=None):
    if(n is None):
        n = len(array)
    
    if(n <=1):
        return
    
    insertionSortRecursivo(array, n-1)

    chave = array[n-1]
    j=n-2

    while(j>=0 and array[j]> chave):
        array[j+1] = array[j]
        j-=1
    array[j+1] = chave



array = [8,4,16,20,11,16,2,24,13]
insertionSortRecursivo(array)
print("Insertion Sort Recursivo:",array)




def selectionSortRecursivo(array, comeco=0):
    n = len(array)

    if comeco >= n-1:
        return
    
    minimoValor = comeco
    for i in range(comeco+1,n):
        if(array[i]<array[minimoValor]):
            minimoValor = i

    array[comeco],array[minimoValor] = array[minimoValor],array[comeco]

    selectionSortRecursivo(array, comeco + 1)


array = [8,4,16,20,11,16,2,24,13]
selectionSortRecursivo(array)
print("Selection Sort Recursivo:",array)



#Questão 5.– Escreva uma função que permute os elementos de um vetor inteiro v[0..n-1] de modo que
#eles fiquem em ordem decrescente. Inspire-se no algoritmo Selectionsort.

def SelectionSortDecrescente(array):
    n = len(array)

    for i in range(n):
        maiorValor = array[i]
        maiorPosicao = i
        for j in range(n - 1, i, -1):
            if(array[j]>maiorValor):
                maiorValor = array[j]
                maiorPosicao = j
        array[i],array[maiorPosicao]=array[maiorPosicao],array[i]

            

array = [8,4,16,20,11,16,2,24,13]
SelectionSortDecrescente(array)
print("Selection Sort Decrescente:",array)


#Questão 6.– Invente um algoritmo de ordenação que seja mais rápido que o de inserção e o de seleção.
#Explique como consegue.
def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def AlgSuperior(array):
    meio = len(array) // 2
    parte1 = array[:meio]
    parte2 = array[meio:]

    parte1Ordenada = bubbleSort(parte1)
    parte2Ordenada = bubbleSort(parte2)

    resultado = []
    i = j = 0

    while i < len(parte1Ordenada) and j < len(parte2Ordenada):
        if parte1Ordenada[i] < parte2Ordenada[j]:
            resultado.append(parte1Ordenada[i])
            i += 1
        else:
            resultado.append(parte2Ordenada[j])
            j += 1

    while i < len(parte1Ordenada):
        resultado.append(parte1Ordenada[i])
        i += 1

    while j < len(parte2Ordenada):
        resultado.append(parte2Ordenada[j])
        j += 1

    print("Algoritmo Superior:",resultado)

array = [
    8, 4, 16, 20, 11, 16, 2, 24, 13, 7, 33, 12, 6, 22, 18, 15, 3, 9, 25, 17,
    31, 19, 27, 14, 5, 21, 28, 10, 1, 23, 29, 26, 30, 34, 35, 36, 40, 32, 38, 37,
    39, 42, 44, 43, 41, 45, 46, 48, 50, 47, 49, 51, 52, 54, 53, 55, 56, 58, 57, 59,
    60, 61, 63, 62, 65, 64, 66, 67, 69, 68, 70, 71, 73, 72, 74, 75, 77, 76, 78, 79,
    80, 81, 83, 82, 84, 85, 87, 86, 88, 89, 91, 90, 92, 93, 95, 94, 96, 97, 99, 98
]

AlgSuperior(array)
