books=[]

def add_book():
    book=input("book name:")
    books.append(book)

def remove_book():
    book=input("book name to remove:")
    if book in books:
        books.remove(book)
        print("removed")
    else:
        print("not found")

def reverse_books():
    books.reverse()

add_book()
remove_book()
reverse_books()
print(books)
