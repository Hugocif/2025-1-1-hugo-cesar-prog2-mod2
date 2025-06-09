diasDaSemana = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira"
                    , "Sexta-feira", "Sábado", "Domingo")

mesesDoAno = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho"
                , "Agosto", "Setembro", "Outubro", "Novenbro", "Dezembro")

estacoesDoAno = ("Primavera", "Verão", "Outono", "Inverno")

listaDiasDaSemana = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira"
                    , "Sexta-feira", "Sábado", "Domingo")

listaMesesDoAno = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho"
                , "Agosto", "Setembro", "Outubro", "Novenbro", "Dezembro")

listaEstacoesDoAno = ("Primavera", "Verão", "Outono", "Inverno")

FINALIZAR_PROGRAMA = 5

listaDeCompra = ["Água", "Açucar", "Arroz", "Pão", "Leite", "Massa", "Carne"
, "Refrigerante", "Feijão", "Café", "Alface", "Tomate", "Cebola"
, "Lentilha", "Laranja"]

linguagensDeProgramacao = ["C", "C++", "Java", "Python", "Lua", "JavaScript"]

medicos = ["Dr. João", "Dr. José", "Dra. Maria", "Dra. Aparecida", "Dra. Marcela"]

"""Lembrando que passar a função imprimirEstruturaDeDados, que usa a função
print, como parâmetro de uma outra chamada a função print, fará com que o 
valor "None" seja impresso, na tela, como último valor, por causa do retorno da
função print, que está sendo chamada dentro da função imprimirEstruturaDeDados"""
def imprimirEstruturaDeDados(estruturaDeDados):
    print(estruturaDeDados)
    
def imprimirEstruturaDeDadosUsandoFor(estruturaDeDados):
    for indiceElemento in range(len(estruturaDeDados)):
        print(f" {indiceElemento} - ", estruturaDeDados[indiceElemento])
        
    print("\n")

def menuDeOpcoes():
    print("menu de opções:")
    print(" 1 - Adicionar Item\n 2 - Remover Item\n 3 - Atualizar Item\n 4 - Imprimir Itens\n 5 - Sair do Programa")

def adicionarItemListaDeCompras(lista, item):
    """Adiciona um novo item a lista de compras. Observem os parâmetros da função, será através deles
    que a operação de inclusão vai ocorrer."""
    lista.append(item)

def excluirItemListaDeCompras(lista, elemento_lista):
    try:
        lista.remove(elemento_lista) #remove o item de compra pelo nome

    except:
        print(f"Erro ao excluir \n{lista[elemento_lista]}\n ")
        
def atualizarItemListaDeCompras(lista, indice, elemento_lista):
    try:
        lista[indice] = elemento_lista #atualiza o item de compra pelo seu índice dentro da lista

    except:
        print(f"Erro ao atualizar \n{elemento_lista}\n na lista de compras")

def advinharNomesLinguagensProgramacao(lista, nomeLinguagem):
    return nomeLinguagem in lista

def procurarMedico(lista, nome):
    if nome in lista:
        return True
    else:
        return False
#---------------------------------------------------------------------------------------------------------------------------------
    
"""01 - Crie 03 variáveis do tipo tupla que contenham: os dias da semana,
os meses do ano, as estações do ano. Crie uma função, que tenha 1 parâmetro,
que imprima na tela os valores definidos em cada uma das tuplas.
"""

Dias_Da_Semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta')
Meses_Do_Ano = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
Estações_Do_Ano = ('Verão', 'Outono', 'Inverno', 'Primavera')

#Programas Principais que fazem uso das funções implementadas.

"""Lista do professor:"""
"""01 - Crie 03 variáveis do tipo tupla que contenham: os dias da semana,
os meses do ano, as estações do ano. Crie uma função, que tenha 1 parâmetro,
que imprima na tela os valores definidos em cada uma das tuplas.
"""
print("Dias da semana: ")
imprimirEstruturaDeDados(diasDaSemana)
print("\n")

print("Meses do ano: ")
imprimirEstruturaDeDados(mesesDoAno)
print("\n")

