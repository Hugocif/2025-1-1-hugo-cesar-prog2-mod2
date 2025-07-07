#resposta da 4
while True:
    
    numero_digitado_pelo_usuario = input("Digite um número pra descobrirmos se é par ou ímpar: ")
    if not (numero_digitado_pelo_usuario.strip().isnumeric()):
        print("Digito invalido")
        break
    if (int(numero_digitado_pelo_usuario) % 2 == 0):
        print("Seu numero é par")
    if (int(numero_digitado_pelo_usuario) % 2 == 1):
        print("Seu numero é ímpar")
#resposta da 5
    numero_digitado_pelo_usuario = input("Digite um número: ")
    if not (numero_digitado_pelo_usuario.strip().isnumeric()):
        print("Digito invalido")
        break
    if (int(numero_digitado_pelo_usuario) < 0):
            print("Seu numero é negativo")
    if (int(numero_digitado_pelo_usuario) > 0):
            print("Seu numero é positivo")
#resposta da 1
    numero_digitado_pelo_usuario = input("Digite um número: ")
    numero_digitado_pelo_usuario2 = input("Digite um número: ")
    if not (numero_digitado_pelo_usuario and numero_digitado_pelo_usuario2.strip().isnumeric()):
        print("Digito invalido")
        break
    if (int(numero_digitado_pelo_usuario) < int(numero_digitado_pelo_usuario2)):
        print(f"Primeiro digito = {numero_digitado_pelo_usuario}\nSegundo digito = {numero_digitado_pelo_usuario}\n{numero_digitado_pelo_usuario} é  menor que {numero_digitado_pelo_usuario2}")
    if (int(numero_digitado_pelo_usuario) < int(numero_digitado_pelo_usuario2)):
        print(f"{numero_digitado_pelo_usuario} é  maior que {numero_digitado_pelo_usuario2}")
    if (int(numero_digitado_pelo_usuario) < int(numero_digitado_pelo_usuario2)):
        print(f"{numero_digitado_pelo_usuario} é  igual á {numero_digitado_pelo_usuario2}")
#resposta da 2
    print("Que medico gostaria de marcar uma consulta:\n\nJoão Feldmann digite 1.\nDavi Debus digite 2.\nLuiz Fernando digite 3.")
    numero_digitado_pelo_usuario = input("Digite sua escolha: ")
    if not (numero_digitado_pelo_usuario.strip().isnumeric()):
        print("Medico escolhido não existe no sistema")
        break
    if (int(numero_digitado_pelo_usuario)==1):
        print("Joâo Feldmann esta disponivel")
    if (int(numero_digitado_pelo_usuario)==2):
        print("Davi Debus esta disponivel")
    if (int(numero_digitado_pelo_usuario)==3):
        print("Luiz Feldmann esta disponivel")
    else:
        print("Medico escolhido não existe no sistema")
        
#resposta da 6
    print("Irremos calcular seu IMC(índice de massa corporal):")
    
    altura_digitado_pelo_usuario = input("Digite sua altura: ")
    peso_digitado_pelo_usuario = input("Digite seu peso: ")
    if(peso_digitado_pelo_usuario and altura_digitado_pelo_usuario.strip().isnumeric()):
        Indice_Massa_Corporal = float(Indice_Massa_Corporal)   
        Indice_Massa_Corporal = float(peso_digitado_pelo_usuario)/(float(altura_digitado_pelo_usuario)*float(altura_digitado_pelo_usuario))
    if Indice_Massa_Corporal <= 18.5: 
        print("Você esta abaixo do peso")
    if (Indice_Massa_Corporal > 18.5) and (Indice_Massa_Corporal <= 24.9): 
        print("Você esta no peso normal")
    if (Indice_Massa_Corporal > 25) and (Indice_Massa_Corporal <= 29.9): 
        print("Você esta com sobrepeso")
    if Indice_Massa_Corporal > 30: 
        print("Você esta acima do peso")
     
    #resposta da 7
    numero_digitado_pelo_usuario = input("Digite um número para a converção: ")
    if(peso_digitado_pelo_usuario.strip().isnumeric()):
        print("É valido")
    numero_convertido = float(numero_digitado_pelo_usuario)
    print(f"numero digitado por tu: {numero_digitado_pelo_usuario}")
    print(f"numero convertido para: {type(numero_convertido)}")
    
    #resposta da 8
    numero_digitado_pelo_usuario = input("Digite um número: ")
    numero_digitado_pelo_usuario2 = input("Digite um número: ")
    
    if(peso_digitado_pelo_usuario and numero_digitado_pelo_usuario2.strip().isnumeric()):
        print("Não é valido")
    print(f"Esse é seu primeiro número: {float(numero_digitado_pelo_usuario)}\nEsse é seu primeiro número: {float(numero_digitado_pelo_usuario2)}")
    if float(numero_digitado_pelo_usuario) < 150:
        print(f"{numero_digitado_pelo_usuario} é menor do que 150")
    if float(numero_digitado_pelo_usuario) > 150:
        print(f"{numero_digitado_pelo_usuario} é maior do que 150")
    if float(numero_digitado_pelo_usuario2) < 150:
        print(f"{numero_digitado_pelo_usuario2} é menor do que 150")
    if float(numero_digitado_pelo_usuario2) > 150:
        print(f"{numero_digitado_pelo_usuario2} é maior do que 150")
    
    #resposta da 9
    print("Os dias da semana são:\n\nDomingo\nSegunda-Feira\nTerça-Feira\nQUarta-Feira\nQuinta-Feira\nSexta-Feira\nSábado")
    #resposta da 10
    print("Os meses são:\n\nJaneiro\nFevereiro\nMarço\nAbril\nMaio\nJunho\nJulho\nAgosto\nSetenbro\nOutubro\nNovenbro\nDezenbro")