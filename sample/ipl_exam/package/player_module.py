class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Player(Person):
    def __init__(self, name, age, team, runs):
        super().__init__(name, age)
        self.team = team
        self.runs = runs

    def display(self):
        print(self.name, self.age, self.team, self.runs)