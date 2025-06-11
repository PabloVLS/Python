class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def imprimir_lista(cabeca):
    atual = cabeca
    while atual:
        print(atual.valor, end=" -> ")
        atual = atual.proximo
    print("None")

def merge_sort(cabeca):
    # Caso base: lista vazia ou com um nó só
    if cabeca is None or cabeca.proximo is None:
        return cabeca

    # Encontrar o meio da lista e separar em duas metades
    meio = encontrar_meio(cabeca)
    direita = meio.proximo
    meio.proximo = None  # quebra a lista em duas partes

    # Ordenar as duas metades recursivamente
    esquerda_ordenada = merge_sort(cabeca)
    direita_ordenada = merge_sort(direita)

    # Mesclar as duas listas ordenadas e retornar a cabeça da lista resultante
    return mesclar_listas(esquerda_ordenada, direita_ordenada)

def encontrar_meio(cabeca):
    # Usa dois ponteiros: lento e rápido para achar o meio da lista
    lento = cabeca
    rapido = cabeca.proximo

    while rapido and rapido.proximo:
        lento = lento.proximo
        rapido = rapido.proximo.proximo

    return lento

def mesclar_listas(l1, l2):
    no_falso = No(0)  # nó auxiliar para facilitar a mesclagem
    cauda = no_falso

    while l1 and l2:
        if l1.valor < l2.valor:
            cauda.proximo = l1
            l1 = l1.proximo
        else:
            cauda.proximo = l2
            l2 = l2.proximo
        cauda = cauda.proximo

    # Anexa o que sobrou de l1 ou l2
    cauda.proximo = l1 if l1 else l2

    return no_falso.proximo

# --- Exemplo de uso ---

# Criar uma lista: 4 -> 2 -> 1 -> 3 -> None
cabeca = No(4)
cabeca.proximo = No(2)
cabeca.proximo.proximo = No(1)
cabeca.proximo.proximo.proximo = No(3)

print("Antes da ordenação:")
imprimir_lista(cabeca)

cabeca = merge_sort(cabeca)

print("Depois da ordenação:")
imprimir_lista(cabeca)
