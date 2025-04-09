#Questão 1.– Escreva uma função que verifique se um vetor v[0..n-1] está em ordem crescente. (Este
#exercício põe em prática a estratégia de escrever os testes antes de inventar algoritmos para o problema.)
def verificacaoCrescente(array):
    trava = False
    n= len(array)
    primeira = array[0]
    for i in range(n-1):
        if primeira > array[i]:
            print(array)
            print("DESORDENADO")
            trava = True
            break
        primeira = array[i]
    if trava == False:
        print(array)
        print("ORDENADO")
    
        

array = [1,2,3,4,5,6,7]
verificacaoCrescente(array)


#Questão 2.– Escreva uma função que receba um inteiro x e um vetor v[0..n-1] de inteiros em ordem
#crescente e insira x no vetor de modo a manter a ordem crescente.

def inserirXCrescente(x,array):
    n = len(array)
    array.append(n-1)
    for i in range(n):
        if(array[i]>x):
            pos = i
            valor=array[i]
            array[i] = x
            i+=1
            j=i
            #array[j]=valor
            while i+1<n:
                array[j]=array[i]
                j+=1
                i+=1
            array[pos+1] = valor
            break
    print(array)


x = 3
array = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
inserirXCrescente(x,array)

