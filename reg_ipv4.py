#!/usr/bin/python3
# -*- coding: utf-8 -*-

file = '/home/tn/bin/network_stuff.csv'

first_line = True
with open(file, 'r') as fh:
    for line in fh.readlines():
        if first_line is True:
            first_line = False
            continue
        rows = line.split(';')
#        print(rows)
        pattern = rows[0]
        octetts = pattern.split('.')
#        print(octett)

        l = 0
        for i in octetts:
            l = l + 1
 
        if l == 4:
            print(f'Treffer ok: {octetts}')
            for octett in octetts:
#                print(octett)
                for zeichen in octett:
                    print(zeichen)
#                    if zeichen == 0:
#                        print('ok')                    
#                    elif zeichen == 1:
#                        print('ok')
#                    else:
#                        continue
#  225.255.255.241/28
#  255.255.255.240



#            octett_ok = int(octett) 


#        else:
#            print(pattern)
#            print('WEG DAMIT')

