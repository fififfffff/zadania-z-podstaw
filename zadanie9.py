import random
f=[]
g = 0
b = 0
for i in range(20):
   a = random.randint(0, 10)
   f.append(a)
f.sort()

for i in range(20):
    if f[i-1] == f[i]:
        b = b + 1
    else:
        b = 0
    if g < b:
        g = b
    
g += 1
print("najwiekrza ilosc powtorzen to:", g)