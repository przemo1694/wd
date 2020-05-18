n = int(input("Podaj ilość liczb: "))

liczby = []

i = 0
while i < n:
    print("[",i,"]:" ,end='')
    liczby.append(input())
    i+=1

i = 0
while i < n:
    print(str(liczby[i]),",",end='')
    i+=1