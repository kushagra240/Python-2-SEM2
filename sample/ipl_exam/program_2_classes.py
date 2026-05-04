class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Player(Person):
    def __init__(self, name, age, team, runs):
        super().__init__(name, age)
        self.team = team
        self.runs = runs


p1 = Player("Virat", 36, "RCB", 7000)
print(p1.name, p1.age, p1.team, p1.runs)