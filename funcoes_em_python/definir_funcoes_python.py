#LISTA DE EXERCÍCIOS ESTRUTURA DE REPETIÇÃO “FOR”

#1)Escrita ao contrário

def PalavraEscolhida(PalavraVirar)
    
     
for itemdalista in "Instituto Federal De Santa Catarina":
 print(itemdalista)

mensagemASerExibidaNaHorizontal = ''

#3)Tabuada

def Tabuada(NumeroCalcular):
    NumerosCalculados = []
    
    for i in range(1, 11):
        NumerosCalculados.append(i * NumeroCalcular)
        
    return NumerosCalculados

numero = input("informe o nuero p/ calcular a tabuada: ")

print(Tabuada(int(numero)))