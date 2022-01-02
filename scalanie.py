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
    id_powiatu = 0
    with open(filepath, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            tempList = []
            for field in row:
                tempList.append(field)
            if tempList[1].startswith('\"Powiat'):
                if not tempList[0] in slowik:
                    slowik[tempList[0]] = tempList[1:-1]
                else:
                    ilePol = 2
                    slowik[tempList[0]].extend(tempList[2:-1])

lista = []
id = 1

for val in slowik.values():
    val.insert(0,id)
    lista.append(val)
    id = id + 1


with open("dane.csv", "w", newline="") as f:
    for i in range(len(lista)):
        for k in range(len(lista[i])):
            if k is not (len(lista[i]) - 1):
                f.write(str(lista[i][k]).replace(",",".") + ',')
            else:
                f.write(str(lista[i][k]).replace(",","."))
            
        f.write('\n')