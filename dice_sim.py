#!/usr/bin/env python3
"""
A dice simulator.

Author: Evan Fetherolf
"""
import sim

def main():
    """Starts the die rolling sim"""
    print('Welcome to the Dice Simulator')
    dice = sim.create_dice()

    while True:
        response = input("Type 'r' to roll; type 'e' to exit. ")
        if response == 'e':
            print('Goodbye!')
            break
        elif response == 'r':
            print(sim.roll_dice(dice))
        elif response == 's':
            dice = sim.create_dice()
        else:
            print('Invalid response.')

if __name__ == '__main__':
    main()
