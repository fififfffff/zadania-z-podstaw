import random
b = []
for i in range(20):
    a = random.randint(0, 10)
    b.append(a)
c = max(b) - min(b)

print(b)
print("Róznica pomiędzy największą i najmniejszą liczbą wynosi:", c)
