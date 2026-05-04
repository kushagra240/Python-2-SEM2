class item:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
class book(item):
    def __init__(self,name,price,author):
        super().__init__(name,price)
        self.author=author
    
    def display(self):
        print(f"name:{self.name}, price:{self.price}, author:{self.author}")
        
        