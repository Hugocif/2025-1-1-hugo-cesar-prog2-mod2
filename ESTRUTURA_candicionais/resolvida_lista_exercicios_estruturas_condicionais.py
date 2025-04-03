"""Implementação sugerida pelo professor, como exemplo."""


#EXERCÍCIO 1
primeiroValorInformadoPeloUsuario = input("Digite o primeiro número: ")
segundoValorInformadoPeloUsuario  = input("Digite o segundo número: ")

#Validação do tipo de entrada informada pelo Stdin (teclado)
if not (primeiroValorInformadoPeloUsuario.strip().isnumeric()):
    print(f"O primeiro valor informado: \"{primeiroValorInformadoPeloUsuario}\" não é um valor numérico inteiro válido. O programa foi finalizado.")
    
elif (not (segundoValorInformadoPeloUsuario.strip().isnumeric())):
    print(f"O segundo valor informado: \"{segundoValorInformadoPeloUsuario}\" não é um valor numérico  inteiro  válido.  O programa foi finalizado.")
    
else:
    if (int(primeiroValorInformadoPeloUsuario) > int(segundoValorInformadoPeloUsuario)):
        print(f"O primeiro número {primeiroValorInformadoPeloUsuario} é maior que o segundo {segundoValorInformadoPeloUsuario}.")
        
    elif (int(segundoValorInformadoPeloUsuario) > int(primeiroValorInformadoPeloUsuario)):
        print(f"o Segundo número {segundoValorInformadoPeloUsuario} é maior que o primeiro {primeiroValorInformadoPeloUsuario}.")
        
    else:
        print("Os valores informados são iguais.")


#EXERCÍCIO 2
print('''============= Clínica Médica Barsa'===================
      1 - Dr. José Matos
      2 - Dra. Fernanda Santos
      3 - Dra. Beti Silva
      ''')

opcaoInformada = input("Informe o médico(a) que deseja marcar uma consulta: ")

if opcaoInformada == '1':
    print("Sua consulta foi marcada com o Dr. José Matos.")
    
elif opcaoInformada == '2':
    print("Sua consulta foi marcada com a Dra. Fernanda Santos.")
    
elif opcaoInformada == '3':
    print("Sua consulta foi marcada com a Dra. Beti Silva.")

else:
    print(f"Opção inválida. Não existe um profissional com o código {opcaoInformada}. O programa foi finalizado.")


#EXERCÍCIO 3
fraseOculta      = "Python é uma excelente linguagem de programação!!!"
palavra_ou_frase = input("Informe uma palavra ou frase: ")

encontrouPalavraFrase = fraseOculta.find(palavra_ou_frase)

if encontrouPalavraFrase == -1:
    print(f"A palavra ou frase \"{palavra_ou_frase}\" não está presente na frase oculta.")
    
else:
    print(f"A palavra ou frase \"{palavra_ou_frase}\" está presente na frase oculta.")
    
    
#EXERCÍCIO 4
numeroDoTipoInteiro = input("Informe um valor inteiro: ")

#Validação do tipo de entrada informada pelo Stdin (teclado)
if not (numeroDoTipoInteiro.strip().isnumeric()):
    print(f"O valor informado: \"{numeroDoTipoInteiro}\" não é um valor numérico inteiro válido. O programa foi finalizado.")
   
else:
    if (int(numeroDoTipoInteiro) % 2) == 0:
        print(f"O número {numeroDoTipoInteiro} é par")
        
    else:
        print(f"O número {numeroDoTipoInteiro} é ímpar")
    
#EXERCÍCIO 5
primeiroValorInformadoPeloUsuario = input("Digite o primeiro número: ")
segundoValorInformadoPeloUsuario  = input("Digite o segundo número: ")

#Validação do tipo de entrada informada pelo Stdin (teclado)
try:
    if (int(primeiroValorInformadoPeloUsuario) > 0) and (int(segundoValorInformadoPeloUsuario) > 0):
        print(f"Os números {primeiroValorInformadoPeloUsuario} e {segundoValorInformadoPeloUsuario} são positivos.")

    elif (int(primeiroValorInformadoPeloUsuario) > 0) and (int(segundoValorInformadoPeloUsuario) < 0):
        print(f"O número {primeiroValorInformadoPeloUsuario} é positivo, já o número {segundoValorInformadoPeloUsuario} não é negativo.")

    elif (int(primeiroValorInformadoPeloUsuario) < 0) and (int(segundoValorInformadoPeloUsuario) > 0):
        print(f"O número {primeiroValorInformadoPeloUsuario} não é positivo, já o número {segundoValorInformadoPeloUsuario} é positivo.")

    elif (int(primeiroValorInformadoPeloUsuario) == 0) or (int(segundoValorInformadoPeloUsuario) == 0):
        print(f"O número ZERO é um valor neutro.")

    else:
        print(f"Os números {primeiroValorInformadoPeloUsuario} e {segundoValorInformadoPeloUsuario} são negativos.")
  
except:
  print(f"Ou \"{primeiroValorInformadoPeloUsuario}\" ou \"{segundoValorInformadoPeloUsuario}\" ou ambos não são valores numéricos válidos.")
    
