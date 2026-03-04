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