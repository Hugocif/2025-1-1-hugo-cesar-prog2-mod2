#questão 1
""" Crie um programa que possa exibir, em tela para o usuário, conceitos teóricos das
linguagens de programação e\ou da linguagem Python. Para tanto: (3,00)
1.1. O programa deve rodar em um laço de repetição. A cada iteração do laço o
programa deve solicitar uma entrada de dados, por parte do usuário, para
que o mesmo possa decidir o que deve ser feito;
1.2. Para o usuário poder finalizar o programa, deve ser digitado a palavra “sair”.
Variações de escrita, maiuscula ou minúscula, da palavra sair devem ser
aceitas pelo programa, podendo assim ser finalizado;
1.3. Ao iniciar o programa, um menu de opções numéricas, com uma descrição
textual abreviada do conceito, devem ser exibidos para o usuário;
1.4. Para poder ler os conceitos teóricos, o usuário deve digitar uma das opções
numéricas do menu que representa o conceito desejado;
1.5. Se o usuário digitar uma palavra diferente da solicitada no item 1.2, uma
mensagem deve ser exibida informando que se desejar finalizar o programa,
a palavra “sair” deve ser digitada.
1.6. Se o usuário digitar um valor numérico que não existe no menu de opções,
item 1.3, uma mensagem deve ser exibida informando “Opção Inválida” e
sugerindo que o usuário observe as opções do menu.
1.7. Linguagens de programação utilizam operadores, que tem papel importante
na construção de programas. A linguagem Python não é diferente. Crie um
item de menu chamado “Operadores”. Quando selecionado, o programa
deverá exibir a categoria, o nome e o símbolo que representa tal operador.
Categorias:
➢ Operadores Aritméticos: 03 exemplos;
➢ Operadores Comparação: 03 exemplos;
➢ Operadores Lógicos: 03 exemplos;
1.8. Crie um item de menu chamado “Palavras Reservadas no Python”. Quando
selecionado, o programa deverá exibir 10 palavras reservadas da linguagem
Python;
1.9. Crie um item de menu chamado “Tipos de dados no Python”. Quando
selecionado, o programa deverá exibir 04 tipos de dados usados na
linguagem Python;
1.10. Crie um item de menu chamado “Variável”. Quando selecionado: explique o
conceito de “Variável” no Python. Cite as regras para criação de nomes
válidos para variáveis impostas pela linguagem. Porque variáveis são
utilizadas em Python;
1.11. Essa questão será avaliada sob dois aspectos: 1º - se o programa funciona
conforme as regras descritas acima. Se os padrões de codificação e os
conceitos estudados em sala de aula foram aplicados. 2º - se as questões
conceituais\teóricas estão corretas.
"""


"""menu =print("___________________________________________\nSegue os conceitos teóricos disponíveis: \n1=Operadores Aritiméticos;\n2=Operadores de comparação;\n3=Operadores Lógicos; \nDigite sair para terminar o programa. \n___________________________________________ ")

conceitoteorico = (input("Digite o número do conceito de sua escolha: "))

if conceitoteorico == "1":
    print("Operadores Aritiméticos são operadores mátematicos. Exemplos: =, -, * e /")
    
elif conceitoteorico == "2":
    print("Operadores de comparação comparam operadores. Exemplos= =!, == e +=")
    
elif conceitoteorico == "3":
    print("Operadores lógicos. Exemplos: and, or e not")
    
elif conceitoteorico.upper() == "SAIR":
    print("Saindo do programa.")
    
else:
    print("Os caractéres digitados são inválidos. Se deseja sair do programa, digite sair: ")"""

"""Q1
1 - Funcionalidades\requitos não implementado: 1.1, 1.6, 1.8, 1.9, 1.10.
Meio certo: 1.7

NOTA DA QUESTÃO: 1,00
"""

#Questão 2
""" Crie um programa Python que verifique se um ano é bissexto. Uma mensagem
deverá ser exibida na tela informando se o ano digitado é ou não bissexto.
➢ Um ano é bissexto se for divisível por 4;
➢ Exceto se for divisível por 100, a menos que seja divisível por 400."""

