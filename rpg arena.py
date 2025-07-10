#battle arena for players


class Character:
    # Constructor
    def __init__(self, name, strength, health, defense):
        self.name = name
        self.strength=strength
        self.health=health
        self.defense = defense

player = Character("Momo the Cat", 100,50,100)
print(player.name)
print(player.strength)
print(player.health)
print(player.defense)

