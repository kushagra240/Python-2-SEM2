class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(self.brand, self.model, self.price)


Laptop("Dell", "Inspiron", 55000).display()
