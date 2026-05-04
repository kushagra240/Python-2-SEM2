players = [{"name": "Virat"}, {"name": "Rohit"}]


def add_player():
    players.append({"name": input("Player name: ")})


def delete_player():
    name = input("Name to delete: ")
    for player in players:
        if player["name"] == name:
            players.remove(player)
            break


def display_players():
    for player in players:
        print(player)


add_player()
delete_player()
display_players()