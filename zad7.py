n = int(input("Podaj ilość liczb: "))

liczby = []

for i in range(1 , n+1, 1):
    print("[",i,"]:" ,end='')
    liczby.append(input())

for i in range(0 , n, 1):
    l = int(liczby[i]) ** 2
    print(str(liczby[i]),"^2 =",str(l))