import random
b = []

d = 0
for i in range(20):
    a = int(input("Podaj liczbę: "))
    b.append(a)
    d += b[-1] 
    

print("Suma tych liczb to:",d)