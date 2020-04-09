#!/usr/bin/python3


def gross(Ausgabetext):
    gross = False
    for i in ausgabetext:
        if(gross is True):
            gross = False
            print(i.upper())
        else:
            gross = True
            print(i.lower())

ausgabetext =input('gib dein text ein: ')
gross(ausgabetext)
        
