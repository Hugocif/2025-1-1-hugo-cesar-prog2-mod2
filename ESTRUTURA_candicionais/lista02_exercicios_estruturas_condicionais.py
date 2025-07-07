from datetime import date
import datetime
import uuid

#resposta da 1

numero_digitado_pelo_usuario = input("Escreva um número: ")
numero_digitado_pelo_usuario2 = input("Escreva um número: ")
if(numero_digitado_pelo_usuario and numero_digitado_pelo_usuario2.strip().isnumeric()):
    print("É valido")
    numero_digitado_pelo_usuario2 = float(numero_digitado_pelo_usuario2)
    numero_digitado_pelo_usuario = float(numero_digitado_pelo_usuario)

    numero_derivado_da_conta = numero_digitado_pelo_usuario2 + numero_digitado_pelo_usuario
    print(f"{numero_digitado_pelo_usuario2} + {numero_digitado_pelo_usuario} = {numero_derivado_da_conta}")
    
    numero_derivado_da_conta = numero_digitado_pelo_usuario2 * numero_digitado_pelo_usuario
    print(f"{numero_digitado_pelo_usuario2} * {numero_digitado_pelo_usuario} = {numero_derivado_da_conta}")
    
    numero_derivado_da_conta = numero_digitado_pelo_usuario2 / numero_digitado_pelo_usuario
    print(f"{numero_digitado_pelo_usuario2} / {numero_digitado_pelo_usuario} = {numero_derivado_da_conta}")
    
    numero_derivado_da_conta = numero_digitado_pelo_usuario2 - numero_digitado_pelo_usuario
    print(f"{numero_digitado_pelo_usuario2} - {numero_digitado_pelo_usuario} = {numero_derivado_da_conta}")
#resposta da 2

frase =  "Bem vindo turma da Programação II ao mundo da programação Python!!!"
frase = frase[::-1]
print(f"{frase}")
#resposta da 3


tamanho_da_senha = int(input("digite quantos caracteres sua senha deve ter: "))

if tamanho_da_senha <= 0:
    print("Digite um numero maior que 0")
if tamanho_da_senha > 128:
    print("Digite uma quantidade menor")
if tamanho_da_senha < 128:
    print("Digite uma quantidade menor")
    
uuid = str(uuid.uuid4()).replace("-", "")
senha = uuid[:tamanho_da_senha]
print(f"Sua senha gerada é: {senha}")

#4

data_atual = date.today()
print(data_atual)
print(datetime.datetime.now(). strftime("%H:%M:%S"))