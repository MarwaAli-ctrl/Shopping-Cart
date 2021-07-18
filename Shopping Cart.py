#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Cart:
    def __init__(self, item = []):
        self.item = list
    def add(self, item):
        if self == 'add':
            item = input('What would you like to add to your cart? ')
            cart.append(item)
            return(f"Your cart now has: {cart}.")
            
    def remove(self, item):
        if self == 'remove':
            delete = input('What would you like to remove? ')
            cart.pop(item)
            
    def show(self, item):
        if self == 'show':
            input(f'This is your current shopping cart {cart}.')

    def quit(self):
        if self == 'quit':
            return('thanks for shopping')
            
       
while True:
    self = input('Please make a selection? add/remove/show/quit ')

