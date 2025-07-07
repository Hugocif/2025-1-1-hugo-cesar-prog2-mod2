#verificar o tamanho de string
mensagem = "Dia chuvoso"

print(f"caracter da mensagem: \"{mensagem}\": ", len(mensagem))

#Acessar String pelo índice
frase = "aula sobre tratamanto de string no python"
indice = 150

if indice <= len(frase) -1:
    print(f"O caracter na posição 5 da frase \"{frase}\" é", frase[indice])

else:
    print(f"O índice {indice} é valido")

#Acessar o ultimo da string
print("O ultimo caracter da frase é:", frase[-1])

for caracter in frase:
    print(caracter)

#colocar primeiro caracter com letra maiuscula
frase2 = "linguagem pythom"

frase3 = frase2.capitalize()
print(frase3)

print(frase2.title())

#Função que verifica se a frase termine com determinada palavra, função booleana
print(frase2.endswith("programação"))

if frase2.endswith("a"):
    print("")
else:
    print("")


frase3 = "Não devemos assistir as aulas."
print(frase3.replace("Não", ""))
print(frase3.replace(" ", ""))

print(f"Número de caracter \"a e A\" da frase \"{frase}\" é: ",frase.count("a") + frase.count("A"))

print(f"Retorna uma substring \"{frase}\" = ", frase[5:12])