#!/usr/bin/python3
# -*- coding: utf-8 -*-

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

    def __repr__(self):
        output = '-' * 50 
        output += '\n'
        for key, value in self.attribute.items():
            output += f'{key}: {value}\n'
        return output

