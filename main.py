import json
print("MAIN IS RUNNING")
from game import Game
from user import User


# create games
game1= Game("Persona 5", "JRPG", 2016)
game2= Game("Resident Evil 7: Biohazard", "Horror", 2017)
# create a user
user1 = User("Amarion")
user1.log_game(game1, 150, 9)
user1.log_game(game2, 40, 7)

print("About to call show_library")
user1.show_library()