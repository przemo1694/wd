n = 0

while n<1 or n>10:
    n = int(input("napisz wysokość od 1 do 10: "))

    if n<1 or n>10:
        print("To nie jest liczba od 1 do 10")

for y in range (1,n+1,1):
    for x in range (0,y,1):
        print("A",end='')
    print("")