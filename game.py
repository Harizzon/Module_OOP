import csv
from classes import models
from classes import exceptions
from classes import settings


player_lives = settings.player_lives


def main():
    try:
        level = 1
        lives = 1
        command = input("Enter the command START, SHOW SCORES, HELP, EXIT ")

        if command.lower() == "start":

            # block with constants
            name = input("Enter players name: ")
            score = 0
            all_attack = 0
            player = models.Player(name, player_lives, score, all_attack)
            enemy = models.Enemy(level, lives)
            all_attack = 0
            rigth_attacks = [1, 2, 3]
            st_defense = 0

            ######################
            while True:

                # block for input validation
                try:
                    all_attack = int(input("Chooser your fighter: 1 - mage, 2 - warrior, 3 - rouge "))
                    if all_attack not in rigth_attacks:
                        raise ValueError

                except ValueError:
                    print("You can enter only 1, 2, 3")

                except TypeError:
                    print("You can enter only 1, 2, 3")
                ######################
                # in this block creating the player and enemy
                player.allowed_attacks = all_attack
                # block attack
                try:
                    st_attak = player.attack(enemy)
                    # block defense
                    if enemy.lives > 0:
                        all_attack = int(input("Chooser your defender: 1 - mage, 2 - warrior, 3 - rouge "))
                        player.allowed_attacks = all_attack
                        st_defense = player.defence(enemy)
                    ######################
                    # fight block
                    player.fight(st_attak, st_defense)
                    print(f'You have {player.lives} lives')
                    print(f'Enemy have {enemy.lives} lives')
                    print("--------------------------------------")
                ######################
                except exceptions.EnemyDown:
                    print("Enemy down")
                    level += 1
                    enemy.lives = level
                    score += 5
                    print("New enemy added")
                    print(f'Welcome to the level: {level}')
                    print(enemy.lives)

        elif command.lower() == 'show scores':
            with open('scores.txt', 'r') as file:
                reader = csv.reader(file)
                for item in reader:
                    print(item)

        elif command.lower() == 'help':
            print("""
            This is simple game.
            
            """)

        elif command.lower() == 'exit':
            raise KeyboardInterrupt
    except exceptions.GameOver:
        print("Game over")
        print(f"Your result is: {score}")
        with open('scores.txt', 'a', newline='') as file:
            file.write([name, score])


    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")


if __name__ == '__main__':
    main()
