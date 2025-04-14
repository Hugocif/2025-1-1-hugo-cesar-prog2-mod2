#Exercicio 1
for itemdalista in "Instituto Federal De Santa Catarina":
 print(itemdalista)

mensagemASerExibidaNaHorizontal = ''

#Exercício 2
for numerosPares in range(0, 21, 2):
 print (f"Os números pares de 0 a 20 são: ", numerosPares)

#Exercício 3
numeroquevaitertabuada= int(input("Digite um número para calcular a tabuada: "))

for itemdalista in range(1, 11):
 print(f"{itemdalista} X {numeroquevaitertabuada} = {itemdalista * numeroquevaitertabuada}")

#Exercício 4
valortempo1 = 0
import time

for valortempo1 in range(0,20):
 valortempo1 += 1
print(f"Contagem : ", valortempo1)
#1 - O valor -1, no SEGUNDO parâmetro é o stop (opcional), ou seja, indica até onde a sequência deve ser gerada. Nesse caso específic, até o ZERO, por isso foi passado o valor -1;
#2 - O valor -1, no TERCEIRO parâmetro é o step (opcional), ou seja, é o incremento dos valores da sequência que nesse casose dará de 1 em 1, o fato do valor ser negativo indica, nesse caso, que a sequêncai será gerada em ordem decrescente : 20, 19, 18, 17..


#Exercício 5
for impares in range(0,101,2):
 print(f"Os números ímpares são : ", impares)

# Exercicio 6
numerouser = int(input("Digite um número : "))

for i in range(2, numerouser):
 if numerouser % i == 0 :
  print("O número é primo.")
else:
 
 print("O número não é primo.")