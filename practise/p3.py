books=[{"name":"HI","author":"hello"},{"name":"good","author":"morning"}]

def update_books():
    books[1]["name"]="good morning"

def sort_books():
    books.sort(key=lambda book: book["name"])

update_books()
sort_books()
print(books)