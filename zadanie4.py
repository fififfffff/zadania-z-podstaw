import random
lista = []

for i in range(20):
    a = random.randint(1,10)
    
    lista.append(a)


for i in range(2):
    b = min(lista)
    
    print(b)
    lista.remove(b)
