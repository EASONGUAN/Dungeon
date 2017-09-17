"""This is a class representing the hero itself, the enemies and the objects on the map."""

class World:
    def __init__(self, hero):
        self.hero = hero
        self.enemies = []
        self.walls = []
        self.items = []
        self.mazes = []  # A list of mazes(maps).

    def generate_walls(self, width, height):
        pass

