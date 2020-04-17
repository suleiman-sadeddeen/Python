#!/usr/bin/python3
# *.* coding: utf-8 -*-







class Product():

    def __init__(self, attribute):
        self.attribute = attribute

    def set_attribute(self, key, value):
        self.attribute[key] = value

    def get_attribute(self):
        return self.attribute

    def show_me(self):
        for _key, _value in self.attribute.items():
            print(f'{_key}: {_value}')

birne = Product({'Name': 'Birne', 'Gewicht': 500, 'Preis': 2, 'Farbe': 'gruen'})
birne.set_attribute('Preis', 1)
print(birne.get_attribute())
birne.set_attribute('Preis', 3)
birne.set_attribute('Farbe', 'braun')
print(birne.get_attribute())

birne.show_me()
