import json
from game import Game


print("USER.PY LOADED")


class User:
    def __init__(self, username):
        self.username = username
        self.logged_games = []
        
    def log_game(self, game, hours_played, rating):
     print("log_game method exists")
     entry = {
         "game": game,
         "hours_played": hours_played,
         "rating": rating
     }
     self.logged_games.append(entry)

    def show_library(self):
         print("show_library method exists")
         print(f"{self.username}'s Game Library:")
         for entry in self.logged_games:
           g = entry["game"]
           print(f"{g.title} ({g.genre}, {g.release_year}) - Hours: {entry['hours_played']}, Rating: {entry['rating']}")

    def save_library(self):
       data_to_save = []
       for entry in self.logged_games:
          g = entry["game"]
          new_entry = {
             "title": g.title,
             "genre": g.genre,
            "release_year": g.release_year,
            "hours_played": entry["hours_played"],
            "rating": entry["rating"]

          }
          data_to_save.append(new_entry)

         #Write JSON once
       with open("library.json", "w") as f:
            json.dump(data_to_save, f)


    def load_library(self):
        self.logged_games = []
        with open("library.json", "r") as f:
             data_loaded = json.load(f)
             for entry in data_loaded:
              g = Game(entry["title"], entry["genre"], entry["release_year"])
             logged_entry = {
                "game": g,
                "hours_played": entry["hours_played"],
                "rating": entry["rating"]
             }
             self.logged_games.append(logged_entry)