#!/usr/bin/python3


with open('/home/tn/bin/einkaufliste.csv', 'r') as fh:
    content = fh.read()
    
print(content)

print('---')
einkaufliste = []
counter = 1
firstline = True
with open('/home/tn/bin/einkaufliste.csv', 'r') as fh:
    for line in fh.readlines():
        if firstline is True:
            firstline = False
            continue
#        print(line)
##########################################
#        name = ..
#        preis = ..
        items = line.split(',')
        name = items[0][1:]
        name = name[:-1]
        preis = int(items[1])
        gewicht = int(items[2])
        anzahl = items[3]
        anzahl = int(anzahl[:-1])
#        print(items)
##########################################
#        print(f'Produkt Name: -{name}-')
#        print(f'Preis: -{preis}-')
#        print(f'Gewicht: -{gewicht}-')
#        print(f'Anzahl: -{anzahl}-')
#        print(gewicht * 3)

        nahrungsmittel = {'name': name, 'preis': preis, 'gewicht': gewicht, 'anzahl': anzahl}

        einkaufliste.append(nahrungsmittel)

        counter = counter + 1
# 'Milch',1,1000,4
print(einkaufliste)


