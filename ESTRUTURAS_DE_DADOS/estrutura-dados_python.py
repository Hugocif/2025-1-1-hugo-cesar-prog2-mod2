"""#tuplas, listas, dicionários 

#maneiras d edeclararuma tupla
variavel_do_tipo_tupla = "a", "b", "c", "d", "e"

variavel_do_tipo_tupla =('a', 'b', 'c', 'd', 'e')

#Para criar uma tupla com um único elemento 

LetrasMinusculas =('a')

type(LetrasMinusculas)

#Outra forma de criar uma tupla é com a função integrada tuple. Sem argumentos cria uma tupla vazia

variavel_do_tipo_tupla = tuple()

variavel_do_tipo_tupla = ()

#se os argumentos 

variavel_do_tipo_tupla = tuple("sequencia")

variavel_do_tipo_tupla = ('s', 'e', 'q', 'u', 'e', 'n', 'c', 'i', 'a')

variavel_do_tipo_tupla = ('a', 'b', 'c', 'd', 'e')

variavel_do_tipo_tupla[0] = 'A'

#LISTA 

variaveldotipolista = [10,20,30,40]
variavel_do_tipo_lista = ['programação', 'banco de dados', 'redes de computadores']

variaveldotipolista2 = ['spam', 2.0, 5, [10,20]]

variavel_do_tipo_lista2 = ['programação', 'banco de dados', 'redes de computadores']
variavel_do_tipo_lista2[0] = 'programação'

variavel_do_tipo_lista2 = ['programação', 'banco de dados', 'redes de computadores']
if 'Banco de Dados' in variavel_do_tipo_lista2:
    print('true')
    
else:
    print('false')
    
variaveldotipolista3= [10, 20, 30, 40]
    
for itemdalista in variaveldotipolista3:
    print(itemdalista)
    
for item in range(len(variaveldotipolista3)):
    print("No índice ", item, " - ", variaveldotipolista3[item])
    
    if item >= 3:
     print (variaveldotipolista3[3])
    

variaveldotipolista4= [10,20,30,40]
 
for i in range(len(variaveldotipolista4)):
     variaveldotipolista4[i] = variaveldotipolista4[i]*2
        
variaveldotipolista4 =[20, 40, 60, 80]

#DICIONÁRIO

#Um dicionário é um mapeamento (chave-valor);


dicionario={
    <chave>:<valor>,
    <chave>:<valor>,
    .
    <chave>:<valor>
}


my_dict={
    1:"data",
    2:"strucure",
    3:"python",
    4:"progamming",
    5:"lenguage"
}

#Adicionar um novo item a um dicionário já criado

my_dict[6]="database"
print(my_dict)

# Metodos mais comuns:


# clear()
# get(<chave>)
# items()

"""