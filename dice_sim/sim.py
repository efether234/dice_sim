"""
The dice simulator module.

This module contains all of the functions necessary to run the simulation:
        create_dice() creates the dice used for the simulation. It asks the user
    how many dice to roll, and then how many sides each die should have. It
    returns a list of dice.
        roll_dice() actually rolls the dice. It iterates through the list of dice
    and rolls each one, appending the result to a new list, which it returns.
"""
from die import Die

def create_dice():
    """
    Create user specified number of dice

    Ask the user how many dice they would like to roll,vask the user how many
    sides each die should have, then returnvlist with that number of dice.
    """
    dice = []
    number_of_dice = None
    while not number_of_dice:
        try:
            number_of_dice = int(input('How many dice would you like to roll? '))
        except ValueError:
            print('Oops! Make sure to enter a number!')

    for i in range(number_of_dice):
        die = None
        while not die:
            try:
                die = Die(int(input('Please enter a number of sides for die #' \
                    + str(i + 1) + ': ')))
            except ValueError:
                print('Oops! Make sure to enter a number!')
        dice.append(die)

    return dice

def roll_dice(dice):
    """
    Roll the dice.

    Takes a list of Die() objects (dice), appends the results of each die's roll()
    method to a list, then returns the list.
    """
    return [die.roll() for die in dice]
