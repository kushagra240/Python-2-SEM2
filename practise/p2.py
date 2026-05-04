class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

class my_book(Book):
    def __init__(self,title,author,edition,price):
        super().__init__(title,author)
        self.edition=edition
        self.price=price
    
    def display(self):
        print(self.title,self.author,self.edition,self.price)

b1=my_book("python","hey","first",500)
b1.display()

