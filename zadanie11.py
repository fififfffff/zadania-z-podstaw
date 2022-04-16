import random
b = []
c = 0
d = []
for i in range(20):
    a = random.randint(0, 10)
    b.append(a)
for i in range(20):
    if b[-1] % 2 == 0:
        c += 1
        d.append(b[-1])
        b.remove(b[-1])
    else:
        d.append(b[-1])
        b.remove(b[-1])
print(d)
print("Liczby parzyste wystąpiły:", c, "razy")