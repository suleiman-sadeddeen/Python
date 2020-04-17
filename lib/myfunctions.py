#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Funktion die prueft ob alle Zeichen der Eingabe in einer gegebenen Liste enthalten sind
# Die Funktion gibt True odder False zurueck
def is_something(pattern, liste):
    for item in pattern:
        schalter = False
        for element in liste:
            if item == element:
                schalter = True
                break
        if schalter is False:
            return False
    return True

# berechnen der Netzwerkadressen und der Broadcasts zu einer Netzmask
def netzwerke():
    counter = 0
    amount_networks = 0
    ipranges = {}
    for i in range(24, 31):
        amount_networks = 2 ** counter
        counter += 1
        sprung = int(256 / amount_networks)
        ipliste = []
        for i2 in range(0, amount_networks):
            ipliste.append((i2*sprung, (i2+1)*sprung-1))
        ipranges[str(i)] = ipliste
    return ipranges

