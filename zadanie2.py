liczby = []
a = 0
for i in range(200):
    b = 0
    for i in range(len(str(a))):
        
        if str(a)[b] == "6":
            liczby.append(a)
            b += 1
        else:
            b += 1
    a += 1

print(liczby)
