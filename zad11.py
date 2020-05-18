n = 0

while n<3 or n>9:
    n = int(input("napisz wysokość od 1 do 10: "))

    if n<3 or n>9:
        print("To nie jest liczba od 1 do 10")

i = 0
ip = int(n/2)+1

for y in range (0,n,1):

    if(y < (n/2)):
        i+=1
        ip-=1
    else:
        i-=1
        ip+=1


    for a in range (0,ip,1):
        print(" ",end='')

    for b in range (1,(i*2),1):
        print("o",end='')
        
    print("")