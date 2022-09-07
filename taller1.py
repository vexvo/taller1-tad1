class Supermarket:

    def __init__(self):
        self.dairy = []
        self.cleaning = []
        self.grains = []

    def add_product(self, category, product_name, product_amt: int):
        if (category == "dairy"): self.dairy.append((product_name, product_amt))
        if (category == "cleaning"): self.cleaning.append((product_name, product_amt))
        if (category == "grains"): self.grains.append((product_name, product_amt))
        else: print("Category entered does not exist")
