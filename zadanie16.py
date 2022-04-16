import random
b = []
c = 0
d = []
for i in range(20):
    a = random.randint(0, 10)
    b.append(a)

for i in range(20):
    if b[-1] == 3:
        print("false")
        exit() 
    else:
        d.append(b[-1])
        b.remove(b[-1])

for i in range(20):
    if d[-1] == 1:
        print("true")
        exit()
    else:
        b.append(d[-1])
        d.remove(d[-1])

print("false")