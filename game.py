from classes import models
from classes import exceptions
import csv
import datetime
from Module.classes.models import Player
player_lives = 5

def main():
    try:
        level = 1
        lives = level
        command = input("Enter the command START, SCORES, HELP ")

        if command.lower() == "start":

            # block with constants
            name = input("Enter players name: ")
            score = 0

            all_attack = 0
            rigth_attacks = [1, 2, 3]
            st_defense = 0

            ######################
            while True:

            # block for input validation
                try:
                    all_attack = int(input("Enter 1, 2, 3 "))
                    if all_attack not in rigth_attacks:
                        raise ValueError
                    elif type(all_attack) != int:
                        raise TypeError
                except ValueError:
                    print("You can enter only 1, 2, 3")

                except TypeError:
                    print("You can enter only 1, 2, 3")
            ######################
            # in this block creating the player and enemy
                player = models.Player(name, player_lives, score, all_attack)
                enemy = models.Enemy(level, lives)
            # block attack
                st_attak = player.attack(enemy)
                # block defense
                if enemy.lives > 0:
                    all_attack = int(input("Enter 1, 2, 3 "))
                    st_defense = player.defence(enemy)
            ######################
            # fight block
                player.fight(st_attak, st_defense)
                print(player.lives)
                print(enemy.lives)
            ######################
            pass
        elif command.lower() == 'scores':
            pass

        elif command.lower() == 'help':
            pass
    except exceptions.EnemyDown:
        print("Enemy down")

    except exceptions.GameOver:
        print("Game over")
        with open('scores.txt', 'a', newline='') as file:
            witer = csv.writer(file)
            witer.writerow([name, score])
    finally:
        print("Good bye!")


if __name__ == '__main__':
    main()

    # try:
    # attack = int(input("Chose your fighter 1 - mage, 2 - warrior, 3 - rouge "))
    #     if attack not in rigth_attacks:
    #         raise ValueError
    #     elif type(attack) != int:
    #         raise TypeError
    #     else:
    #         continue
    # except ValueError:
    #     print("You can enter only 1, 2, 3")
    # except TypeError:
    #     print("You can enter only 1, 2, 3")
    ########################################
