
import random
a=[]
test=[]
slowo = ""
for i in range(20):
    a = random.randint(0, 4)
    a.append(a)
print(a)
for j in range(i+1):
    slowo = slowo + str(a[j])
d_123 = slowo.count("123")
print(slowo)
print("jest",d_123 ,'123')