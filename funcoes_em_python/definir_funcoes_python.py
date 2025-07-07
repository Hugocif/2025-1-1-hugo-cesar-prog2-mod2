import datetime
import random
import string  
from datetime import date
import time

#Questões Gerais

def é_numerico(x):
    if (x.strip().isnumeric()):
        
        return True
    else:
        
        return False
  
def variavel():
    return """
    Na programação, uma variável é um espaço de memória que armazena valores que podem ser alterados durante a execução de um 
    programa. As variáveis são elementos fundamentais da programação, independentemente da linguagem utilizada. 
                        Variável
    ______________________________
    Definição
    Um item de dados nomeado que pode armazenar diferentes valores
    ______________________________
    Função
    Armazenar e manipular valores durante a execução de um programa
    ______________________________
    Onde está localizada
    Na memória física ou virtual do computador
    ______________________________
    Como é identificada
    Por um nome descritivo ou identificador
    ______________________________
    Como é utilizada
    Declarada e atribuída um valor
    ______________________________
"""

def sintaxe():
    return """  
    Sintaxe é o conjunto de regras que definem como escrever um código de programação,
    de forma que o computador possa entender e executar as instruções. 
    _____________________________
    Sintaxe
    Regras que definem a estrutura e a forma de escrever instruções e programas
    Importância
    Fundamental para a construção de códigos e para a legibilidade do código
    ______________________________
    Elementos
    Palavras-chave, operadores, pontuação, recuo, variáveis, estruturas de controle, funções
    ______________________________
    Características
    Cada linguagem de programação tem sua própria sintaxe
    ______________________________
    Ferramentas
    Existem ferramentas e editores de código que ajudam a verificar a sintaxe
    ______________________________
    Erros
    Erros de sintaxe são um dos tipos mais comuns de erros que programadores enfrentam
    ______________________________"""
    
def Semântica():
    return """Semântica na programação é o estudo do significado de um trecho de código, ou seja, o que ele faz.
É uma área da ciência da computação que complementa a sintaxe, que define a estrutura do código. 
 __________________
|    Semântica             |        Sintaxe        |
|O que define              | A estrutura do código |
|O significado do código   |                       |
|_________|________|
"""

def laco_infinito():
    return """Um laço infinito em programação é uma sequência de instruções que se repete infinitamente, sem que seja possível 
atingir a condição de saída. É também conhecido como "repetição infinita".
 
Causas:
A variável de controle do laço não consegue atingir o último número. 
O programador escreve uma condição que nunca será satisfeita. 
O programador esquece de alterar o valor da variável de controle do laço.

Como sair:
Usar o comando "break" para forçar a saída quando uma determinada condição ocorrer.

Exemplos de uso:
No entanto, existem momentos onde isso é util como por exemplo esse codigo.
"""

#lista02_exercicios_estruturas_condicionais

def reescrever_ao_contrario(frase):
    return frase[::-1]

def demonstracao_data():
    
    return date.today()
     
def demontracao_hora():
    
    return datetime.datetime.now(). strftime("%H:%M:%S")

def gerar_senha(tamanho):
    # Define os caracteres permitidos na senha (letras maiúsculas, minúsculas e números)
    caracteres = string.ascii_letters + string.digits
    # Gera uma senha aleatória com o tamanho especificado
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def calculadora(escolha, numero1, numero2):

    if escolha == 1:
        return numero1 + numero2
    if escolha == 2:
        return numero1 * numero2
    if escolha == 3:
        return numero1 / numero2
    else:
        return numero1 - numero2

#lista_for_02_04_2025

def frase_horizontal(frase, guardado):
    for letra in frase:
        guardado.append(letra)
    return guardado

def escrever_vertical(mensagem):
    for letra in mensagem:
        print(letra)

def contagem_regresiva(contador, numero):
    for contador in range(0,21):

        print(f"Contagem: ", numero)
        time.sleep(1)
        numero-=1

def tabela_de_multiplicação(numero_do_usuario, numero):

        resultado = numero_do_usuario * numero
        return resultado
        
def contagem_regreciva():
    
    numero = 20

    for contador in range(0,21):

        time.sleep(1)
        numero-=1


numero = ''
while True:
    numero_do_usuario = input("Escolha uma das opções: ")
    
    if é_numerico(numero_do_usuario):
        print("É númerico")
        numero_do_usuario = int(numero_do_usuario)
    else:
        print("Não é númerico")
        break
    data_de_hoje = demonstracao_data()
    print(data_de_hoje)
    data_de_hoje = demontracao_hora()
    print(data_de_hoje)
    
    if numero_do_usuario == 1:
        numero = 20
        contagem = 0
        contagem_regresiva(contagem, numero)

    
    elif numero_do_usuario == 2:
        frase_do_usuario = input("Digite uma frase para reescrevela ao contrario: ")    
        frase_do_usuario = reescrever_ao_contrario(frase_do_usuario)
        print(frase_do_usuario)

    elif numero_do_usuario == 3:
        mensagem = input("Digite uma frase para reescrevela na vertical: ")
        escrever_vertical(mensagem)


    elif numero_do_usuario == 4:
        frase_na_horizontal = []
        frase_do_usuario = input("Digite uma frase para reescrevela na horizontal: ")
        frase_horizontal(frase_do_usuario, frase_na_horizontal)
        print(frase_na_horizontal)

    elif numero_do_usuario == 5:
        
        # Solicita ao usuário o número de caracteres para a senha
        tamanho = input("Digite o número de caracteres para a senha: ")
        
        if é_numerico(tamanho):
            print("É númerico")
            tamanho = int(tamanho)
        else:
            print("Não é númerico")
            break
       

        # Gera e exibe a senha
        senha = gerar_senha(tamanho)
        print("Sua senha aleatória é:", senha)
    elif numero_do_usuario == 6:
        numero = input("Escolha uma das seguintes opções:\n 1 = soma\n 2 = multiplicação\n 3 = divisão\n 4 = subtração\n 5 = sair\nescolha: ")
        
        if é_numerico(numero):
            print("É númerico")
            numero= int(numero)
        else:
            print("Não é númerico")
            break
        
        if not (numero <= 4 and numero > 0):
            break
        
        elif numero <= 4 and numero > 0:
            
            numero_da_conta = input("Escolha um numero para a conta: ")
            outro_numero_da_conta = input("Escolha outro numero para a conta: ")
            
            if é_numerico(numero_da_conta) and é_numerico(outro_numero_da_conta):
                print("É númerico")
                
                outro_numero_da_conta = int(outro_numero_da_conta)
                numero_da_conta = int(numero_da_conta)
            
                resultado = calculadora(numero, numero_da_conta, outro_numero_da_conta)
                print(resultado)
            
            else:
                print("Não é númerico")

            break
        
        
    elif numero_do_usuario == 7:
        numero_da_conta = input("Escolha a tabelha desejada: ")
        
        if é_numerico(numero_da_conta):
            
            numero_da_conta = int(numero_da_conta)
            
            for numero in range(0,11):
                
                resultado = tabela_de_multiplicação(numero_da_conta, numero)
                print(f"{numero_da_conta} X {numero} = {resultado}")
        else:
                print("Não é númerico")

    elif numero_do_usuario == 8:

        contagem_regreciva()