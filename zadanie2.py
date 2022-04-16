

def kelwin():
    a = float(input("Podaj temperatuję w kelvinach: "))
    b = a - 273.15
    if a - 273.15 < 0:
        print("none")
    else:  
        print("Jest", a - 273.15, "stopni celcjusza")
    def farenhit():
        c = b * 1.8
        d = c + 32
        print(d)
        
    farenhit()



kelwin()

