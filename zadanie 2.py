import random
lista = []

for i in range(20):
    a = random.randint(1,10)
    
    lista.append(a)
b = max(lista)
print(lista)
print(b)