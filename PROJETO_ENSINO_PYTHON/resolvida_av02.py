OPCAO_MANIPULAR_LISTA = 1
OPCAO_MEDIA_DICIONARIO = 2
OPCAO_CONTAGEM_DE_LETRAS = 3
OPCAO_MANIPULAR_DATAS = 4
OPCAO_USAR_TUPLAS = 5


MENU_OPCAO_MANIPULAR_LISTA = "1- Manipular listas"
MENU_OPCAO_MEDIA_DICIONARIO = "2 - Média usando dicionário"
MENU_OPCAO_CONTAGEM_DE_LETRAS = "3 - Contagem de letras com dicionário"
MENU_OPCAO_MANIPULAR_DATAS = "4 - Manipulação de Datas"
MENU_OPCAO_USAR_TUPLAS = "5 - Usando Tuplas"


LINGUAGENS_PROGRAMACAO = ["Python", "JavaScript", "Java", "C++", "C#", "PHP", "TypeScript", "Kotlin", "Swift", "Ruby"]

ADICIONAR_ITEM = 1
REMOVER_ITEM = 2
ATUALIZAR_ITEM = 3
IMPRIMIR_LISTA = 4
FINALIZAR = 5

alunos_notas = {
    "Antonio": [7, 8, 9], 
    "Vinicius": [10, 9, 8],
    "Miguel": [5, 6, 7],
    "Thyago": [9, 9, 10],
    "Aline": [7, 6, 7]
}


def exibirMenuPrincipal():
    print("Opções: ")
    print(" " + MENU_OPCAO_MANIPULAR_LISTA + "\n" + MENU_OPCAO_MEDIA_DICIONARIO + "\n" + MENU_OPCAO_CONTAGEM_DE_LETRAS + "\n" + MENU_OPCAO_MANIPULAR_DATAS + "\n" + MENU_OPCAO_USAR_TUPLAS)

def exibirMenuSecundarioLista():
    print("Menu de opções listas: ")
    print(" 1 - Adicionar item;\n 2 - Remover item;\n 3 - Atualizar item;\n 4 - Imprimir lista;\n 5 - Finalizar manipulação listas;")

def adicionarItemLista(lista, item):
    #Adiciona um novo item na lista passada por parâmetro. O item a ser adicionado também foi passado por parâmetro.
    lista.append(item)

def imprimirLista(lista):
    for IndiceElemento, nomeElemento in enumerate(lista):
        print(f"{IndiceElemento} - {nomeElemento}")

def excludeItemListaLinguagemProgragacaoMeoDeos(lista, indice_elemento):
    try:
        lista.pop(indice_elemento)
    except Exception as listError:
        print(f"Erro ao excluir item lista: {listError} ")

def excluirItemPeloNome(lista, nome_elemento):
    try:
        lista.pop(nome_elemento)
    except Exception as listError:
        print(f"Erro ao excluir item lista: {listError} ")
        
def addnewitem(lista, indice, item_new):
    try:
        lista[indice] = item_new
    except Exception as listError:
        print(f"Erro ao incluir item lista: {listError} ")

#Q1 - PROGRAMA PRINCIPAL 

UsuarioNaoDigitouSair = False

exibirMenuPrincipal()

while not UsuarioNaoDigitouSair:

    opcaoDigitadaPeloUsuario = input("Informe a opção desejada: ")
    
    
    #validar opção digitada
    if opcaoDigitadaPeloUsuario.strip().isnumeric() == True:

        if int(opcaoDigitadaPeloUsuario) == OPCAO_MANIPULAR_LISTA:
            #CHAMAR FUNÇÕES DE MUNIPULAÇÃO DE STRING
            print("\n")
            imprimirLista(LINGUAGENS_PROGRAMACAO)
            exibirMenuSecundarioLista()

            opcao = input("Digite sua escolha: ")

            if opcao.strip().isnumeric() ==True:

                if int(opcao) == FINALIZAR:
                    print("Finalizada a manipulação de listas. . . \n")

                else:
                    while int(opcao) != FINALIZAR:
                        if int(opcao) == ADICIONAR_ITEM:

                            item = input("Digite o item a ser adicionado na lista: ")

                            adicionarItemLista(LINGUAGENS_PROGRAMACAO, item)


                        elif int(opcao) == REMOVER_ITEM:
                            print("Remover")
                            #excludeItemListaLinguagemProgragacaoMeoDeos(lista, indice_elemento)

                            item_nao_encontrado = True

                            itemLista = input("Digite o nome da linguagem de programação a ser excuída: ")

                            for indice, item in enumerate(LINGUAGENS_PROGRAMACAO):
                                if itemLista.upper()== LINGUAGENS_PROGRAMACAO[indice].upper():
                                    excludeItemListaLinguagemProgragacaoMeoDeos(LINGUAGENS_PROGRAMACAO, indice)

                                    item_nao_encontrado = False
                                    print(f"\"{itemLista}\" foi excluído com sucesso!\n")
                                    break
                            if item_nao_encontrado:
                                print(f"O elemento \"{itemLista}\" não existe na lista de linguagens de programação.")


                        elif int(opcao) == ATUALIZAR_ITEM:
                            item_nao_encontrado3 = True

                            item_update = input("Digite o nome da linguagem de programação a ser atualizada: ")

                            for indice, item in enumerate(LINGUAGENS_PROGRAMACAO):
                                if item_update.upper()== LINGUAGENS_PROGRAMACAO[indice].upper():
                                    item_newest = input("Digite o nome da nova linguagem: ")

                                    addnewitem(LINGUAGENS_PROGRAMACAO, indice, item_newest)

                                    item_nao_encontrado3 = False
                                    print(f"\"{item_newest}\" foi atualizado com sucesso!\n")
                                    break
                            if item_nao_encontrado3:
                                print(f"O elemento \"{item_newest}\" não existe na lista de linguagens de programação.")


                        elif int(opcao) == IMPRIMIR_LISTA:
                            imprimirLista(LINGUAGENS_PROGRAMACAO)


                        elif(opcao) == FINALIZAR:
                            print("bye")
                            break

                        else:
                            print(f"\"{opcao}\" não existe no menu de listas...")

                        opcao = input("Informe uma opção de menu desejada: ")

                        if not opcao.strip().isnumeric():
                            print("A opção \"{opcao}\" não existe no menu de listas, saindo...")
                            break


            else:
                print("Opção inválida. A opção \"{opcaoUsuario}\" não existe no menu Lista.")
                #exibe o menu de ações novamente
                exibirMenuSecundarioLista()

                break


        elif int(opcaoDigitadaPeloUsuario)== OPCAO_MEDIA_DICIONARIO:
            print()

        elif int(opcaoDigitadaPeloUsuario) == OPCAO_CONTAGEM_DE_LETRAS:
            print()

        elif int(opcaoDigitadaPeloUsuario) == OPCAO_MANIPULAR_DATAS:
            print()

        elif int(opcaoDigitadaPeloUsuario) == OPCAO_USAR_TUPLAS:
            print()

        else:
            print("")




    else:
        if opcaoDigitadaPeloUsuario.lower() == "sair":
        #atualiza o controle do laço infinito e sai do programa
            UsuarioNaoDigitouSair = True

        else:
            print("Opção inválida. A opção \"{opcaoDigitadaPeloUsuario}\" não existe no menu de opções.")
            exibirMenuPrincipal()
            
            