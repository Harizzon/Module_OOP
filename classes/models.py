from random import choice
from classes import exceptions


class Enemy:
    """
    This class create an enemy
    """
    def __init__(self, level, lives):
        self.level = level
        self.lives = lives

    def decrease_lives(self):
        """
        this method decrease enemy's life
        :return: int
        """
        self.lives -= 1
        if self.lives == 0:
            raise exceptions.EnemyDown
        return self.lives

    @staticmethod
    def select_attack():
        """
        THis method show type of attack
        :return: random int
        """
        enemy_attack = choice([1, 2, 3])

        return enemy_attack


class Player:
    """
    This class create player
    """
    def __init__(self, name, lives, score, allowed_attacks):
        self.name = name
        self.lives = lives
        self.score = score
        self.allowed_attacks = allowed_attacks

    def decrease_lives(self):
        """
        This method decrease players health
        :return: int
        """
        self.lives = self.lives - 1
        if self.lives == 0:
            raise exceptions.GameOver
        return self.lives

    def attack(self, enemy_obj):
        """
        this method returns result of players attack
        :param enemy_obj: class Enemy
        :return: int
        """
        enemy_attack = enemy_obj.select_attack()

        if int(self.allowed_attacks) == 1:
            if enemy_attack == 1:
                return 0
            elif enemy_attack == 2:

                enemy_obj.decrease_lives()
                self.score += 1
                return 1
            elif enemy_attack == 3:

                return -1
        elif int(self.allowed_attacks) == 2:
            if enemy_attack == 1:

                return -1
            elif enemy_attack == 2:

                return 0
            elif enemy_attack == 3:

                enemy_obj.decrease_lives()
                self.score += 1
                return 1
        elif int(self.allowed_attacks) == 3:
            if enemy_attack == 1:

                enemy_obj.decrease_lives()
                self.score += 1
                return 1
            elif enemy_attack == 2:

                return -1
            elif enemy_attack == 3:

                return 0
        else:
            return print('Error', self.allowed_attacks, enemy_obj.select_attack())

    def defence(self, enemy_obj):
        """
                this method returns result of players defense
                :param enemy_obj: class Enemy
                :return: int
         """
        enemy_attack = enemy_obj.select_attack()

        if enemy_attack == 1:
            if self.allowed_attacks == 1:

                return 0
            elif self.allowed_attacks == 2:

                self.decrease_lives()
                return 1
            elif self.allowed_attacks == 3:

                return -1
        elif enemy_attack == 2:
            if self.allowed_attacks == 1:

                return -1
            elif self.allowed_attacks == 2:

                return 0
            elif self.allowed_attacks == 3:

                self.decrease_lives()
                return 1
        elif enemy_attack == 3:
            if self.allowed_attacks == 1:

                self.decrease_lives()
                return 1
            elif self.allowed_attacks == 2:

                return -1
            elif self.allowed_attacks == 3:

                return 0
        else:
            return print('Error', self.allowed_attacks, enemy_obj.select_attack())

    @staticmethod
    def fight(attack, defense):
        """
        This method returns the result of the round
        :param attack: int
        :param defense: int
        :return: str
        """
        print("Results of the round: ")
        if attack == 1:
            print("You attacked successfully")
        elif attack == 0:
            print("It's a draw!")
        elif attack == -1:
            print('You missed!')

        if defense == 1:
            print("Enemy attacked successfully!")

        elif defense == 0:
            print("It's a draw!")

        elif defense == -1:
            print("Enemy attacked successfully!")
