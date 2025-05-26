# #Q3



# while True:
#     frase = input("\nDigite uma frase ou digite 'sair' para encerrar: ").strip()
    
#     if frase.lower() in ['sair', 'exit', 'fechar', 'encerrar', 'quit', '4']:
#         print("Programa encerrado.")
#         break

#     while True:
#         print("\nMenu de opções:")
#         print("1 - Contar as vogais")
#         print("2 - Verificar se é numérica")
#         print("3 - Inverter a frase")
#         print("4 - Sair")

#         escolha = input("Escolha uma opção: ").strip().lower()

#         if escolha == '1':
#             vogais = 0
#             for letra in frase:
#                 if letra.lower() in 'aeiou':
#                     vogais += 1
#             print("Número de vogais:", vogais)

#         elif escolha == '2':
#             if frase.isnumeric():
#                 print("A frase é numérica.")
#             else:
#                 print("A frase não é numérica.")

#         elif escolha == '3':
#             invertida = frase[::-1]
#             print("Frase invertida:", invertida)

#         elif escolha in ['4', 'sair', 'exit', 'fechar', 'encerrar', 'quit']:
#             print("Encerrar programa...")
#             exit()

#         else:
#             print("Opção inválida. Tente novamente.")



# import re

# def verificar_formato_cpf(cpf):
#     padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    
#     if re.match(padrao, cpf):
#         return True
#     else:
#         return False

# cpf_usuario = input("Digite o CPF no formato 000.000.000-00: ")

# if verificar_formato_cpf(cpf_usuario):
#     print("CPF está no formato correto.")
# else:
#     print("CPF está em formato incorreto. Use: 000.000.000-00")




# def validar_senha(senha):
#     if len(senha) < 6:
#         print("A senha deve ter no mínimo 6 caracteres.")
#         return

#     if len(senha) > 20:
#         print("A senha deve ter no máximo 20 caracteres.")
#         return

#     if not any(c.isupper() for c in senha):
#         print("A senha deve conter pelo menos uma letra maiúscula.")
#         return

#     if not any(c.islower() for c in senha):
#         print("A senha deve conter pelo menos uma letra minúscula.")
#         return
    
#     especiais_permitidos = "$#@!&"
#     if not any(c in especiais_permitidos for c in senha):
#         print("A senha deve conter pelo menos um dos seguintes caracteres especiais: $#@!&")
#         return

#     for c in senha:
#         if c.isspace():
#             print("A senha não pode conter espaços em branco ou tabulações.")
#             return
#         elif not (c.isalnum() or c in especiais_permitidos):
#             print(f"Caractere inválido encontrado: '{c}'. Use apenas letras, números ou os caracteres: $#@!&")
#             return

#     print("Senha válida!")

# senha = input("Digite sua senha: ")
# validar_senha(senha)


def contar_pares_e_impares(numero):
    pares = 0
    impares = 0

    for i in range(1, numero + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"\nNo intervalo de 1 até {numero}:")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

try:
    valor = int(input("Digite um número inteiro maior que zero: "))
    if valor <= 0:
        print("O número deve ser maior que zero.")
    else:
        contar_pares_e_impares(valor)
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")