#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Productlist():

    def __init__(self, p):
        self.p = p
        self.productlist = []

    def read_csv_file(self, file, delimiter):
        firstline = True
        with open(file, 'r') as fh:
            for line in fh.readlines():
                if firstline is True:
                    firstline = False
                    continue
                items = line.split(delimiter)
                name = items[0][1:]
                name = name[:-1]
                costs = int(items[1])
                weight = int(items[2])
                amount = items[3]
                amount = int(amount[:-1])
                produkt = self.p.Product({'Name': name, 'Preis': costs, 'Gewicht': weight, 'Anzahl': amount})
                self.productlist.append(produkt)

    def list_products(self):
        for product in self.productlist:
            print(product)

    def add_product(self, product):
        self.productlist.append(product)

    def write_csv_file(self, myfile, delimiter):
        with open(myfile, 'w') as fh:
            first_element = True
            line = ''
            for product in self.productlist:
                for key, value in product.get_attribute().items():
                    value = str(value)
                    if first_element is True:
                        line += f"'{value}'"
                        first_element = False
                    else:
                        line += f"{delimiter}'{value}'"
                line += '\n'
            fh.writelines(line)

