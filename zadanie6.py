import random
a = []
b = []
c = []
d = int(input("Podaj liczbę: "))
a.append(random.randint(0,d))
b.append(random.randint(0,d))
e = a[-1] + b[-1]
c.append(e)
print(e)