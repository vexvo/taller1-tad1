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
            amt_products = int(input("How many products will you input?"))
            try:
                for i in range(amt_products):
                    cat = input("What category is the product a part of?")
                    prod_name = input("What is the name of the product?")
                    prod_amt = int(input("What is the amount of this product?"))

                    self.add_product(cat, prod_amt, prod_amt)
                break
            except:
                print("Expected a numerical value")
