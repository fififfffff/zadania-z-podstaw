import random
b = []
c = 0

e = int(input("Podaj ilość elementów listy, minimum to 4: "))
for i in range(e):
    a = random.randint(0, 10)
    b.append(a)
b.remove(min(b))
b.remove(max(b))

for i in range(e - 2):
    
    c += b[-1]
    b.remove(b[-1])


f = e - 2
g = c/f
print("Średnia to:", g)
    