def podatki():
    a = int(input("Podaj przychód: "))
    b = int(input("Podaj podatki w procentach: "))
    d = a * b
    c = d / 100
    print("Twój dochód to", a - c )
podatki()
