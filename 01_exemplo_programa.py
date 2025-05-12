#importação da função sleep da biblioteca time
from time import sleep


menu = '''\nMenu de Opções:
            1- Cadastrar evento
            2- Excluir evento
            3- Cadastrar aluno
            4- excluir aluno
            5- Matricular aluno
            6- Desmatricular aluno
            7- Ver eventos cadastrados
            8- Ver alunos cadastrados
            9- Ver alunos matriculados
            10- Resumo SNCT
            
            Sair - digite SAIR\n'''

evento    = {} #keys: titulo, capacidade, vagas_restantes
aluno     = {} #keys: nome, curso, instituição
matricula = {} #keys: evento_nome, evento_aluno


ventos_cadastrados = [] #manipula evento
alunos_cadastrados  = [] #manipula aluno
alunos_matriculados = [] #manipula inscrição de alunos em eventos já pré cadastrados


def codigo_principal():
    escolhaDoMenu = ''
    while escolhaDoMenu != 'sair':
        print(exibir_menu(menu))
        escolhaDoMenu = str(input('Digite sua escolha: ')).strip().lower()
        if escolhaDoMenu == 'sair':
            break
        else:
            print(escolha_do_menu(escolhaDoMenu))
    print('Saiu. Obrigado!')
    resumo(alunos_cadastrados, eventos_cadastrados, alunos_matriculados)

def exibir_matriculados(lista_matriculados):
    if len(alunos_matriculados) > 0:  
        for dicionario in lista_matriculados:
            print(dicionario)
    else:
        return 'Não há nenhum aluno matriculado.'
    
def exibir_eventos(listaDeEventos):
    if len(eventos_cadastrados) > 0:    
        for dicionario in listaDeEventos:
            print(dicionario)
    else:
        return 'Não há nenhum evento cadastrado.'
    
def exibir_menu(menuDeOpcoes):
    return menuDeOpcoes

def exibir_alunos(listaDeAlunos):
    if len(alunos_cadastrados) > 0:
        for dicionario in listaDeAlunos:
            print(dicionario)
    else:
        return 'Não há nenhum aluno cadastrado.'
    
def cadastrar_aluno():
    nome   = input('\nDIGITE O NOME DO ALUNO: ').strip().title()
    if contem_aluno(alunos_cadastrados, nome) == True:
        return 'ALUNO JÁ CADASTRADO.'
    else:
        modulo = input('DIGITE SEU MÓDULO: ').strip()
        if verificacao_int(modulo) == True:
            return 'ENTRADA  INVÁLIDA.'
        else:
            curso = input('INFORME SEU CURSO: ').strip().upper()     
            aluno = {'nome_aluno': nome,
                     'modulo': modulo,
                     'curso': curso}
            alunos_cadastrados.append(aluno)
            exibir_alunos(alunos_cadastrados)
            return '\nALUNO CADASTRADO COM SUCESSO!\n'  
    
def contem_aluno(lista_aluno, nomeInformado):
    if not len(lista_aluno) == 0:
        for dicionario in lista_aluno:
            if dicionario.get('nome_aluno') == nomeInformado:
                return True
        return False
    else:
        return False

def excluir_aluno():
    if len(alunos_cadastrados) > 0:
        exibir_alunos(alunos_cadastrados)
        nomeAluno = input('\nDIGITE O NOME DO ALUNO QUE DESEJA EXCLUIR: ').strip().title()

        for indice in range(len(alunos_cadastrados)):
            if alunos_cadastrados[indice].get('nome_aluno') == nomeAluno:
                alunos_cadastrados.remove(alunos_cadastrados[indice])
                for indice in range(len(alunos_matriculados)):
                    if alunos_matriculados[indice].get('nome_aluno') == nomeAluno: 
                        eventoMatriculado = eventos_cadastrados[indice].get('evento')
                        alunos_matriculados.remove(alunos_matriculados[indice])
                        aumentando_vaga(eventoMatriculado)
                print('\nexcluindo aluno...')
                sleep(3)
                exibir_alunos(alunos_cadastrados)
                return '\Aluno excluído com sucesso!\n'
        return '\nO aluno não foi encontrado. Cadastre o aluno primeiro\nou verifique se o nome está escrito corretamente.\n'

    else:
        return 'Ainda não foi cadastrado nenhum aluno.'

def contem_evento(listaEventos, item):
    if not len(listaEventos) == 0:
        for dicionario in listaEventos:
            if dicionario.get('titulo_evento') == item:
                return True
        return False
    else:
        return False
    
def verificacao_int(numero):
    if not numero.isdigit() == True:
        return True
    else:
        numero = int(numero)
        return False

def cadastrar_evento():
    titulo          = input('\nDIGITE O NOME DO EVENTO: ').title().strip()
    capacidade      = input('DIGITE A CAPACIDADE MÁXIMA DO EVENTO: ').strip()

    if verificacao_int(capacidade) == True:
        print('ENTRADA  INVÁLIDA.')
    else:
        capacidade = int(capacidade)
        vagas_restantes = capacidade

        evento = {}

        if contem_evento(eventos_cadastrados, titulo) == True:
            return "\nEVENTO JÁ EXISTE."
        else:
            print('\nEVENTO CADASTRADO COM SUCESSO!\n')
            evento = {'titulo_evento':   titulo,
                    'capacidade':      capacidade,
                    'vagas_restantes': vagas_restantes}      
            eventos_cadastrados.append(evento)
            return exibir_eventos(eventos_cadastrados)

