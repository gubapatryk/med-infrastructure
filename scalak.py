import csv
import os

firstIteration = True

slowik = {}

directory = r'./dane'
for filename in os.listdir(directory):
    filepath = directory + '/' + filename

    file = open(filepath)
    content = file.readlines()

    LICZBA_CECH_W_PLIKU = content[1].count(';') - 2

    ilePol = 0
    currentListName = 'nun'
    with open(filepath, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            for field in row:
                if ilePol > 0:
                    slowik[currentListName].append(field)
                    ilePol = ilePol - 1
                if field.startswith('\"Powiat'):
                    currentListName = field
                    ilePol = LICZBA_CECH_W_PLIKU
                    if firstIteration:
                        if not currentListName in slowik:
                            slowik[currentListName] = [currentListName]
    firstIteration = False

#print(slowik)

lista = []
id = 1

for val in slowik.values():
    val.insert(0,id)
    lista.append(val)
    id = id + 1


with open("dane.csv", "w", newline="") as f:
    for i in range(len(lista)):
        for k in range(len(lista[i])):
            f.write(str(lista[i][k]) + ',')
        f.write('\n')


for filename in os.listdir(directory):
    print(filename)