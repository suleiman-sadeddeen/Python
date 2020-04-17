#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Das ist ein Person
class Person():
    name = ''

    def laufen (self):
        print(f'kann laufen')

#    def gehen (self):
#        print (f'kann gehen')


sulo = Person()

sulo.laufen('schnell')
sulo.name = 'sulo'
print(sulo.name)
