# 📌 Estrutura de Dados II - Insertion Sort

## 📌 **Pablo Vinicius Lima Souza**

---

## 🚀 Insertion Sort Padrão

![Insertion Sort Padrão](https://github.com/user-attachments/assets/d9c6d105-10c4-408b-a66b-66c9e1ee0d3a)

---

## ⚡ Insertion Sort Otimizado

![Insertion Sort Otimizado](https://github.com/user-attachments/assets/a08e78e5-143d-4b24-af6e-0a576151227d)

---

## ⏳ Análise de Tempo de Execução

### 📊 Insertion Sort Padrão  
**Exemplo 1:**  
![Exemplo 1](https://github.com/user-attachments/assets/20ed9f52-2df8-43ab-9820-efdd26d65124)

**Exemplo 2:**  
![Exemplo 2](https://github.com/user-attachments/assets/db999ee0-38e8-4007-ae41-bba9da017bc9)

**Exemplo 3:**  
![Exemplo 3](https://github.com/user-attachments/assets/63dd40fb-99ca-4cf4-9c87-7adbbb4c1c1c)

---

### ⚡ Insertion Sort Otimizado  
**Exemplo 1:**  
![Exemplo 1](https://github.com/user-attachments/assets/aa09c223-2234-41a8-8fc1-e750c33e28d7)

**Exemplo 2:**  
![Exemplo 2](https://github.com/user-attachments/assets/33550af3-0cf0-402e-9f01-ff793a35042a)

**Exemplo 3:**  
![Exemplo 3](https://github.com/user-attachments/assets/a8907456-b594-4b38-b975-e6349be4e78b)

---

## 📊 Resultado Comparativo

| Exemplo | Insertion Sort Padrão | Insertion Sort Otimizado |
|---------|------------------------|----------------------------|
| 1º      | 0.000088s              | 0.000104s                  |
| 2º      | 0.000088s              | 0.000093s                  |
| 3º      | 0.000111s              | 0.003437s                  |

---

## 📌 Análise

O **Insertion Sort Otimizado** melhora o desempenho ao utilizar **busca binária** para encontrar a posição correta de inserção, reduzindo o número de comparações.  
Além disso, o uso de **fatiamento eficiente** evita movimentações desnecessárias, tornando-o mais rápido em listas grandes ou parcialmente ordenadas.

Esse algoritmo é mais eficiente quando:

- A lista está quase ordenada.
- O número de elementos é alto.
- Busca-se reduzir tempo de comparação e movimentação.
