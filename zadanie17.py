import random
b = []
c = 0
d = []
for i in range(20):
    a = random.randint(0, 10)
    b.append(a)
for i in range(20):
    if b[-1] == 2:
        c += 2
        
    else:
        b.remove(b[-1])
if c == 8:
    print("true")
else:
    print("false")