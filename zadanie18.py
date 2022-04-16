import random
b = []
cztery = 0
jeden = 0
d = []
for i in range(20):
    a = random.randint(1,4)
    b.append(a)

for i in range(20):
    if b[-1] == 4:
        cztery += 1
        d.append(b[-1])
        b.remove(b[-1])
    else:
        d.append(b[-1])
        b.remove(b[-1])


for i in range(20):
    if d[-1] == 1:
        jeden += 1
        b.append(d[-1])
        d.remove(d[-1])
    else:
        b.append(d[-1])
        d.remove(d[-1])
if jeden <= cztery:
    print("false")
else:
    print("true")
    
    