
#                                                                                                 Miłego sprawdzania :)

import time
from datetime import date
lata = []
def rok_prze():
    a = 4
    for i in range(200):
        lata.append(2096 - a)
        a += 4
rok_prze()

def ilość_dni(a, b, c):
    mon = b 

    czas = time.localtime()
    dni_dodac = 0
    rok = a
    for i in range(czas.tm_year - a):
        d = 0
        for i in range(201):
            if a == lata[d]:
                d += 1
                dni_dodac += 1
            else:
                d += 1
        a += 1
    miesioc = 0
    miesioce = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    e = 0
    for i in range(201):
        if rok == lata[e]:
            e += 1
            miesioc += 1
        else:
            e += 1
    if miesioc > 0:
        miesioce[1] = 29
    else:
        miesioce[1] = 28
    for i in range(1):    
        d = 0
        for i in range(b - 1):
            miesioce[d] = 0
            d += 1
    miesioce[b - 1] = c
    f = 0
    for i in range(12):
        f += miesioce[-1]
        miesioce.remove(miesioce[-1])
    czas2 = czas.tm_year
    
    lat = czas2 - rok
    
    if lat == 0:
        lat = 1
    else:
        lat = lat
    dni = 365 * lat - 365 + f
    miesioce2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    z = 11
    
    for i in range(12 - czas.tm_mon):
        miesioce2[z] = 0
        z -= 1
    x = 0
    y = 0
    miesioce2[czas.tm_mon - 1] = czas.tm_mday
    for i in range(12):
        y += miesioce2[x]
        x += 1
    
    if mon == 1:
        dni -= 15
    elif mon == 2:
        dni -= 12
    elif mon == 3:
        dni -= 15
    elif mon == 4:
        dni -= 14
    elif mon == 5:
        dni -= 15
    elif mon == 6:
        dni -= 14
    elif mon == 7:
        dni -= 15
    elif mon == 8:
        dni -= 15
    elif mon == 9:
        dni -= 14
    elif mon == 10:
        dni -= 15
    elif mon == 11:
        dni -= 16
    elif mon == 12:
        dni -= 15
    dni2 = dni + dni_dodac + y
    if dni2 < 372:
        print("JESTEŚ ZA MŁODY, IDŹ DO ŻŁOBKA. Ale żyjesz już", dni2, "dni.")
    else:
        print("Żyjesz już", dni2, "dni.")

        


    


rok_prze()

ilość_dni(a = int(input("Podaj rok urodzenia: ")), b = int(input("Podaj miesiąc urodzenia: ")), c = int(input("Podaj dzień urodzenia: ")))