#EXERCÍCIO 6
peso   = input("Informe o seu peso:   ")
altura = input("Informe a sua altura: ")

#Validação do tipo de entrada informada pelo Stdin (teclado)    
try:
    peso   = float(peso)
    altura = float(altura)
    
    #if not (peso.strip().isnumeric()):
    if type(peso) != float:
        print(f"O peso informado: \"{peso}\" não é um valor numérico válido. O programa foi finalizado.")
        
    #elif not (altura.strip().isnumeric()):
    elif type(altura) != float:
        print(f"A altura informada: \"{altura}\" não é um valor inteiro  válido.  O programa foi finalizado.")
        
    else:
        #Cálculo do IMC
        imc = float(peso) / (float(altura) * float(altura))

        if imc < 18.5:
            print(f"O seu IMC é {imc:.2f}. Você está abaixo do peso.")
            
        elif (imc >= 18.5) and (imc <= 24.9):
            print(f"O seu IMC é {imc:.2f}. Você está com o peso normal.")

        elif (imc >= 25) and (imc <= 29.9):
            print(f"O seu IMC é {imc:.2f}. Você está com o sobrepeso.")
            
        else:
            print(f"O seu IMC é {imc:.2f}. Você está com obesidade.")    
except:
    mensagemDeErro = []
    mensagemDeErro.append(f"O peso informado: {peso}"
    f" ou a altura {altura} ou ambos não são"               
    " valores válidos p/ peso e altura. O programa foi finalizado.")
    
    print(mensagemDeErro)

#EXERCÍCIO 7
numeroInformadoPeloUsuario = input("Digite um número inteiro: ")

#Validação do tipo de entrada informada pelo Stdin (teclado)
if not (numeroInformadoPeloUsuario.strip().isnumeric()):
    print(f"O número: \"{numeroInformadoPeloUsuario}\" não é um valor numérico inteiro válido. O programa foi finalizado.")
    
else:
    numeroConvertidoParaFloat = float(numeroInformadoPeloUsuario)
    print(f"O valor digitado foi {numeroConvertidoParaFloat:.2f} que é do tipo: ", type(numeroConvertidoParaFloat))
    
#EXERCÍCIO 8
primeiroValorInformadoPeloUsuario = input("Digite o primeiro número: ")
segundoValorInformadoPeloUsuario  = input("Digite o segundo número: ")

#Validação do tipo de entrada informada pelo Stdin (teclado)
if not (primeiroValorInformadoPeloUsuario.strip().isnumeric()):
    print(f"O primeiro valor informado: \"{primeiroValorInformadoPeloUsuario}\" não é um valor numérico inteiro válido. O programa foi finalizado.")
    
elif (not (segundoValorInformadoPeloUsuario.strip().isnumeric())):
    print(f"O segundo valor informado: \"{segundoValorInformadoPeloUsuario}\" não é um valor numérico  inteiro  válido.  O programa foi finalizado.")
    
else:
    if (int(primeiroValorInformadoPeloUsuario) > 150 and (int(segundoValorInformadoPeloUsuario)) > 150):
        print(f"Os números {primeiroValorInformadoPeloUsuario}, e {segundoValorInformadoPeloUsuario} são MAIORES do que 150.")
        
    elif (int(primeiroValorInformadoPeloUsuario) < 150 and (int(segundoValorInformadoPeloUsuario) < 150)):
        print(f"Os números {primeiroValorInformadoPeloUsuario}, e {segundoValorInformadoPeloUsuario} são MENORES do que 150.")

    elif (int(primeiroValorInformadoPeloUsuario) == 150 and (int(segundoValorInformadoPeloUsuario) == 150)):
        print(f"Os números {primeiroValorInformadoPeloUsuario}, e {segundoValorInformadoPeloUsuario} são IGUAIS a 150.")

    else:
        print("Vocês podem terminar essa implementação")
        
#EXERCÍCIO 9
print("Os dias da semana são:")
print("Segunda-feira", "Terça-feira", "Quarta-feira" 
, "Quinta-feira","Sexta-feira","Sábado","Domingo\n")

print("Segunda-feira\n", "Terça-feira\n", "Quarta-feira\n" 
, "Quinta-feira\n","Sexta-feira\n","Sábado\n","Domingo\n")

print("Uma forma mais otimizada de implementar essa questão seria usar "
, "estruturas de dados do Python, por exemplo, Tuplas,"
, " assunto futuro dessa disciplina.")


#EXERCÍCIO 10
print("Os meses do ano são:")
print("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"
, "Julho","Agosto","Setembro","Outubro", "Novembro", "Dezembro\n")

print("Janeiro\n", "Fevereiro\n", "Março\n", "Abril\n", "Maio\n", "Junho\n"
, "Julho\n","Agosto\n","Setembro\n","Outubro\n", "Novembro\n", "Dezembro\n")

print("Uma forma mais otimizada de implementar essa questão seria usar "
, "estruturas de dados do Python, por exemplo, Tuplas,"
, " assunto futuro dessa disciplina.")
