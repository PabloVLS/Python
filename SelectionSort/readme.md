# Comparação entre Selection Sort Padrão e Otimizado

# Pablo Vinicius Lima Souza

## Introdução
Este repositório contém duas implementações do algoritmo de ordenação **Selection Sort**: uma versão padrão e uma versão otimizada. O objetivo é demonstrar as diferenças entre as abordagens e as melhorias aplicadas.

## Algoritmo Selection Sort Padrão
A implementação **selectionSort2** segue a lógica clássica do Selection Sort:
- Percorre o array buscando o menor elemento a partir da posição atual.
- Realiza a troca do menor elemento encontrado com a posição inicial do ciclo.
- Esse processo se repete até o array estar completamente ordenado.

### Código:
```python
def selectionSort2(array):
    n = len(array)
    for i in range(n):
        posicaoMenor = i
        menorValor = array[i]
        for j in range(i, n):
            if menorValor > array[j]:
                menorValor = array[j]
                posicaoMenor = j
        array[i], array[posicaoMenor] = array[posicaoMenor], array[i]

    print("Ordenação:", array)

numeros = [6,2,4,8,5,9,1]
selectionSort2(numeros)
```

## Algoritmo Selection Sort Otimizado
A implementação **SelectionSortOtimizado** aplica algumas melhorias:
- **Evita trocas desnecessárias**: só troca os elementos se for realmente necessário.
- **Reduz a complexidade do loop interno**: começa a busca sempre na posição `i+1`.
- **Evita a atribuição desnecessária de valores** ao invés de armazenar o menor número, apenas guarda o índice dele.

### Código:
```python
def SelectionSortOtimizado(array):
    n = len(array)
    for i in range(n-1):
        menorPos = i
        for j in range(i+1, n):
            if array[j] < array[menorPos]:
                menorPos = j
        if menorPos != i:
            array[i], array[menorPos] = array[menorPos], array[i]
    
    print("Ordenados:", array)

numeros = [6,2,4,8,5,9,1]
SelectionSortOtimizado(numeros)
```

## Diferenças entre as versões
| Aspecto | Selection Sort Padrão | Selection Sort Otimizado |
|---------|-----------------------|---------------------------|
| 🚀 Trocas desnecessárias | Sim | Não |
| 🔄 Eficiência no loop | Menor | Maior (começa em `i+1`) |
| 📜 Melhor legibilidade | Pior | Melhor |
| ⚡ Performance | Igual na média | Ligeiramente melhor |



