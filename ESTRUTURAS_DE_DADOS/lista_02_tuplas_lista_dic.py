#1. Crie uma tupla com 5 nomes e imprima o segundo nome.

tupla_com_nomes = ('antonio', 'toninho', 'toni toni', 'egoista', 'tonhão')

print(tupla_com_nomes[1])

#2. Crie uma lista com 5 números inteiros e imprima a soma de todos os elementos.

tupla_com_5_numeros = (1, 2, 3, 4, 5)

print(sum(tupla_com_5_numeros))

#3. Crie um dicionário com 3 pares (chave: valor) representando um aluno (nome, idade, curso). Imprima cada valor.

dicionario_com_3_valores = {
    1: "toninho",
    2: "tonhã",
    3: "antonio"
}

print(dicionario_com_3_valores[1])
print(dicionario_com_3_valores[2])
print(dicionario_com_3_valores[3])

#4. Converta uma lista em tupla e imprima o tipo antes e depois da conversão

lista_tupla = [2, 4]

print(type(lista_tupla))

lista_tupla = tuple(lista_tupla)

print(type(lista_tupla))

# 5. Adicione um novo elemento ao final de uma lista de frutas e imprima a nova lista.

lista_de_frutas =['laranja', 'maça', 'kiwi']

lista_de_frutas.append('banana')