from typing_extensions import Self
from xml.etree.ElementTree import TreeBuilder


class Supermarket:

    # a
    def __init__(self):
        self.dairy = []
        self.cleaning = []
        self.grains = []

    # b
    def add_product(self, category, product_name, product_amt: int):
        if (category == "dairy"): self.dairy.append((product_name, product_amt))
        if (category == "cleaning"): self.cleaning.append((product_name, product_amt))
        if (category == "grains"): self.grains.append((product_name, product_amt))
        else: print("Category entered does not exist")

    # c
    def add_product_console(self):
        while True:
            try:
                amt_products = int(input("How many products will you input?"))
                for i in range(amt_products):
                    cat = input("What category is the product a part of?")
                    prod_name = input("What is the name of the product?")
                    while True:
                        try:
                            prod_amt = int(input("What is the amount of this product?"))
                            break
                        except:
                            print("Expected a numerical value")
                    self.add_product(cat, prod_amt, prod_amt)
                break
            except:
                print("Expected a numerical value")

    # d
    def existing_product(self):
        while True:
            amt_products_validate = int(input("How many products are you going to validate"))
            try:
                for i in range(amt_products_validate):
                    product_searched = input("Product which's existence will be validated")
                    found = False
                    size = self.dairy.size() + self.cleaning.size() + self.grains.size()
                    amt_added = 0
                    while found == False and i < size:
                        if self.dairy[i] == product_searched:
                            amt_added = int(input("How much of the product will you add"))
                            aux = list(self.dairy[i])
                            aux[i+1] = aux[i] + amt_added 
                            found = True
                        elif i > self.dairy.size():
                            if self.cleaning[i] == product_searched:
                                amt_added = int(input("How much of the product will you add"))
                                aux = list(self.cleaning[i])
                                aux[i+1] = aux[i] + amt_added 
                                found = True
                            elif i > (self.dairy.size() + self.cleaning.size()):
                                if self.grains[i] == product_searched:
                                    amt_added = int(input("How much of the product will you add"))
                                    aux = list(self.grains[i])
                                    aux[i+1] = aux[i] + amt_added 
                                    found = True
                                else:
                                    print("Product doesn't exist, creating it")
                                    self.add_product_console()
                                    break

                break
            except:
                print("Expected a numerical value")

    # e
    def print_products(self):
        print(f'------------ PRODUCTS ------------\n {self.dairy}\n {self.cleaning}\n {self.grains}')