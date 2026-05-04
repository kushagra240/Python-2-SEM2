players = []


def add_player():
    players.append(input("Player name: "))


def update_player():
    old_name = input("Name to update: ")
    new_name = input("New player name: ")
    if old_name in players:
        index = players.index(old_name)
        players[index] = new_name


add_player()
update_player()
print(players)