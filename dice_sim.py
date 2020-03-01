"""
A dice simulator.
"""
from die import Die

def create_die():
    """
    Takes an int (sides) from the user, and returns a die with that
    number of sides.
    """
    die = None
    while not die:
        sides = input('Please enter a number of sides for the die: ')
        try:
            die = Die(int(sides))
        except ValueError:
            print('Oops! Make sure to enter a number!')
    return die

def start_sim():
    """
    Starts the die rolling sim
    """
    print('Welcome to the Dice Simulator')
    die = create_die()
    while True:
        response = input("Type 'r' to roll; type 'e' to exit. ")
        if response == 'e':
            print('Goodbye!')
            break
        elif response == 'r':
            print(die.roll())
        elif response == 's':
            die = create_die()
        else:
            print('Invalid response.')

if __name__ == '__main__':
    start_sim()
