from library.module import book

try:
    book1=book(input("name:"),int(input("price:")),input("author:"))
    book1.display()
except ValueError:
    print("invalid input")

