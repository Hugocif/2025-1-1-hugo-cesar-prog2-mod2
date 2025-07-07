import time
from pathlib import Path
import platform

"""
def ler_arquivo(arquivo):
    
    try:
    
        with open(arquivo, 'r', encoding='uft-8') as f:
    
            return f.read()

    except FileNotFoundError:
    
        print("Erro: Arquivo não encontrado.")
    
    except Exception as e:
    
        print("Ocorreu um erro inesperado: {e}")
        
    return None
    


#With open fecha o arquivo para você

with open('exemplo.txt', 'r', encoding='uft-8') as f:
    
    conteudo = f.read() #Lê todo conteúdo
    
with open('exemplo.txt', 'r', encoding='uft-8') as f:
    
    linhas = f.readlines() #Lê linha por linha em lista
    
f.seek(0) #Move cursor 

with open('exemplo.txt', 'r', encoding='uft-8') as f:
    
    linhas = f.readline() #Lê uma linha por vez
    
#Escrevendo texto

#O modo de abertura 'w' trunca o arquivo, ou seja, apaga o arquivo, caso ele
#exista, senão um novo arquivo e insere o conteúdo.


with open('saida.txt', 'w', encoding='uft-8') as f:
    
    f.write("primeira linha") 

    f.write("primeira linha")
    
#Acrescenta conteúdo

#O modo de abertura "a" adiciona o conteúdo no final do arquivo, caso ele
#exista, senão cria um novo arquivo e insere o conteúdo.

with open('saida.txt', 'a', encoding='uft-8') as f:
    
    f.write("\nNova linha") 
    
#Write() não adiciona quebra de linha automaticamente

#conbine com join() para lista de string:

linhas = ["linha 1", "linha 2", "linha 3"]

with open('saida.txt', 'w', encoding='uft-8') as f:
    
    f.write("\n".join("Nova linha")) 
    
with open('imagem.jpg', 'rb') as img:
    
    dados = img .read()
    
with open('copia.jpg', 'wb') as copia:
    
    copia.write(dados)

with open('log.txt', 'r', encoding='uft-8') as f:
    
    for linha in f:
        
        print(linha.strip()) #Strip remove \n
        
try:
    
    with open('log.txt', 'r', encoding='uft-8') as f:
    
        conteudo = f.read()

except FileNotFoundError:
    
    print("Arquivo não encontrado.")
    
except PermissionError:
    
    print("Permissão negada para abrir o arquivo")
    
except Exception as e:
    
    print("Ocorreu um erro inesperado: {e}")
    """
def ler_arquivo_readlines(nome_de_arquivo):
    try:
    
        with open(nome_de_arquivo, "r") as arquivo:
        
            linha_de_linhas = arquivo.readlines()
            
            for linha in linha_de_linhas:
                
                print(linha)
                time.sleep(0.1)
        
    except Exception as e:
    
        print(f"Ocorreu um erro ao ler o arquivo: \"{nome_de_arquivo}\" - {e}")
        
arquivo_txt = str(Path.cwd()) + "/MANIPULAÇÃO_DE_ARQUIVOS/arquivo_csv/br_ibge_censo_2022_alfabetizacao_grupo_idade_sexo_raca.csv"
        

print("caminho completo arquivo: ", arquivo_txt)

ler_arquivo_readlines(arquivo_txt)
    
def ler_arquivo_readline(nome_de_arquivo):
    try:
    
        with open(nome_de_arquivo, "r") as arquivo:
        
            arquivo.readline()
            
            for linha in arquivo:
                
                print(arquivo.readline())
                time.sleep(0.1)
        
    except Exception as e:
    
        print(f"Ocorreu um erro ao ler o arquivo: \"{nome_de_arquivo}\" - {e}")
        
arquivo_txt = str(Path.cwd()) + "/MANIPULAÇÃO_DE_ARQUIVOS/arquivos_txt/indice_tabela.txt"
        

print("caminho completo arquivo: ", arquivo_txt)

ler_arquivo_readline(arquivo_txt)