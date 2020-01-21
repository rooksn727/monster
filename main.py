player = {"name": "Nick",  "attack": 10, "heal": 15, "health": 100}
monster = {"name": "Chanco",  "attack": 12, "health": 100}
game_running = True

while game_running == True:

    print("Please choose your course of action")
    print("1) Attack")
    print("2) Heal")
    player_choice = input()

    if player_choice == "1":
        monster["health"] = monster["health"]  - player["attack"]
        player["health"] = player["health"] - monster["attack"]
        print(monster["health"])
        print(player["health"])
    elif player_choice == "2":
        print("You healed yourself")

    else:
        print("Invalid Input")
    if player["health"] <= 0 or monster["health"] <= 0:
        game_running = False