from package.player_module import Player


try:
    player = Player(input("Name: "), int(input("Age: ")), input("Team: "), int(input("Runs: ")))
    player.display()
except ValueError:
    print("Invalid input")