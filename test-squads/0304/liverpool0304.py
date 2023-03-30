
class Player(object):
    def __init__(self, squad_number, name, age, nation, position,previous_club,):
        self.squad_number = squad_number
        self.name = name
        self.age = age
        self.nation = nation
        self.position = position
        self.previous_club = previous_club


steven_gerrard = Player(8, "Steven Gerrard", 24, "England", "CM", "Liverpool")



squad = {
    "8": steven_gerrard,
}


