#Questão 1
#A logica está correta porem , nao precisa fazer tantas verificações se True e False , apenas se for False, 
#assim será mais otimizado.
def verifica(lista):
    n= len(lista)
    sim = True
    for i in range(1, n):
        if lista[i-1] > lista[i]:
            sim = False
            break

    return sim

##################################################################################################
#Questão 2
#Bubble Sort normal
def bubble_sort(array):
    tamanho = len(array)
    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            if array[j] > array[j+1]:
                aux = array[j]
                array[j] = array[j + 1] 
                array[j+1]= aux
    return array
# Bublle Sort otimizado com a logica de interromper a execução se ja estiver ordenada.
def bubble_sort(array):
    tamanho = len(array)
    for i in range(tamanho):
        trocou = False  # flag de verificação
        for j in range(0, tamanho - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                trocou = True  # houve troca
        if not trocou:
            break  # lista já está ordenada
    return array


array = [5,1,23,47,6,98,55]
bubble_sort(array)
#print(array)
####################################################################################################

#Questão 3

#[77, 51, 11, 37, 29, 13, 21]


#77 > 51 troca [51, 77, 11, 37, 29, 13, 21] 
#77 > 11 troca [51, 11, 77, 37, 29, 13, 21]  
#77 > 37 troca [51, 11, 37, 77, 29, 13, 21]   
#77 > 29 troca [51, 11, 37, 29, 77, 13, 21]  
#77 > 13 troca [51, 11, 37, 29, 13, 77, 21]   
#77 > 21 troca [51, 11, 37, 29, 13, 21, 77]   
#Trocas nesta passada: 6


#51 > 11 troca [11, 51, 37, 29, 13, 21, 77]   
#51 > 37 troca [11, 37, 51, 29, 13, 21, 77]   
#51 > 29 troca [11, 37, 29, 51, 13, 21, 77]   
#51 > 13 troca [11, 37, 29, 13, 51, 21, 77]   
#51 > 21 troca [11, 37, 29, 13, 21, 51, 77]  
#Trocas nesta passada: 5

#37 > 29 troca [11, 29, 37, 13, 21, 51, 77]   
#37 > 13 troca [11, 29, 13, 37, 21, 51, 77]   
#37 > 21 troca [11, 29, 13, 21, 37, 51, 77]  
#Trocas nesta passada: 3


#29 > 13 troca [11, 13, 29, 21, 37, 51, 77]  
#29 > 21 troca [11, 13, 21, 29, 37, 51, 77]   
#Trocas nesta passada: 2

#################################################################################################

#Questão 4
#4 a) A alternativa A não vai ordenar o primeiro valor do vetor.

#4 b) Se você fizer essa mudança você terá problemas com o tamanho da lista, pois faz a comparação do
#número atual do index i com os próximos, além de ser completamente desnecessário, pois se o último
#número já é maior que o penúltimo, não há a necessidade de nenhuma troca.

#4 c)Nesse caso você não teria uma alteração a lógica, mas cria uma situação desnecessária pois não é
#preciso trocar um número por ele mesmo, mesmo que nesse caso v[min-index] fosse o menor número, um
#número igual a ele estaria logo após ele na lista


#################################################################################################
#Questão 5
#A) Pior Caso [5,4,3,2,1] = Foram 10 comparações , 7 Trocas.
#B)Melhor Caso [1,2,3,4,5]= Foram 10 comparações , 0 Trocas.

#################################################################################################
#Questão 6
#O v[i] = x, é totalmente desnecessário , pois ocupa mais espaço de memória, 
# já que se colocar depois de finazliar o while como v[i+1]=aux já
# garante a posição correta. Outro problema é o primeiro "for" começar
#  com (1,n), ou seja, ignorando a primeira posição que seria o (0,n)

##################################################################################################
#Questão 7

def insertion_sort_recursivo(array, n=None):
    if n is None:
        n = len(array)
    if n <= 1:
        return
    insertion_sort_recursivo(array, n - 1)
    numero = array[n - 1]
    j = n - 2
    while j >= 0 and array[j] > numero:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = numero

array = [5,1,23,47,6,98,55]
insertion_sort_recursivo(array)
print(array)