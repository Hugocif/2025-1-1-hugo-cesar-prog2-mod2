#Q1:    

from pathlib import Path

arquivo_txt = ""
arquivo_csv = ""

def ler_arquivo(arquiuvo_caminho_completo_extenso):
    try:
        with open(arquiuvo_caminho_completo_extenso, "r") as arquivo:
            conteudo_do_arquivo = arquivo.readline()
            print("conteudo do arquuivo: ")
            print(conteudo_do_arquivo)
            
    except FileNotFoundError:
        print(f"oarquivo \"{arquiuvo_caminho_completo_extenso}\" nao foi encontrado")

    except Exception as error:
        print(f"oarquivo \"{arquiuvo_caminho_completo_extenso}\" nao foi encontrado")
        
arquivo_txt = str(Path.cwd()) + r"/Manipulacao_arquivos/arquivos_txt/indices_tabelas.txt"

print("diretório de trabalho: ", arquivo_txt)

ler_arquivo(arquivo_txt)
        

























