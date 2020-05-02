
"""
This module for custom exception
"""


class GameOver(Exception):
    """
    This exception raises when player health == 0 or less
    """


class EnemyDown(Exception):
    """
        This exception raises when enemy health == 0 or less
    """
