OPCAO_MANIPULAR_LISTA = 1
OPCAO_MEDIA_DICIONARIO = 2
OPCAO_CONTAGEM_DE_LETRAS = 3
OPCAO_MANIPULAR_DATAS = 4
OPCAO_USAR_TUPLAS = 5


MENU_OPCAO_MANIPULAR_LISTA = "1- Manipular listas"
MENU_OPCAO_MEDIA_DICIONARIO = "2- Media usando dicionario"
MENU_OPCAO_CONTAGEM_DE_LETRAS = "3- Contagem de letras em dicionario"
MENU_OPCAO_MANIPULAR_DATAS = "4- Manipulacão da Data"
MENU_OPCAO_USAR_TUPLAS = "5- Usando Tuplas"

ADICIONAR_ITEM = 1
REMOVER_ITEM = 2
ATUALIZAR_ITEM = 3
IMPRIMIR_LISTA = 4
FINALIZAR = 5

LINGUAGENS_PROGRAMACAO = ["Python", "JavaScript", "Java", "C++", "C#", "PHP", "TypeScript", "Kotlin", "Swift", "Ruby"]

def exibirMenuPrincipal():
    print("Opcões: ")
    print(" " + MENU_OPCAO_MANIPULAR_LISTA + "\n" + MENU_OPCAO_MEDIA_DICIONARIO + "\n" + MENU_OPCAO_CONTAGEM_DE_LETRAS + "\n" + MENU_OPCAO_MANIPULAR_DATAS + "\n" + MENU_OPCAO_USAR_TUPLAS)

def exibirMenuSecundarioLista():
    print("Menu de opções listas: ")
    print(" 1 - Adicionar item;\n 2 - Remover item;\n 3 - Atualizar item;\n 4 - atualizar um item;\n 5 - Finalizar manipulação listas;")
    
def adicionarItemLista(Lista, item):
    #Adciona um novo item na lista passada por parametro. O item a ser adicionado também foi passado npor parametro
    Lista.append(item)
    


#Q1 - PROGRAMA PRINCIPAL    



UsuarioDigitadoSair = False

exibirMenuPrincipal()

while not UsuarioDigitadoSair:
    
    opcaoDigitadaPeloUsuario = input("informe a opcao de menu desejada: ")
    
    #validar opcao desejada
    if opcaoDigitadaPeloUsuario.strip().isnumeric()  == True:
        
        if int(opcaoDigitadaPeloUsuario) == OPCAO_MANIPULAR_LISTA:
            #chamar funcoes de manipulacao de string
            print("\n")
            exibirMenuSecundarioLista()
            
            opcaoUsuario = input("Digite sua escolha")
            
            if opcaoUsuario.strip().isnumeric() == True:
                
                if int(opcaoUsuario) == FINALIZAR:
                    print("Finalizada a manipulação de listas. . . \n")
                    
                else:
                    while int(opcaoUsuario) != FINALIZAR:
                        if int(opcaoUsuario) == ADICIONAR_ITEM:
                            
                            item = input("Digite o item a ser adicionado na lista: ")
                            
                            adicionarItemLista(LINGUAGENS_PROGRAMACAO, item)
                            
                    
                        elif int(opcaoUsuario) == REMOVER_ITEM:
                            print("Remover")
                            
                        
                        elif int(opcaoUsuario) == ATUALIZAR_ITEM:
                            print("Atualizar")
                            
                        
                        elif int(opcaoUsuario) == IMPRIMIR_LISTA:
                            print("Imprimir")
                            
                        
                        elif(opcaoUsuario) == FINALIZAR:
                            print("bye")
                            

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