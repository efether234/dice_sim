"""
A die object.
"""
import random
import math
class Die():
    def __init__(self, sides):
        assert isinstance(sides, int), 'sides must be an int'
        self.sides = sides

    def roll(self):
        """
        Rolls the die.

        Args:
            sides: int - number of sides of the die
        
        Return: int
        """
        return math.ceil(random.random() * self.sides)
