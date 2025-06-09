#1. Crie uma tupla com 5 nomes e imprima o segundo nome.

tupla_com_nomes = ('antonio', 'toninho', 'toni toni', 'egoista', 'tonhão')

print(tupla_com_nomes[1])

"""Lista do professor:"""
#1. Crie uma tupla com 5 nomes e imprima o segundo nome.

nomes = ("Ana", "Bruno", "Carlos", "Diana", "Eduardo")
print("O segundo nome da lista é: ", nomes[1])
#----------------------------------------------------------------------------------------------------------------------------------
#2. Crie uma lista com 5 números inteiros e imprima a soma de todos os elementos.

tupla_com_5_numeros = (1, 2, 3, 4, 5)

print(sum(tupla_com_5_numeros))

"""Lista do professor:"""
#2. Crie uma lista com 5 números inteiros e imprima a soma de todos os elementos.

numeros = [1, 2, 3, 4, 5]
print(f"A soma dos números contidos na lista é: {sum(numeros)}")
#----------------------------------------------------------------------------------------------------------------------------------
#3. Crie um dicionário com 3 pares (chave: valor) representando um aluno (nome, idade, curso). Imprima cada valor.

dicionario_com_3_valores = {
    1: "toninho",
    2: "tonhã",
    3: "antonio"
}

print(dicionario_com_3_valores[1])
print(dicionario_com_3_valores[2])
print(dicionario_com_3_valores[3])

"""Lista do professor:"""
#3. Crie um dicionário com 3 pares (chave: valor) representando um aluno (nome, idade, curso). Imprima cada valor.

aluno = {"nome": "João", "idade": 20, "curso": "Engenharia"
    , "nome1": "Maria", "idade1": 19, "curso1": "Engenharia"
    , "nome2": "Fernanda", "idade2": 20, "curso2": "Engenharia"}
for valor in aluno.values():
    print(valor)
#----------------------------------------------------------------------------------------------------------------------------------
#4. Converta uma lista em tupla e imprima o tipo antes e depois da conversão

lista_tupla = [2, 4]

print(type(lista_tupla))

lista_tupla = tuple(lista_tupla)

print(type(lista_tupla))

"""Lista do professor:"""
#4. Converta uma lista em tupla e imprima o tipo antes e depois da conversão.

lista = [1, 2, 3]
print("Essa é um tipo lista: ", type(lista))
tupla = tuple(lista)
print("Essa é um tipo tupla: ", type(lista))

#----------------------------------------------------------------------------------------------------------------------------------
# 5. Adicione um novo elemento ao final de uma lista de frutas e imprima a nova lista.

lista_de_frutas =['laranja', 'maça', 'kiwi']

lista_de_frutas.append('banana')

"""Lista do professor:"""
#5. Adicione um novo elemento ao final de uma lista de frutas e imprima a nova lista.

frutas = ["maçã", "banana", "laranja"]
print(f"Lista original: {frutas}")
frutas.append("uva")
print(f"Nova lista com um novo item adicionado: {frutas}")
#----------------------------------------------------------------------------------------------------------------------------------
#6. Crie uma lista com números de 1 a 10. Remova os números pares da lista e imprima o resultado.

numeros        = list(range(1, 11))

#Em Python, list comprehension é uma forma compacta e eficiente de criar listas.

numerosImPares = [n for n in numeros if n % 2 != 0]

print("Usando list comprehension, gerou-se apenas os números ímpares: ", numerosImPares)
#----------------------------------------------------------------------------------------------------------------------------------
#7. Dado um dicionário com nomes de produtos e preços, encontre o produto mais caro.

produtos = {"arroz": 5.5, "feijão": 7.8, "carne": 25.0}
mais_caro = max(produtos, key=produtos.get)
print(mais_caro)
#----------------------------------------------------------------------------------------------------------------------------------
#8. Crie uma tupla com 10 números e encontre o maior e o menor valor.

tupla_numeros = (10, 3, 5, 8, 2, 7, 12, 1, 4, 9)
print(f"O maior valor da lista é: {max(tupla_numeros)} e o menor é: {min(tupla_numeros)}")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#9. Crie uma lista de dicionários, onde cada dicionário representa um aluno com as chaves: "nome", "nota". Imprima os nomes dos alunos com nota maior que 7.

alunos = [{"nome": "Alice", "nota": 8},
          {"nome": "Beto", "nota": 6},
          {"nome": "Clara", "nota": 9}]

print("Os alunos com nota maior do que 7 são: ")
for aluno in alunos:
    if aluno["nota"] > 7:
        print(aluno["nome"])
#----------------------------------------------------------------------------------------------------------------------------------
#10. Inverta uma lista de palavras e imprima o resultado.

palavras = ["python", "é", "divertido"]
palavras.reverse()
print(palavras)
#----------------------------------------------------------------------------------------------------------------------------------
#11. Crie um dicionário onde a chave é o nome de uma pessoa e o valor é uma lista de suas notas. Imprima a média de cada pessoa.

notas = {
    "Carlos": [7, 8, 9],
    "Amanda": [10, 9, 8],
    "Lucas": [5, 6, 7]
}
for nome, lista_notas in notas.items():
    media = sum(lista_notas) / len(lista_notas)
    print(f"A média do(a) \"{nome}\" é: {media:.2f}")
#----------------------------------------------------------------------------------------------------------------------------------
#12. Dado uma lista de tuplas representando transações (cliente, valor), calcule o total gasto por cada cliente.

transacoes = [("Ana", 100), ("Bruno", 50), ("Ana", 75), ("Bruno", 25)]
total_por_cliente = {}
for cliente, valor in transacoes:
    total_por_cliente[cliente] = total_por_cliente.get(cliente, 0) + valor
print(total_por_cliente)
#----------------------------------------------------------------------------------------------------------------------------------
#13. Crie uma função que recebe uma lista de strings e retorna um dicionário com a contagem de cada letra.

def contar_letras(lista):
    contador = {}
    for palavra in lista:
        for letra in palavra:
            if letra.isalpha():
                contador[letra] = contador.get(letra, 0) + 1
    return contador

print(contar_letras(["banana", "abacaxi", "uva"]))
#----------------------------------------------------------------------------------------------------------------------------------
#14. Crie um dicionário invertido: dado um dicionário {chave: valor}, crie um novo dicionário {valor: chave}.

original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print(invertido)
#----------------------------------------------------------------------------------------------------------------------------------
#15. Crie uma lista de números e use um dicionário para contar quantas vezes cada número aparece na lista.

numeros = [1, 2, 2, 3, 1, 4, 2, 5]
contagem = {}

for numero in numeros:
    contagem[numero] = contagem.get(numero, 0) + 1

print(contagem)