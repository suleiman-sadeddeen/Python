#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gesucht sind die Netzwerkadresse under Broadcast zu einer Netzmaske
# Wir verwenden die Kurzschreibweise

# 192.168.27.1/24
# { 'netaddress': 192.168.27.0
#   'broadcast' : 192.168.27.255
# }

# 192.168.27.16/25
# 0 - 256 - Das heisst, wir haben 256 Moeglichkeiten
ipranges = {}
ipranges['24'] = [ [0, 255] ]
ipranges['25'] = [ [0, 127], [128, 255] ]
ipranges['26'] = [ [0, 63], [64,127], [128, 191], [192, 255]]

amount_networks = {}
amount_networks['24'] = 1
amount_networks['25'] = 2
amount_networks['26'] = 4
amount_networks['27'] = 8
amount_networks['28'] = 16
amount_networks['29'] = 32
amount_networks['30'] = 64
amount_networks['31'] = 128

# berechnen der Netzwerkadressen und der Broadcasts zu einer Netzmask
def netzwerke(anzahl, sprung):
    ipliste = []
    for i in range(0, anzahl):
        ipliste.append((i*sprung, (i+1)*sprung-1))
    return ipliste


# 24
# 25
# 26
# netzmaske = 27
# Anzahl der Netzwerke
counter = 0
amount_networks = 0
ipranges = {}
for i in range(24, 31):
    amount_networks = 2 ** counter
#    print(amount_networks)
    counter += 1
    sprung = int(256 / amount_networks)
    ipranges[str(i)] = netzwerke(amount_networks, sprung)

print(ipranges)

#dek is_something(pattern, liste):
#    for item in pattern:
#        schalter = False
#        for element in liste:
#            print(f'vergleiche {item} mit {element}')
#            if item == element:
#                schalter = True
#                break
#        if schalter is False:
#            return False
#    return True
#
#
##############################
#liste = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
#while 1:
#    eingabe = input('Geben Sie die zu pruefende Zeichenkette ein: ')
#    result = is_something(eingabe, liste)
#    print(result)
##    result = True
##    for item in eingabe:
##        if item not in liste:
##            result = False
##    print(result)



