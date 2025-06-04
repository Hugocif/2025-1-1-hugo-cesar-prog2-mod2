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
        
        #Métodos das listas em python: append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy.
        
        d = {'a': 1, 'b': 2, 'c': 3}
        d.clear()
        print(d) #Saída
        
        d1 = {'a': 1, 'b': 2}
        d2 = d1.copy()
        print(d2) #Saída: {'a': 1, 'b': 2}
        
        keys = {'a', 'b', 'c'}
        d3 = dict.fromkeys(keys, 0)
        print(d3) 
        
        d4 = {'a': 1}
        print(d.get('a'))
        print(d.get('b', 0))
        
        d5 = {'a': 1, 'b': 2}
        for k,v in d.itens():
            print(k,v)
            
            d6 =