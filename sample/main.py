import csv
import json

from player import add_player, delete_player, display_players, players, update_player


CSV_FILE = "players.csv"
JSON_FILE = "players.json"


def save_data():
    records = [player.to_dict() for player in players]
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "team", "runs"])
        writer.writeheader()
        writer.writerows(records)
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)
    print("Saved")


def load_data():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            records = list(csv.DictReader(file))
    players.clear()
    for record in records:
        add_player(record["name"], int(record["age"]), record["team"], int(record["runs"]))
    print("Loaded")


def main():
    while True:
        print("\n1.Add 2.Delete 3.Update 4.Display 5.Save 6.Load 7.Exit")
        choice = input("Enter choice: ")
        try:
            if choice == "1":
                add_player(input("Name: "), int(input("Age: ")), input("Team: "), int(input("Runs: ")))
            elif choice == "2":
                print("Deleted" if delete_player(input("Name to delete: ")) else "Not found")
            elif choice == "3":
                print("Updated" if update_player(input("Name to update: "), input("New Name: ")) else "Not found")
            elif choice == "4":
                display_players()
            elif choice == "5":
                save_data()
            elif choice == "6":
                load_data()
            elif choice == "7":
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input")
        except FileNotFoundError:
            print("File not found")
        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()