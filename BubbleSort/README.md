# 📌 Estrutura de Dados II - Bubble Sort

## 📌 **Pablo Vinicius Lima Souza**


---

## 🚀 Bubble Sort Padrão

![Bubble Sort Padrão](https://github.com/user-attachments/assets/d484be9e-03ad-4215-a3cf-e771617d11c2)

---

## ⚡ Bubble Sort Otimizado

![Bubble Sort Otimizado](https://github.com/user-attachments/assets/ec5f244c-d43d-4068-9186-72b67bf14cca)

---

## ⏳ Análise de Tempo de Execução

### 📊 Bubble Sort Padrão
Exemplo 1:

![Exemplo 1](https://github.com/user-attachments/assets/2cd0642f-91b0-4b6e-a09f-b7d2b7becc29)

Exemplo 2:

![Exemplo 2](https://github.com/user-attachments/assets/b6eb728a-8656-40f9-8032-36847c476111)

Exemplo 3:

![Exemplo 3](https://github.com/user-attachments/assets/40aceccf-905f-41f2-b123-ac34bc526105)

---

### ⚡ Bubble Sort Otimizado
Exemplo 1:

![Exemplo 1](https://github.com/user-attachments/assets/71f40721-3b5a-4f4f-8963-27e61f679b92)

Exemplo 2:

![Exemplo 2](https://github.com/user-attachments/assets/277543cf-23ac-4ad1-b4fb-e2e9c97aab63)

Exemplo 3:

![Exemplo 3](https://github.com/user-attachments/assets/cc26f231-1460-427d-9c02-1eaee53b4fac)


---

## 📊 Resultado Comparativo

| Exemplo | Bubble Sort Padrão | Bubble Sort Otimizado |
|---------|--------------------|----------------------|
| 1º      | 0.001424s          | 0.001549s           |
| 2º      | 0.002590s          | 0.002484s           |
| 3º      | 0.004692s          | 0.001994s           |

---

## 📌 Análise

O **Bubble Sort Otimizado** melhora o desempenho ao incluir uma variável (`veri`) para detectar se houve trocas. Se nenhuma troca ocorrer, o loop externo é encerrado antecipadamente. Isso o torna mais eficiente quando:

✔️ O array está parcialmente ordenado.
✔️ O array se ordena rapidamente nas primeiras iterações.

🔸 **Overhead da verificação extra:** A instrução `if veri == False: break` adiciona um pequeno custo extra a cada iteração.
🔸 **Casos onde a otimização não faz diferença:** Se o array for totalmente aleatório e precisar de todas as iterações, a otimização pode não trazer vantagem e até aumentar o tempo.

Isso explica por que no 1º exemplo o Bubble Sort Otimizado foi ligeiramente mais lento.

---

📌 **Conclusão:** Em cenários específicos, a versão otimizada pode ser significativamente mais rápida, mas em casos de alta desordem, seu impacto pode ser mínimo ou até negativo.