print("Estações do ano: ")
imprimirEstruturaDeDados(estacoesDoAno)
print("\n")

print("Dias da semana usando um laço for para iterar sobre a tupla: ")
imprimirEstruturaDeDadosUsandoFor(diasDaSemana)
print("\n")

print("Meses do ano usando um laço for para iterar sobre a tupla: ")
imprimirEstruturaDeDadosUsandoFor(mesesDoAno)
print("\n")

print("Estações do ano usando um laço for para iterar sobre a tupla: ")
imprimirEstruturaDeDadosUsandoFor(estacoesDoAno)
print("\n")
#---------------------------------------------------------------------------------------------------------------------------------

"""Lista do professor:"""
"""02 - Crie 03 variáveis do tipo lista que contenham: os dias da semana,
os meses do ano, as estações do ano. Crie uma função, que tenha 1 parâmetro,
que imprima na tela os valores definidos em cada uma das listas."""
print("Lista dos dias da semana: ")
imprimirEstruturaDeDados(diasDaSemana)
print("\n")

print("Lista dos meses do ano: ")
imprimirEstruturaDeDados(mesesDoAno)
print("\n")

print("Lista das estações do ano: ")
imprimirEstruturaDeDados(estacoesDoAno)
print("\n")

print("Lista dos dias da semana usando um laço for para iterar sobre a tupla: ")
imprimirEstruturaDeDadosUsandoFor(diasDaSemana)
print("\n")

print("Lista dos meses do ano usando um laço for para iterar sobre a tupla: ")
imprimirEstruturaDeDadosUsandoFor(mesesDoAno)
print("\n")

print("Lista das estações do ano usando um laço for para iterar sobre a tupla: ")
imprimirEstruturaDeDadosUsandoFor(estacoesDoAno)
print("\n")
#----------------------------------------------------------------------------------------------------------------------------------]

"""Lista do professor:"""
"""03 - Exiba o tamanho e os elementos: primeiro, terceiro e último das estruturas 
de dados criadas e inicializadas nas questões 1 e 2.
"""
print("Tamanho da Tupla dias da semana: ", len(diasDaSemana), " elementos.")
print("Tamanho da Tupla meses do ano: ", len(mesesDoAno), " elementos.")
print("Tamanho da Tupla estações do ano: ", len(estacoesDoAno), " elementos.")

print("Primeiro elemento da Tupla dias da semana: ", diasDaSemana[0])
print("Terceiro elemento da Tupla meses do ano: ", mesesDoAno[2])
print("Último elemento da Tupla dias das estações do ano: ", estacoesDoAno[-1])
#----------------------------------------------------------------------------------------------------------------------------------

"""Lista do professor:"""
"""04 - Crie uma lista de compras de supermercado com 15 itens. Através de um laço
de repetição, exiba na tela, cada um dos itens dessa lista de compras. Você
deve decidir que tipo de estrutura de dados utilizar e imprimir, logo abaixo
da lista de compras, os motivos da sua decisão, ou seja, explique porque
utilizou tal estrutura de dados."""
imprimirEstruturaDeDadosUsandoFor(listaDeCompra)
#----------------------------------------------------------------------------------------------------------------------------------

"""Lista do professor:"""
"""05 - Crie um programa que atualize a lista de compras da questão 4. O programa
deve solicitar ao usuário, através de um menu de opções, que tipo de operação 
deseja efetuar sobre a lista de compras: incluir um novo item, remover um item ou 
atualizar um item existente. Crie uma função para cada tipo de operação permitida. Após o usuário informar uma 
das opções válida do menu, o programa deve solicitar que o usuário digite o nome do produto\item para que a função 
correta seja chamada e a alteração da lista de compras possa ser feita. Implemente uma forma de encerrar o programa 
através da interação do usuário.
"""
opcaoSelecionada  = 99 # inicializado com um valor diferente do finalizar programa
itemListaDecompra = ""

