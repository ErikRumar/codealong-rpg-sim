from resources import Character, Goblin, save_character, load_characters
import random

def fight(fighter : Character, enemies : list):

    while not len(enemies) == 0:
        fighter_target = random.choice(enemies)
        fighter_target.take_damage(fighter.attack())
        if fighter_target.gethealth() <= 0:
            print("Target has died")
            enemies.remove(fighter_target)
            if len(enemies) == 0:
                break
    
    print(f'fight is over! {fighter.name} won!')

def new_fight(players: list, enemies : list):
    participants = players + enemies # slå ihop alla deltagare i en lista
    random.shuffle(participants)

    for char in participants:
        target = ""

        # check if goblin or character
        
        if char in players:
            target = random.choice(enemies)
        else:
            target = random.choice(players)
            
        target.take_damage(char.attack())    
        if target.gethealth() == 0:
            print(f"{char.get_name()} has killed {target.get_name()}")
            if (type(target) == Goblin):
                enemies.remove(target)
            else:
                players.remove(target)
            participants.remove(target)
        else:
            print(f"{target.get_name()} was attacked by {char.get_name()}")
            print(f"{target.get_name()} has {target.gethealth()} healthpoints left")
        if len(enemies) == 0 or len(players) == 0: break


def main():

    players = []

    enemies = []

    nick = Character("Nick", 15, 3, 1)
    emy = Character("Emy", 20, 6, 5)
    players.append(nick)
    players.append(emy)

    enemies.append(Goblin(1))
    enemies.append(Goblin(2))

    # fight(emy, enemies)

    while not (len(enemies) == 0 or len(players) == 0):
        new_fight(players, enemies)
    if len(enemies) == 0:
        print("The players won!")
    elif len(players) == 0:
        print("The goblins won!")
    # save_character(emy)

    players = load_characters()
    for player in players:
        print("\n", player)
    

if __name__ == "__main__":
    main()