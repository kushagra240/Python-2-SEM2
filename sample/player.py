class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Player(Person):
    def __init__(self, name, age, team, runs):
        super().__init__(name, age)
        self.team = team
        self.runs = runs

    def to_dict(self):
        return {"name": self.name, "age": self.age, "team": self.team, "runs": self.runs}


players = []


def add_player(name, age, team, runs):
    players.append(Player(name, age, team, runs))


def delete_player(name):
    for player in players:
        if player.name.lower() == name.lower():
            players.remove(player)
            return True
    return False


def update_player(name, new_name):
    for player in players:
        if player.name.lower() == name.lower():
            player.name = new_name
            return True
    return False


def display_players():
    for player in players:
        print(player.to_dict())