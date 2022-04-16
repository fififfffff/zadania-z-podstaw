import random
b = []
c = 0
d = [0]
for i in range(20):
    a = random.randint(0, 10)
    b.append(a)
for i in range(20):
    if d[-1] == 2 and b[-1] == 2:
        print("true")  
        
        exit()    
          
    else:
        
        d.append(b[-1])
        b.remove(b[-1])
print("false")