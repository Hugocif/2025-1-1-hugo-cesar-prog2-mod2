from datetime import datetime
from datetime import date
from datetime import time


"""Pytz é uma biblioteca do Python que permite calcular fusos horários e
resolver problemas com horários ambíguos no final do horário de verão.

O tzdata é um “pacote” de dados do Python que fornece dados de fuso
horário IANA. Ele é principalmente usado pelo módulo “zoneinfo” da
biblioteca padrão, mas também pode ser usado como fonte de dados de fuso
horário para outras bibliotecas de fuso horário.;
Salve, faça commit e push."""

#QUESTÃO 2:

"""data_atual = datetime.now()
hora_atual = data_atual.strftime("%d%n%Y- %H:%M:%S")

print("Horario atual:", hora_atual)"""

#QUESTÃO 3:

"""dia_atual = datetime.today()
dia_atualmente = dia_atual.strftime("%d%n%Y")

print("|Dia de hoje: ", dia_atualmente)"""

#QUESTÃO 4:

"""horario = time(14, 30, 50)

print(horario.hour, ':', horario.minute, ':', horario.second)
print('horario: ', horario.strftime('%H:$H:%S'))"""

#QUESTÃO 5:

