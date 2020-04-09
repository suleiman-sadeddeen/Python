#!/usr/bin/python3

#address;private;network;broadcast;netmask;hosts;ipv6;bin

#def datei_einlesen(Datei):
#    ipliste = []
    firstline = True
    # einlesen der Daten aus einer CSV Datei
    with open(Datei, 'r') as fh:
        for line in fh.readlines():
            if firstline is True:
                firstline = False
                continue
            items = line.split(';')
#            print(items)
            pattern = item[0]
            ersteaddress = pattern.split('.')
#            print(ersteaddress)

            length = 0
            for i in ersteaddress:
                length = length + 1
            if length == 4:
                print(f'Treffer ok: {ersteaddress}')
            else:
                print(pattern)
                print('WEG DAMIT')

ipliste = datei_einlesen('/home/ss/bin/network_stuff.csv')

