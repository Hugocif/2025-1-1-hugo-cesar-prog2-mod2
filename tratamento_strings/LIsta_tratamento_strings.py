#1 - Crie uma função que receba uma string como parâmetro, e retorne uma string em maiúsculo da string que foi passada por parâmetro.

def maiusculador(palavra):
    return palavra.strip().upper()

palavrinha = input("escreva: ")
print(maiusculador(palavrinha))




"""2 – Crie uma função que receba 2 parâmetros: o 1º parâmetro deve ser uma frase do tipo string; o 2º
parâmetro deve ser uma palavra do tipo string. A função deverá retornar True se a palavra estiver
na frase passada como parâmetro, caso contrário, deverá retornar False."""
def palavra_na_frase(frase, palavra):

    if frase.count(palavra) > 0:
        return True
frase_1 = input("escreva uma frase: ")

sua_palavra = input("escreva uma palavra: ")

if palavra_na_frase(frase_1, sua_palavra):
    print(f"\"{frase_1}\" contem \"{sua_palavra}\"")
else:
    print(f"\"{frase_1}\" não contem \"{sua_palavra}\"")
"""3 – Crie uma função que receba 3 parâmetros:
➢ 1º parâmetro deve ser uma frase;
➢ 2º parâmetro deve ser uma palavra que esteja na frase;
➢ 3º parâmetro deve ser uma nova palavra, que vai substituir na frase do 1º parâmetro, a
palavra passada no 2º parâmetro.
A função deverá retornar uma nova frase contendo a alteração solicitada no requisito da função."""
def palavra_na_frase_com_substituição(frase, palavra, substituir):

    if frase.count(palavra) > 0:
        return frase.replace(palavra, substituir)
        
frase_1 = input("escreva uma frase: ")

sua_palavra = input("escreva uma palavra que esteja na frase: ")

outra_palavra = input("escreva uma palavra para substituir a anterior: ")

print(palavra_na_frase_com_substituição(frase_1, sua_palavra, outra_palavra))

"""4 – Crie uma função que receba uma palavra e verifique se ela é um palíndromo (ignorar espaços e
maiúsculas/minúsculas). A função deve retornar um booleano."""

def palindromo_verificador(frase):
    
    if frase == frase[::-1]:
        
        return True

    else:
        
        return False

frase_1 = input("escreva uma frase: ")

if palindromo_verificador(frase_1):
    
    print(f"A frase {frase_1} é um palíndromo")
    
else:
    
    print(f"A frase {frase_1} não é um palíndromo")

#5 – Crie uma função que receba um texto como parâmetro. A função deve retornar a quantidade de vogais do texto.

def contador_de_vogais(frase):
    
    numero_de_vogais = frase.lower().count("a") +frase.lower().count("e") + frase.lower().count("i") + frase.lower().count("o") + frase.lower().count("u")
    
    return numero_de_vogais

numero_de_vogais = 0

frase_1 = input("escreva uma frase: ")

numero_de_vogais = contador_de_vogais(frase_1)

print(f"A frase \"{frase_1}\" contem {numero_de_vogais} vogais")

#6 – Crie uma função que receba uma frase como parâmetro e retorne uma nova string que é a #primeira palavra dessa frase.

def primeira_palavra(frase):
    
    palavras = frase.split()
    
    if palavras:
        
        return palavras[0]
    
frase_1 = input("escreva uma frase: ")

primeira_palavra_da_frase = primeira_palavra(frase_1)

print(f"A primeira palavra da frase \"{frase_1}\" é \"{primeira_palavra_da_frase}\"")

"""7 – Crie uma função que receba 3 parâmetros:
➢ 1º parâmetro deve ser uma frase;
➢ 2º parâmetro deve ser um caracter (uma letra) que será utilizado p/ saber se a frase inicia
com esse caracter;
➢ 3º parâmetro deve ser um caracter (uma letra) que será utilizado p/ saber se a frase termina
com esse caracter.
A função deve usar expressões lógicas e retornar um booleano."""

def verificador_de_inicio_e_fim(frase, começo, final):
    
    if frase[0] == começo and frase[-1] == final:
        
        return True


frase_1 = input("escreva uma frase: ")

letra_inicial = input("Digite uma letra: ")

letra_final = input("Digite uma letra: ")

if verificador_de_inicio_e_fim(frase_1, letra_inicial, letra_final):
    
    print(f"A primeira letra da frase \"{frase_1}\" é \"{letra_inicial}\" e a ultima é \"{letra_final}\"")
    
else:
    
    print(f"A primeira letra da frase \"{frase_1}\" não é \"{letra_inicial}\" e a ultima não é \"{letra_final}\"")
#8 – Crie uma função que receba um texto como parâmetro e retorne um valor inteiro que represente a quantidade de palavra desse texto.

def contador_de_palavras(frase, contador_de_palavras_na_frase):
    
    palavras = frase.split()
    for palavra in palavras:
        

        contador_de_palavras_na_frase += 1
        
    return contador_de_palavras_na_frase 

frase_1 = input("escreva uma frase: ")
contador = 0
contador = contador_de_palavras(frase_1, contador)

print(f"A frase \"{frase_1}\" tem {contador} palavras")

"""9 – Crie uma função que receba um texto como parâmetro que contenha pontuação: pontos, vírgulas
e pontos de exclamação. A função deverá remover essa pontuação e retornar um novo texto."""

def destruidor_de_pontos(frase):
    
    frase2 = frase.replace(".", "").replace(",", "").replace("!", "")
    
    
    return frase2

frase_pontuada = input("escreva uma frase com pontuação: ")

frase_destruida = destruidor_de_pontos(frase_pontuada)

print(frase_destruida)