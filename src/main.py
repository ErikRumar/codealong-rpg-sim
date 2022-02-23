from resources import Character, Goblin, save_character, load_characters, save_character, create_character
import random
import time

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
        # target = ""

        # check if goblin or character
        
        if char in players:
            target = enemies[random.randint(0, len(enemies) - 1)]
        else:
            target = players[random.randint(0, len(players) - 1)]
            
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
            time.sleep(1)
            print(f"{target.get_name()} has {target.gethealth()} healthpoints left")
            time.sleep(1)
        if len(enemies) == 0 or len(players) == 0: break


def main():

    players = load_characters()
    enemies = []


    print("Would you like to create a new character? (y/n)")
    new_char = input(": ")
    if new_char.lower() == "y":
        new = create_character()
        players.append(new)


    amount_of_goblins = int(input("How many goblins should they fight?: "))
    for i in range(amount_of_goblins):
        enemies.append(Goblin(i+1))

    while not (len(enemies) == 0 or len(players) == 0):
        new_fight(players, enemies)
    if len(enemies) == 0:
        print("The players won!")
        print("Would you like to save the remaining characters? (y/n)")
        while True:
            save_progress = input(": ")
            if save_progress.lower == "y":
                save_character(players)
            elif save_progress.lower() == "n":
                break
            else:
                print("That was not a valid option")
    elif len(players) == 0:
        print("The goblins won!")
    # save_character(emy)

    players = load_characters()
    for player in players:
        print("\n", player)
    

if __name__ == "__main__":
    main()