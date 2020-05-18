import math

l = -1

while(l < 0):
    l = int(input("Podaj liczbę:"))
    if (l < 0):
        print("Liczba nie może być ujemna")

print (str(math.sqrt(l)))
