'''
    Author: Santiago Uribe Gil
    Version: 1.0.0
    Date: 07/09/2022
'''

from taller1 import Supermarket

# a - create lists for each category
supermarket = Supermarket()

# b - create product in each category
supermarket.add_product("dairy", "Leche Colanta", 12)
supermarket.add_product("dairy", "Leche Alpina", 14)
supermarket.add_product("dairy", "Mantequilla la fina", 25)

# c - create product in each category via console
supermarket.add_product_console()

# d - check if product exists, if it does add, if it doesnt, create
supermarket.existing_product()