"""ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")"""
    
"""Q2
CERTO 1.0
"""

#Questão 3
"""Crie um programa que rode em um laço de repetição. Exiba, a cada iteração do laço,
um menu com as seguintes opções:
➢ Contar vogais da frase;
➢ Verificar se a frase é numérica;
➢ Inverter a frase;
➢ Sair.
O usuário deverá informar uma frase via “stdin”. Ao digitar uma das opções do
menu, o programa deverá efetuar o processamento necessário e exibir o resultado
esperado. Para finalizar o programa, variações de escrita da palavra "sair" deverão
ser aceitas."""

"""while True:
    frase = input("\nDigite uma frase: ")

    print("\nMenu:")
    print("1 - Contar vogais")
    print("2 - Verificar se é numérica")
    print("3 - Inverter frase")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ").strip().lower()

    if opcao in ["4", "sair"]:
        print("Encerrando o programa.")
        break
    elif opcao == "1":
        vogais = "aeiouAEIOU"
        total = sum(1 for letra in frase if letra in vogais)
        print("Total de vogais:", total)
    elif opcao == "2":
        print("A frase é numérica." if frase.isnumeric() else "A frase não é numérica.")
    elif opcao == "3":
        print("Frase invertida:", frase[::-1])
    else:
        print("Opção inválida.")"""
        
"""Q3
CERTO 1.5

Usaram list comprehension na implementação da questão, espero que tenham ententido o conceito e a sintaxe para poderem usar nas mais diversas situações.
"""

#Questão 4
"""Escreva um programa que realiza a validação de uma senha digitada pelo usuário,
em texto claro. O mecanismo de validação deve: (2,00)
4.1. Verificar se a senha digitada possui um tamanho mínimo de 6 caracteres.
Caso não tenha, exibir mensagem informando o usuário do tamanho mínimo
da senha e finalizar o programa;
4.2. Verificar se a senha digitada possui um tamanho máximo de 20 caracteres.
Caso não tenha, exibir mensagem informando o usuário do tamanho máximo
da senha e finalizar o programa;
4.3. A senha deve ter pelo menos uma letra maiuscula. Caso não tenha, exibir
mensagem informando o usuário que a senha deve ter pelo menos uma letra
maiuscula e finalizar o programa;
4.4. A senha deve ter pelo menos uma letra minúscula. Caso não tenha, exibir
mensagem informando o usuário que a senha deve ter pelo menos uma letra
minúscula e finalizar o programa;
4.5. A senha deve ter pelo menos um caractere especial: “$#@!&”. Caso não
tenha, exibir mensagem informando o usuário que a senha deve ter pelo
menos um desses caracteres especiais “$#@!&” e finalizar o programa.
Demais caracteres especiais devem ser considerados inválidos;
4.6. Caracteres do tipo “whitespace” devem ser considerados inválidos: espaço
em branco, tabulações (\t), quebra de linha (\n), retorno do carro (\r), etc…
"""

"""def validar_senha(senha):
    if len(senha) < 6:
        print("A senha deve ter no mínimo 6 caracteres.")
        return

    if len(senha) > 20:
        print("A senha deve ter no máximo 20 caracteres.")
        return

    if not any(c.isupper() for c in senha):
        print("A senha deve conter pelo menos uma letra maiúscula.")
        return

    if not any(c.islower() for c in senha):
        print("A senha deve conter pelo menos uma letra minúscula.")
        return
    
    especiais_permitidos = "$#@!&"
    if not any(c in especiais_permitidos for c in senha):
        print("A senha deve conter pelo menos um dos seguintes caracteres especiais: $#@!&")
        return

    for c in senha:
        if c.isspace():
            print("A senha não pode conter espaços em branco ou tabulações.")
            return
        elif not (c.isalnum() or c in especiais_permitidos):
            print(f"Caractere inválido encontrado: '{c}'. Use apenas letras, números ou os caracteres: $#@!&")
            return

    print("Senha válida!")

senha = input("Digite sua senha: ")
validar_senha(senha)"""

