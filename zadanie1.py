import time
from datetime import date

def wiek():
    rok = time.localtime()
    a = input("Podaj imię: ")
    b = int(input("Podaj rok urodzenia: "))
    print(a, rok.tm_year - b, "lat")
wiek()