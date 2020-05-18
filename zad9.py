
suma = 0

napis = ""

while not napis.isdigit():
    napis = input("napisz liczbę wielocyfrową: ")

    if not napis.isdigit():
        print("To nie jest liczba")

for i in range (0,len(napis),1):
    suma += int(napis[i])

print (suma)