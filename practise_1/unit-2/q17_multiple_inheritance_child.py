class Father:
    def __init__(self):
        self.father_feature = "Tall"


class Mother:
    def __init__(self):
        self.mother_feature = "Kind"


class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def display(self):
        print(self.father_feature, self.mother_feature)


Child().display()
