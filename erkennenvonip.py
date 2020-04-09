#!/usr/bin/python3

address;private;network;broadcast;netmask;hosts;ipv6;bin

def datei_einlesen(Datei):
    _ipliste = []
    firstline = True
    # einlesen der Daten aus einer CSV Datei
    with open(Datei, 'r') as fh:
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
            bigiplist = {'Address': address, 'Preis': preis, 'Gewicht': gewicht, 'Anzahl': anzahl}
            _ipliste.append(bigiplist)
    return _ipliste

ipliste = datei_einlesen('/home/ss/bin/network_stuff.csv')

