import random

lista = []
lista2 = []

for i in range(20):
    a = random.randint(1,100)
    lista.append(a)

print(lista)

for i in range(20):
    b = min(lista)
    lista2.append(b)
    lista.remove(b)
    

print(lista2)

    