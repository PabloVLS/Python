def merge_sort_iterativo(array):
    n = len(array)
    tamanho_bloco = 1  
    resultado = array[:]  

    while tamanho_bloco < n:
        i = 0
        while i < n:
            esquerda = resultado[i : i + tamanho_bloco]
            direita = resultado[i + tamanho_bloco : i + 2 * tamanho_bloco]
            resultado[i : i + 2 * tamanho_bloco] = merge(esquerda, direita)
            i += 2 * tamanho_bloco
        tamanho_bloco *= 2

    return resultado

def merge(esquerda, direita):
    i = 0
    j = 0
    resultado = []

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1


    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado



array = [10, 3, 5, 7, 2, 9, 1, 6]
ordenado = merge_sort_iterativo(array)
print("Lista ordenada:", ordenado)
