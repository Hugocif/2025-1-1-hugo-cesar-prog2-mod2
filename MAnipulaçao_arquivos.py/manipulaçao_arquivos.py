from pathlib import Path
import time
import platform
arquivo_txt = ""
arquivo_csv = ""
"""
def ler_arquivo(arquivo_caminho_completo_extensao):
    try:

    except FileNotFoundError:
       print ("Erro: o arquivo\") 
"""

nome_caminho_completo_arquivo_e_extensao = "manipulacao_arquivos/arquivos.txt/indices_tabelas.txt"

#Exercício 1: Leitura e Arquivo
#Crie um programa que leia e exiba o conteúdo de um arquivo chamado dados.txt. caso o arquivo não exista, capture a exceção e 
#exiba uma mensagem apropriada.

def ler_arquivo(arquivo_caminho_completo_extensao):
    try:
        with open(arquivo_caminho_completo_extensao, 'r') as arquivo :
            conteudo_arquivo = arquivo.read()
            print (conteudo_arquivo)
        
    except FileNotFoundError:
        print ("Erro: Arquivo não existe.")

#Exercícios 2: Escrita em arquivo
#Crie uma lista que receba uma lista de strings e escreva cada item em uma nova linha de um arquivo chamado Saida.txt.

def escrita_arquivo(saida_txt):
    try:
        lista_geral = []
        lista_locomotivas   = ["carro", "moto", "barco"]
        lista_frutas        = ["banana", "manga", "maca"]
        lista_esportes      = ["volei", "futebol", "tenis de mesa"]
        lista_geral.append (lista_esportes)
        lista_geral.append (lista_frutas)
        lista_geral.append (lista_locomotivas)
        
        with open(saida_txt, 'w') as arquivo:
            arquivo.write ("\n".join(lista_geral))
            return arquivo
            
    except FileNotFoundError:
        return ("Arquivo não encontrado.")


#exercício 3: Contagem de linhas
#Crie uma função contador_de_linhas que leia um arquivo e retorne o número total de linhas.
def contagem_linhas(arquivo_contagem):
    try:
        with open(arquivo_contagem, 'r') as arquivo:
            linhas = arquivo.readlines()
            return len(linhas)
        
    except FileNotFoundError:
        return ("Arquivo não encontrado.")
   

#Exercício 4: Copiar arquivo
#Implemente uma função que copie o conteúdo de um arquivo para outro. Ambos os nomes dos arquivos devem ser passados como parâmetros.

#Exercicio 5: Manipulação com With e tratamento de exeções
#Escreva um código que aba um arquivo com o bloco with, leia o conteudo e conte quantas palavras ele possui. Utilize tratamento de exeções 
#para lidar com possiveis erros.


def ler_arquivos_com_laco_rapeticao(arquivo_caminho_completo_extensao):
    try:
        with open(arquivo_caminho_completo_extensao, 'r') as arquivo:
            for linha in arquivo:
                print(linha.strip())
                time.sleep(1)
                
    except FileNotFoundError:
        return ("Arquivo não encontrado.")

# print ("1. Leitura e arquivo\n 2.Escrita em arquivo\n 3. Contagem de linhas\n 4. Copiar arquivo\n 5. ")
# escolha_usuario = input("Escolha um opção ou digite 'sair' para sair")

arquivo_txt = str(Path.cwd()) + r"/manipulacao_arquivos/arquivos.txt/indices_tabelas.txt"

print ("Diretório de trabalho: ", arquivo_txt)
ler_arquivo(arquivo_txt)

# if escolha_usuario.upper == "SAIR":
#     print ("Saindo do programa...")
    
def ler_arquivo_com_readlines(arquivo_caminho_completo_extensao):
    try:
        with open(arquivo_caminho_completo_extensao, "r", encoding = "utf-8") as arquivo:
            #Lê todas as lihas do arquivo e retorna uma lista de strings
            lista_de_linhas = arquivo.readline()
        
            for linha in lista_de_linhas:
                print (linha)
                time.sleep(1)
    
    except Exception as e:
        print (f"Erro ao ler o arquivo \"{arquivo_caminho_completo_extensao}\" - \{e} ")


def ler_arquivo_readline(arquivo_caminho_completo_extensao): 
    try:
        with open(arquivo_caminho_completo_extensao, "r", encoding = "utf-8") as arquivo:
            #Lê todas as lihas do arquivo e retorna uma lista de strings

            for linha in arquivo:
                print (arquivo.readline())
   
    except Exception as e:
        print (f"Erro ao ler o arquivo \"{arquivo_caminho_completo_extensao}\" - \{e} ")

#Programa principal

#marcador rawstring r
arquivo_txt = str(Path.cwd()) + r"/manipulacao_arquivos/arquivos.txt/indices_tabelas.txt"
arquivos_csv = str(Path.cwd()) + r"/manipulacao_arquivos/arquivos_csv/br_ibge_censo_2022_alfabetizacao"

print ("Caminho completo arquivo: ", arquivo_txt)
ler_arquivo_com_readlines(arquivo_txt)
print (ler_arquivo_readline)