import csv

LICZBA_CECH_W_PLIKU = 4

slowik = {}

ilePol = 0
currentListName = 'nun'
with open('drg.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        for field in row:
            if ilePol > 0:
                slowik[currentListName].append(field)
                ilePol = ilePol - 1
            if field.startswith('\"Powiat'):
                currentListName = field
                ilePol = LICZBA_CECH_W_PLIKU
                if currentListName in slowik:
                    print('e')
                else:
                    slowik[currentListName] = []


LICZBA_CECH_W_PLIKU = 1

ilePol = 0
currentListName = 'nun'
with open('moni.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        for field in row:
            if ilePol > 0:
                slowik[currentListName].append(field)
                ilePol = ilePol - 1
            if field.startswith('\"Powiat'):
                currentListName = field
                ilePol = LICZBA_CECH_W_PLIKU
                if currentListName in slowik:
                    print('e')
                else:
                    slowik[currentListName] = []

print(slowik)