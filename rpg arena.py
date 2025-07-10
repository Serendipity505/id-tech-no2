#battle arena for players


class Character:
    # Constructor
    def __init__(self, name, strength, health, defense,speed,intelligence):
        self.name = name
        self.strength=strength
        self.health=health
        self.defense = defense
        self.speed = speed
        self.intelligence = intelligence

    #take_damage() Method
    def take_damage(self,damage):
        damage_taken = damage - self.defense
        self.health-=damage_taken
        return damage_taken
    #attack() Metgod
    def attack(self,target):
        damage = self.strength * 2
        damage_dealt = target.take_damage(damage)
        return damage_dealt
    # is_alive() Method
    def is_alive(self):
        return self.health > 0
player = Character("Momo the Cat", 30,50,100,100,100)
print(player.name)
print(player.strength)
print(player.health)
print(player.defense)
print(player.speed)
print(player.intelligence)

