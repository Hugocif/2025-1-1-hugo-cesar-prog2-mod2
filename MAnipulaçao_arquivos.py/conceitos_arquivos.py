



with open('exeple.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()  #Le todo o conteúdo
    
    
with open('exemplo.txt', 'r', econding='utf8') as f:
    linhas = f.readlines()  #Le linha por linha em lista 
       
f.seek(0) #mova o cursor para o inicio

with open('exemplo.txt', 'r', econding='utf8') as f:
 linhas = f.readlines()  #Le uma linha por vez
 
#EScreva um texto 

#o modo de abertura "W" trunca o arquivo, ou seja, apaga o arquivo, cas el
#exista, senao cria um novo arquivo e insere o conteudo 
 
with open('saida.txt', 'w', econding='utf8') as f:
    f.write("primeira linha.\n")
    
    f.write("segunda linha.")
    
    
#Acrescentando conteudo 

#O modo de abertura "a" adiciona o conteudo no final do arquivo, caso ele
#exista, senão cria um novo arquivo e insere o conteudo 

with open('saida.txt', 'r', econding='utf8') as f:
      f.write("\Nova LInha adicionada.")
      
      
#write() nao adiciona quebra de linha automaticamente
#combine com join()para listas de strngs:
#linhas =["linha1", "linha2", "linha3"]

with open('lista.txt', 'w', econding='utf8') as f:
 f.write("\n".join(linhas))


with open('imagem.jpg', 'rb') as img:
    dados =img.read()
    
with open('copia.jpg', 'wb') as copia:
    copia.write(dados)

with open('log.txt', 'r') as f:
     for linha in f:
         print(linha.stri()) #strip remove \n
         
try:
   with open('log.txt', 'r', encoding='utf-8') as f:
       conteudo=f.read()
       
except FileNotFoundError:
    print("Aquivo não encontrado.")       

except PermissionError:
    print("Arquivo nao encontrado.")
    
except Exception as e:
    print(f"Ocorreu um erro insperao: {e}")
    
def ler_arquivo(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return f.read()
        
    except FileNotFoundError:  
        print("erro:arquivo nao existe.")
        
    except Exception as e:
        print(f"erro ao ler arquivo:{e}")
        
    return None