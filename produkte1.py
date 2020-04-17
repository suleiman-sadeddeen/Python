#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Produkt():

    #produkt0 = {'Name': 'Milch',
    #           'Preis': 1,
    #           'Gewicht': 1000,
    #           'Anzahl': 4}
    def __init__(self, eigenschaft):
        self.attribut = eigenschaft
 
    def set_attribut(self, key, value):
#        self.attribut = {}
        self.attribut[key] = value

    def get_attribut(self):
        return self.attribut


apfel = Produkt({'Name': 'Apfel', 'Farbe': 'gruen'})


#print(apfel.get_attribut())
#apfel.set_attribut('Name', 'Apfel')
#apfel.set_attribut('Farbe', 'gruen')

print(apfel.get_attribut())

