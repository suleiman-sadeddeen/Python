#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Das ist eine Klasse
class Fahrzeug():
    name = ''

    def vorwaerts_bewegen (self, geschwindigkeit):
        print(f'Ich bewege mich {geschwindigkeit} vorwaerts')


    def rueckwaerts_bewegen (self, geschwindigkeit):
        print('Ich bewege mich {geschwindigkeit} rueckwaerts')


###########################

golf = Fahrzeug()
    
golf.vorwaerts_bewegen('schnell')
golf.name = 'Golf'
print (golf.name)

bmw = Fahrzeug()
bmw.name = 'BMW'
bmw.rueckwaerts_bewegen()
bmw.vorwaerts_bewegen('sehr schnell')
print(bmw.name)

print (golf.name)
golf.rueckwaerts_bewegen('langsam')

