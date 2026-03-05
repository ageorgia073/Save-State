class Game:
    def __init__(self, title, genre, release_year):
        self.title = title
        self.genre = genre
        self.release_year = release_year

game1 = Game("Persona 5", "JRPG", 2016)
game2 = Game("Resident Evil 7: Biohazard", "Horror", 2017)
game3 = Game("Mortal Kombat 11", "Fighting", 2019)





games = [game1,game2,game3]

for g in games:
   print(f"{g.title} ({g.genre}, {g.release_year})")