while opcaoSelecionada != FINALIZAR_PROGRAMA:
    item_nao_encontrado = False
    menuDeOpcoes()
    opcaoSelecionada = input("Selecione uma das opções do Menu: ")
    
    if opcaoSelecionada == "1":
        itemListaDecompra = input("Digite o item a ser incluído na lista de compras: ")
        adicionarItemListaDeCompras(listaDeCompra, itemListaDecompra)
    
    elif opcaoSelecionada == "2":        

        itemListaDecompra = input("Digite o item a ser excluído na lista de compras: ")
        
        for indice in range(len(listaDeCompra)):
                if itemListaDecompra == listaDeCompra[indice]:
                    excluirItemListaDeCompras(listaDeCompra, itemListaDecompra) #remove o item de compra pelo nome
                    break
                
                else:
                    item_nao_encontrado = True
                
        if item_nao_encontrado:
            print (f"O item \"{itemListaDecompra}\" não existe na lista de compras.")
        
    
    elif opcaoSelecionada == "3":
        itemListaDecompra = input("Digite o item a ser atualizado na lista de compras: ")
        
        for indice, item in enumerate(listaDeCompra):
                if itemListaDecompra == item:
                    novoItem = input("Digite o novo item: ")
                    atualizarItemListaDeCompras(listaDeCompra, indice, novoItem)
                    break
                
                else:
                    item_nao_encontrado = True
                
        if item_nao_encontrado:
            print (f"O item \"{itemListaDecompra}\" não existe na lista de compras.")
        
    elif opcaoSelecionada == "4":
        print("Lista de compras:")
        imprimirEstruturaDeDadosUsandoFor(listaDeCompra)
        
    elif opcaoSelecionada == "5":
        print("Programa finalizado !!!")
        break
        
    else:
        print(f"A opção \"{opcaoSelecionada}\" não existe no menu de opções. Digite uma opção válida.")
        menuDeOpcoes()  
#----------------------------------------------------------------------------------------------------------------------------------  

"""Lista do professor:"""
"""
Questão 6 - Crie uma estrutura de dados que armazene o nome das linguagens de
programação: C, C++, JavaScript, Java, Lua e Python. Implemente um
programa que solicite ao usuário que tente adivinhar quais linguagens de
programação constam em uma lista oculta de nomes, informando, para tanto,
nomes de linguagens de programação. Exiba mensagem na tela para o
usuário informando se a linguagem consta ou não na lista oculta. A
funcionalidade de procurar em uma lista oculta de nomes deverá ser
implementada através de função.
"""
nomeLinguagem = input("Tente advinhar as linguagens de programação de uma lista oculta. Digite o nome de uma linguagem de programação: ")

if advinharNomesLinguagensProgramacao(linguagensDeProgramacao, nomeLinguagem):
    print(f"A linguagem de programação \"{nomeLinguagem}\" consta da lista oculta. Parabéns você acertou um dos nomes.")

else:
    print(f"A linguagem de programação \"{nomeLinguagem} NÃO CONSTA\" da lista oculta. Parabéns você acertou um dos nomes.")

#----------------------------------------------------------------------------------------------------------------------------------

"""Lista do professor:"""
"""
Questão 7 - Crie um programa que possa marcar uma consulta médica. Utilize uma
estrutura de dados para armazenar o nome dos médicos que atendem na
clínica. Solicite ao usuário que informe com qual profissional deseja marcar uma consulta 
médica. Implemente funções que possam: 
imprimir na tela o nome dos profissionais, procurar na lista de profissionais o nome 
informado, exibir na tela mensagem de que a consulta foi marcada com sucesso. Em
caso de falha, exibir mensagem na tela informando o usuário do ocorrido.
"""    
imprimirEstruturaDeDadosUsandoFor(medicos)

profissional = input("Digite o nome do médico que deseja marcar uma consulta: ")

if procurarMedico(medicos, profissional):
    print(f"Consulta médica marcada com o(a) {profissional}.")

else:
    print(f"O profissional \"{profissional}\" não consta na lista de médicos(as) da clínica.")
    imprimirEstruturaDeDadosUsandoFor(medicos)    
    
