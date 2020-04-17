#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Person():
    myname = 'Otto'    

    def gib_name(self, myname):
        self.myname = myname

    def sag_namen(self, myname):
        print(f'Mein Name ist {myname}')

    def sag_namen1(self):
        print(f'Mein Name ist {Person.myname}')

    def sag_namen2(self):
        print(f'Mein Name ist {self.myname}')


peter = Person()
peter.gib_name('Peter')
maxi = Person()
maxi.gib_name('Maxi')
maxi.sag_namen2()
peter.sag_namen2()


#peter.sag_namen2()
#peter.sag_namen('Ernie')
#peter.sag_namen2()
#peter.sag_namen1()
#
#max.gib_name('Max')
#max.sag_namen2()
#peter.sag_namen2()











#peter.sag_namen('Gerd')
#peter.sag_namen1()
#peter.myname = 'Max'
#print(peter.myname)
#
#liese = Person()
#print(liese.myname)
#
