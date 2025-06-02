numeros_inteiros = (1, 2, 3, 2, 4, 2)
print(numeros_inteiros.count(2))

t1 = (10, 20, 30)
print(len(t1)) # |Saída:3

t2 = (10, 20, 30)

print(max(t2))

print(min(t2))

t3 = (1, 2, 3, 4)

print(sum(t3))

t4 = (3, 1, 2)

print(sorted(t4))

lista = [1, 2, 3]

t5 = tuple(lista)

print(t5)

t6 = ('a', 'b', 'c')

print('b' in t6)

t7 = ('a', 'b', 'c')

for i, v in enumerate(t7):
    
    print(i, v)
    
    tarefas = ['acordar', 'estudar', 'trabalhar']
    
    tarefas.append('fazer exercicios')
    tarefas.remove('acordar')
    
    print(tarefas)
    
    
    leituras = []
    
    for _ in range(5):
        leitura = float(input('digite a leiura do sensor; '))
        leitura.append(leitura)
        
        media = sum(leitura) / len(leitura)
        print(f"media das leituras: {media:.2f}")