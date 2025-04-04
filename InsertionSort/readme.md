
# 📌 Estrutura de Dados II - Insertion Sort

## 📌 **Pablo Vinicius Lima Souza**


---

## 🚀 Insertion Sort Padrão

![Insertion Sort Padrão](![image](https://github.com/user-attachments/assets/d9c6d105-10c4-408b-a66b-66c9e1ee0d3a)

---

## ⚡ Insertion Sort Otimizado

![Insertion Sort Otimizado](![image](https://github.com/user-attachments/assets/a08e78e5-143d-4b24-af6e-0a576151227d)

---

## ⏳ Análise de Tempo de Execução

### 📊 Insertion Sort Padrão
Exemplo 1:

![Exemplo 1](![image](https://github.com/user-attachments/assets/20ed9f52-2df8-43ab-9820-efdd26d65124)

Exemplo 2:

![Exemplo 2](![image](https://github.com/user-attachments/assets/db999ee0-38e8-4007-ae41-bba9da017bc9)
)

Exemplo 3:

![Exemplo 3](![image](https://github.com/user-attachments/assets/63dd40fb-99ca-4cf4-9c87-7adbbb4c1c1c)


---

### ⚡ Insertion Sort Otimizado
Exemplo 1:

![Exemplo 1](https://github.com/user-attachments/assets/71f40721-3b5a-4f4f-8963-27e61f679b92)

Exemplo 2:

![Exemplo 2](https://github.com/user-attachments/assets/277543cf-23ac-4ad1-b4fb-e2e9c97aab63)

Exemplo 3:

![Exemplo 3](https://github.com/user-attachments/assets/cc26f231-1460-427d-9c02-1eaee53b4fac)


---

## 📊 Resultado Comparativo

| Exemplo | Insertion Sort Padrão | Insertion Sort Otimizado |
|---------|--------------------|----------------------|
| 1º      | 0.001424s          | 0.001549s           |
| 2º      | 0.002590s          | 0.002484s           |
| 3º      | 0.004692s          | 0.001994s           |

---

## 📌 Análise

O **Insertion Sort Otimizado** melhora o desempenho ao incluir uma variável (`veri`) para detectar se houve trocas. Se nenhuma troca ocorrer, o loop externo é encerrado antecipadamente. Isso o torna mais eficiente quando:

✔️ O array está parcialmente ordenado.
✔️ O array se ordena rapidamente nas primeiras iterações.

🔸 **Overhead da verificação extra:** A instrução `if veri == False: break` adiciona um pequeno custo extra a cada iteração.
🔸 **Casos onde a otimização não faz diferença:** Se o array for totalmente aleatório e precisar de todas as iterações, a otimização pode não trazer vantagem e até aumentar o tempo.

Isso explica por que no 1º exemplo o Bubble Sort Otimizado foi ligeiramente mais lento.

---

📌 **Conclusão:** Em cenários específicos, a versão otimizada pode ser significativamente mais rápida, mas em casos de alta desordem, seu impacto pode ser mínimo ou até negativo.

