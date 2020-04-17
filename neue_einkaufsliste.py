#!/usr/bin/python3
# -*- coding: utf-8 -*-

import lib.Product as p

# schreiben Sie ein Klasse mit der Sie neue Produkte anlegen können
# Die Eigenschaften des Produktes sollen direkt beim instanzieren uebergeben werden
# es soll eine Methode geben mit der sich bestehende Eigenschaften verändern lassen
# 


def read_file():
    file = '/home/tn/bin/einkaufliste.csv'
    einkaufsliste = []
    firstline = True
    with open(file, 'r') as fh:
        for line in fh.readlines():
            if firstline is True:
                firstline = False
                continue
            items = line.split(',')
            name = items[0][1:]
            name = name[:-1]
            preis = int(items[1])
            gewicht = int(items[2])
            anzahl = items[3]
            anzahl = int(anzahl[:-1])
            produkt = p.Product({'Name': name, 'Preis': preis, 'Gewicht': gewicht, 'Anzahl': anzahl})
            einkaufsliste.append(produkt)
        return einkaufsliste

var = read_file()

for item in var:
    print(item)
#    item.show_me()
#print(var)



#birne = Product({'Name': 'Birne', 'Gewicht': 500, 'Preis': 2, 'Farbe': 'gruen'})
#birne.set_attribute('Preis', 1)
#print(birne.get_attribute())
#birne.set_attribute('Preis', 3)
#birne.set_attribute('Farbe', 'braun')
#print(birne.get_attribute())

#birne.show_me()
