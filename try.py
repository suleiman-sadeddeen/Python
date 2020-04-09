#!/usr/bin/python3

a = input('enter a number : ' )
a = int(a)


try:
    l = a / 0
    print(l)
except:
    print('das geht nit')
print('Ende')

