import random
macierz = [random.sample(range(1, 101), 4) for _ in range(4)]
for wiersz in macierz:
     print(wiersz)

print(macierz)
# przekątna
przekatna = []
for i in range(len(macierz)):
    przekatna.append(macierz[i][i])
print(przekatna)