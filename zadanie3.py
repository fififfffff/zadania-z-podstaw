import random
lista = []
c = 0
for i in range(20):
    a = random.randint(1,10)
    lista.append(a)
    print(a)
for b in lista:
    if a % 2 != 0:
        c += b
    else:
        continue
        



print(c)