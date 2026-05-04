class Shape:
    def description(self):
        print("This is a shape.")


class Square(Shape):
    def description(self):
        print("This is a square.")


class Triangle(Shape):
    def description(self):
        print("This is a triangle.")


for shape in (Square(), Triangle()):
    shape.description()
