"""
A dice simulator.
"""
from die import Die

def setup():
    """
    Create user specified number of dice

    Ask the user how many dice they would like to roll, then return
    list with that number of dice.
    """
    dice = []
    number_of_dice = input('How many dice would you like to roll? ')
    try:
        number_of_dice = int(number_of_dice)
    except ValueError:
        print('Oops! Make sure to enter a number!')

    for _ in range(number_of_dice):
        die = create_die()
        dice.append(die)

    return dice

def create_die():
    """Takes an int (sides) from the user, and returns a die with that number of sides."""
    die = None
    while not die:
        sides = input('Please enter a number of sides for the die: ')
        try:
            die = Die(int(sides))
        except ValueError:
            print('Oops! Make sure to enter a number!')
    return die

def roll_dice(dice):
    """
    Roll the dice.

    Takes a list of Die() objects (dice), appends the results of each die's roll()
    method to a list, then returns the list.
    """
    return [die.roll() for die in dice]

def start_sim():
    """Starts the die rolling sim"""
    print('Welcome to the Dice Simulator')
    dice = setup()

    while True:
        response = input("Type 'r' to roll; type 'e' to exit. ")
        if response == 'e':
            print('Goodbye!')
            break
        elif response == 'r':
            print(roll_dice(dice))
        elif response == 's':
            dice = setup()
        else:
            print('Invalid response.')

if __name__ == '__main__':
    start_sim()
