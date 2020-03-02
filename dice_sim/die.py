"""
The die module.

This module contains the Die object, which has one attribute and one method:
        sides (int) represents the number of sides the die has
        roll() returns a random int between 1 and the number of sides (inclusive)
"""
from random import random
from math import ceil
class Die:
    """
    A die object.

    This die object has one attribute (sides) which represents the number
    of sides of the die. It has one public method (roll()) which returns
    an int between 1 and the number of sides (inclusive).
    """
    def __init__(self, sides):
        assert isinstance(sides, int), 'sides must be an int'
        self.sides = sides

    def __str__(self):
        return 'A ' + str(self.sides) + ' sided die'

    def __repr__(self):
        return 'Die(' + str(self.sides) + ')'

    def roll(self):
        """
        Rolls the die.

        Rolls the die by generating random float between zero and one,
        multiplying that by the number of sides, rounding up, and
        returning the resulting int.
        """
        return ceil(random() * self.sides)
