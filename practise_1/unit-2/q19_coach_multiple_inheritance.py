class SportsPerson:
    def __init__(self, sport):
        self.sport = sport


class Employee:
    def __init__(self, name):
        self.name = name


class Coach(SportsPerson, Employee):
    def __init__(self, name, sport, team_name):
        SportsPerson.__init__(self, sport)
        Employee.__init__(self, name)
        self.team_name = team_name

    def display(self):
        print(self.name, self.sport, self.team_name)


Coach("Ravi", "Cricket", "Warriors").display()
