Estrutura de Dados II
Bubble Sort

Pablo Vinicius Lima Souza	
Buble Sort Padrão
![image](https://github.com/user-attachments/assets/d484be9e-03ad-4215-a3cf-e771617d11c2)

 
Bubble Sort Otimizado
![image](https://github.com/user-attachments/assets/e5571b87-263e-4587-ae00-17361e6137c6)

 


Analise de Tempo de Execução

Bubble Sort Padrão
Exemplo 1:
![image](https://github.com/user-attachments/assets/2cd0642f-91b0-4b6e-a09f-b7d2b7becc29)

 	






Exemplo 2:
![image](https://github.com/user-attachments/assets/b6eb728a-8656-40f9-8032-36847c476111)







Exemplo 3: 
![image](https://github.com/user-attachments/assets/40aceccf-905f-41f2-b123-ac34bc526105)





Bubble Sort Otimizado
Exemplo 1:
![image](https://github.com/user-attachments/assets/71f40721-3b5a-4f4f-8963-27e61f679b92)









Exemplo 2:
![image](https://github.com/user-attachments/assets/277543cf-23ac-4ad1-b4fb-e2e9c97aab63)








Exemplo 3:
![image](https://github.com/user-attachments/assets/cd52eddd-fa1e-4fe9-8bee-4ff95cb58953)






RESULTADO

     Bubble Sort Padrão					Bubble Sort Otimizado
1 Exemplo: 0.001424						0.001549
2 Exemplo: 0.002590						0.002484
3 Exemplo: 0.004692						0.001994

Análise
O Bubble Sort otimizado usa a variável veri para detectar se houve trocas. Se nenhuma troca for feita, o loop externo é interrompido antecipadamente. Isso faz com que ele tenha vantagem quando:
✔️ O array está parcialmente ordenado.
✔️ O array se ordena rapidamente nas primeiras iterações.
🔸 Overhead da verificação extra (if veri == False : break): Embora pequena, essa verificação adiciona um custo extra a cada iteração.
🔸 Caso em que trocas ocorrem até o final: Se o array for aleatório e precisar de todas as iterações, a otimização não faz diferença e pode até adicionar tempo extra.
Isso pode explicar o 1º exemplo, onde o otimizado foi mais lento.

