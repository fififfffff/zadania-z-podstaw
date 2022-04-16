import random

b = []
c = [0]
d = []
f = []
for i in range(30):
    e = random.randint(0,10)
    
    b.append(e)
    
    if b[-1] == c[-1]:
        
        d.append(b[-1])
            
    else:
        c.append(b[-1])
    f.append(b[-1])
        

print(d)    
print(d)
print("pary - góra, dół")  
        
    