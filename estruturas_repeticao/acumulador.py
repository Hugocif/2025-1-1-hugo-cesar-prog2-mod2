QUANTIDADE_DE_REPETICOES_DO_LACO = 3
controleDoLaco = 1
soma = 0

while controleDoLaco <= QUANTIDADE_DE_REPETICOES_DO_LACO:
    numeroInteiro = input("Digite um numero inteiro: ")
    print("O valor digitado foi: ", numeroInteiro)
     
    soma = soma + int(numeroInteiro)
    
    #Atualiza o controle do laco p/ que exista um ponto de parada e 
    #o número de repetições seja controlado.
    controleDoLaco = controleDoLaco + 1
    #comtroleDoLaco+= 1 

print("A soma dos números digitados foi: ", soma)