#imports



#globals



#classes

class Character:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return f'Name: {self.name}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}'


#funciton


def hello():
    print("hello world")



#main code