def excluir_evento(Eventos):
  
    if not len(Eventos) == 0:
        exibir_eventos(eventos_cadastrados)
        nomeEvento = input('\nInforme o nome do evento: ').strip().title()

        for dicionario in Eventos:
            if dicionario.get('titulo_evento') == nomeEvento:
                Eventos.remove(dicionario)
                print('\nDesmatriculando alunos do evento...')
                sleep(1)
                print('\nexcluindo evento...')
                sleep(3)
                exibir_eventos(eventos_cadastrados)
                return '\nEvento excluído com sucesso!\n'
        return '\nO evento não foi encontrado. Cadastre o evento primeiro\nou verifique se o nome está escrito corretamente.\n'
    else:
        return 'Ainda não existe nenhum evento.'

def matricular_aluno():
    if len(alunos_cadastrados) > 0:
        exibir_alunos(alunos_cadastrados)
        nome = input('DIGITE O NOME DO ALUNO QUE SERÁ MATRICULADO: ').strip().title()
        if contem_aluno(alunos_cadastrados, nome) == False:
            return '\nO aluno não foi encontrado. Cadastre o aluno primeiro\nou verifique se o nome está escrito corretamente.\n'
        else:
            exibir_eventos(eventos_cadastrados)
            inscreverNoEvento = input('\nINFORME O EVENTO OQUE O ALUNO SERÁ MATRICULADO: ').strip().title()
            if contem_evento(eventos_cadastrados, inscreverNoEvento) == False:
                return '\nO evento não foi encontrado. Cadastre o evento primeiro\nou verifique se o nome está escrito corretamente.\n'
            else:
                matricula = {'nome_aluno': nome,
                            'evento': inscreverNoEvento}
                alunos_matriculados.append(matricula)
                reduzir_vaga(inscreverNoEvento)
                exibir_matriculados(alunos_matriculados)
                return 'Aluno matriculado no evento com sucesso!'
    else:
        return 'Não há alunos cadastrados'
    
def desmatricular_aluno():
    if len(alunos_matriculados) > 0: 
        exibir_alunos(alunos_matriculados)
        nome = input('DIGITE O NOME DO ALUNO QUE SERÁ DESMATRICULADO: ').strip().title()
        if contem_aluno(alunos_matriculados, nome) == False:
            return '\nO aluno não foi encontrado. Matricule o aluno primeiro\nou verifique se o nome está escrito corretamente.\n'
        else:
            for indice in range(len(alunos_matriculados)):
                if alunos_matriculados[indice].get('nome_aluno') == nome:
                    eventoMatriculado = eventos_cadastrados[indice].get('evento')
                    alunos_matriculados.remove(alunos_matriculados[indice])
                    aumentando_vaga(eventoMatriculado)
                    exibir_matriculados(alunos_matriculados)
                    return 'Aluno desmatriculado com sucesso!'
    else:
        return 'Não existem alunos matriculados.'

def reduzir_vaga(nomeEvento):
    msg = ''

    if len(eventos_cadastrados) > 0:
        for indice in range(len(eventos_cadastrados)):
            if eventos_cadastrados[indice].get('titulo_evento') == nomeEvento:
                vagasRestantesEvento = eventos_cadastrados[indice].get('vagas_restantes') -1
                if vagasRestantesEvento >= 0:
                    eventos_cadastrados[indice].update({'vagas_restantes': vagasRestantesEvento})
                    msg = 'O evento ' + eventos_cadastrados[indice].get('titulo_evento') + ' foi atualizado com sucesso!'
                else:
                    msg = 'Não há mais vagas disponíveis neste curso'
    else:
        msg = 'Não existem eventos cadastrados.'

    return msg

def aumentando_vaga(nomeEvento):
    msg = ''

    if len(eventos_cadastrados) > 0:
        for indice in range(len(eventos_cadastrados)):
            if eventos_cadastrados[indice].get('titulo_evento') == nomeEvento:
                vagasRestantesEvento = eventos_cadastrados[indice].get('vagas_restantes') +1
                vagasMaximasEvento = eventos_cadastrados[indice].get('capacidade_maxima')
                if vagasRestantesEvento <= vagasMaximasEvento:
                    eventos_cadastrados[indice].update({'vagas_restantes': vagasRestantesEvento})
                    msg = 'O evento ' + eventos_cadastrados[indice].get('titulo_evento') + ' foi atualizado com sucesso!'
                else:
                    msg = 'Erro! O evento ganhou mais vagas que sua capacidade maxima!'
    else:
        msg = 'Não existem eventos cadastrados.'

    return msg

def escolha_do_menu(escolha):
    if escolha == '1':
        return cadastrar_evento()
    
    elif escolha == '2':
        return excluir_evento(eventos_cadastrados)
    
    elif escolha == '3':
        return cadastrar_aluno()
    
    elif escolha == '4':
        return excluir_aluno()
    
    elif escolha == '5':
        return matricular_aluno()
    
    elif escolha == '6':
        return desmatricular_aluno()
    
    elif escolha == '7':
        return exibir_eventos(eventos_cadastrados)
    
    elif escolha == '8':
        return exibir_alunos(alunos_cadastrados)
    
    elif escolha == '9':
        return exibir_matriculados(alunos_matriculados)
    
    elif escolha == '10':
        return resumo(alunos_cadastrados, eventos_cadastrados, alunos_matriculados)
    
    else:
        return 'ENTRADA INVÁLIDA.'

def resumo(lista_alunos, lista_eventos, lista_cadastrados):
    print('\n\nLISTA DE ALUNOS CADASTRADOS:\n')
    exibir_alunos(lista_alunos)
    print('\nLISTA DE EVENTOS CADASTRADOS:\n')
    exibir_eventos(lista_eventos)
    print('\nLISTA DE MATRICULADOS:\n')
    exibir_matriculados(lista_cadastrados)    

codigo_principal()