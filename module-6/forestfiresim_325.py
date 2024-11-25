#Colton Kohler
#11/24/24
#Module 6.2 Assignment
"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = 'W'  # Water feature

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue  # Skip cells already processed.

                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER  # Water cannot change.
                elif (forest[(x, y)] == EMPTY
                      and random.random() <= GROW_CHANCE):
                    nextForest[(x, y)] = TREE  # Grow a tree.
                elif (forest[(x, y)] == TREE
                      and random.random() <= FIRE_CHANCE):
                    nextForest[(x, y)] = FIRE  # Lightning sets tree on fire.
                elif forest[(x, y)] == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE  # Spread fire.
                    nextForest[(x, y)] = EMPTY  # Tree burns down.
                else:
                    nextForest[(x, y)] = forest[(x, y)]  # Copy existing state.

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    lake_width = WIDTH // 4
    lake_height = HEIGHT // 4
    lake_start_x = (WIDTH - lake_width) // 2
    lake_start_y = (HEIGHT - lake_height) // 2

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if lake_start_x <= x < lake_start_x + lake_width and \
               lake_start_y <= y < lake_start_y + lake_height:
                forest[(x, y)] = WATER  # Place water in the center.
            elif (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as empty space.

    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == WATER:
                bext.fg('blue')
                print(WATER, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Reset to default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # End the program when Ctrl-C is pressed.
