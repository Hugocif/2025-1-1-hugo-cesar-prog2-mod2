"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

def data_menos_data(data_final, data_inicial):
    
        data_entre = relativedelta(data_final, data_inicial)

        return data_entre



# Função para converter string para data
def ler_data(prompt):
    entrada = input(prompt)
    return datetime.strptime(entrada, "%d/%m/%Y").date()

# Lê as datas no formato dia/mês/ano
data_inicial = ler_data("Digite a data inicial (dd/mm/aaaa): ")
data_final = ler_data("Digite a data final (dd/mm/aaaa): ")

# Calcula a diferença detalhada
diferenca = data_menos_data(data_final, data_inicial)

# Mostra o resultado
print(f"\nDiferença: {diferenca.years} anos, {diferenca.months} meses, {diferenca.days} dias")
"""
def é_numerico(variavel):

    if (variavel.strip().isnumeric()):
        
        return True
    
    else:
    
        return False
    
def tupla_print(tupla, indice):
      
      print(tupla[indice])

materias_do_tecnico = 'Matematica', 'Portugues', 'Programação', 'Quimica', 'Artes', 'Educação fisica', 'Filosofia', 'Arquitetura de computadores e redes', 'Historia', 'Sociologia'

print(materias_do_tecnico)

escolha_do_indice = input("escolha o que você quer escrever(entre 0 e 9): ")

if é_numerico(escolha_do_indice):
                                
        numero_do_usuario = int(escolha_do_indice)

        if numero_do_usuario < 10 and numero_do_usuario >= 0:

                tupla_print(materias_do_tecnico, numero_do_usuario)

        else:
              print("O elemento não existe")