"""Q4
1 - Criou uma função com parâmetro e um programa principal p/ usar a função como forma de resolução da questão. Boa abordagem.
Mas a função não retorna nada e ainda usa um print p/ exibir mensagem. Essa é uma responsabilidade desnecessária p/ a função,
poderia ter sido deixada p/ o programa principal. Isso poderia ter sido feito se a função retornasse um booleano por exemplo.
Além disso, usaram o return p/ finalizar o fluxo de execução e forçar a saída da função. Espero que tenham aprendido as questões
conceituais que envolvem essa abordagem, que estudem acoplamento e coesão. Outra coisa, usar estruturas condicionais e\ou de 
decisão da forma como foi usada aqui representa um estilo pobre de escrita de código, poderiam ter usado if/elif/else encadeados
, isso representa boas práticas de programação.

2 - Implementação muito parecida com a dos alunos: Vittor Sette, Felipe Ribas e Bruno, Rafael e Beatriz, Lucas e Miguel;

MEIO CERTO 1.0
"""


#Questão 5
""" O CPF, "Cadastro de Pessoas Físicas", é o registro de contribuintes individuais no
Brasil. Um número único e essencial para a identificação de pessoas físicas. Crie um
programa que verifique o formato e o tamanho de um CPF usado no Brasil. O
modelo de formato e tamanho é o: “000.000.000-00”, onde ZEROS representam
apenas NÚMEROS, e os caracteres ponto (.) e menos (-), representam os
separadores. """

"""import re

def verificar_formato_cpf(cpf):
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    
    if re.match(padrao, cpf):
        return True
    else:
        return False

cpf_usuario = input("Digite o CPF no formato 000.000.000-00: ")

if verificar_formato_cpf(cpf_usuario):
    print("CPF está no formato correto.")
else:
    print("CPF está em formato incorreto. Use: 000.000.000-00")"""
    
"""Q5
MEIO CERTO 0,5

Criaram uma função com parâmetro e um programa principal p/ usar a função como forma de resolução da questão. Boa abordagem.
Mas expressões regulares com rawstring são conhecimentos que não foram utilizados na disciplina, no momento em que essa avaliação
foi aplicada. Fiquem atentos aos conteúdos que podem ser encontrados e\ou gerados na Internet, de nada contribuirão ao aprendizado
de vocês se não tiveram conhecimentos conceituais\práticos básicos prévios que deem suporte ao aprendizado gradual.

"""

#Questão 6
"""Crie um programa que receba um valor inteiro, maior do que ZERO, informado pelo
usuário. O programa deverá exibir a “quantidade de números pares”, e a “quantidade
de números ímpares” que o valor informado pelo usuário possui."""

def contar_pares_e_impares(numero):
    pares = 0
    impares = 0

    for i in range(1, numero + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"\nNo intervalo de 1 até {numero}:")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

try:
    valor = int(input("Digite um número inteiro maior que zero: "))
    if valor <= 0:
        print("O número deve ser maior que zero.")
    else:
        contar_pares_e_impares(valor)
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
    
"""Q6
MEIO CERTO 1,5

Criaram uma função com parâmetro e um programa principal p/ usar a função como forma de resolução da questão. Boa abordagem.
Novamente, a função não retorna nada, e ainda usa um print´s p/ exibir mensagem. Essa é uma responsabilidade desnecessária p/ a função,
poderia ter sido deixada p/ o programa principal.

"""

"""
1 - Geraram um arquivo no formato pdf p/ postar no Sigaa com o código fonte, não foi esse formato solicitado nessa atividade avaliativa.
O nome do arquivo está incorreto: "DaviDebus_JoaoFeldmann.pdf". -1,5

2 - Parte da implementação muito parecida com a dos alunos: Vittor Sette, Felipe Ribas e Bruno, Rafael e Beatriz, Lucas e Miguel;

3 - O nome do arquivo está incorreto: "recuperacao.py". -0,5

Nota Geral 2,0 - 6,5 = 6,0

Amanda e Hugo
"""