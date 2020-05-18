n = int(input("Podaj ilość liczb do przeszukania: "))

for i in range(1 , n, 1):
    if(i % 5 == 0):
        print(i , ",",end='')
