__author__ = 'hap', 'aps'

"""
A module that takes seed value and filename as inputs from parameter and plays the Hot Potato game.

Author: Herat Alkeshkumar Patel (hp9198@rit.edu) , Ashesh Piyush Sheth (as2462@rit.edu)
"""

import sys
import random
from pathlib import Path
from dlList import LinkedList


def hotpotato():
    """
    Class: hotpotato
    Description: Plays the hot potato game
    :return: None
    """
    # Create a list.
    print("Welcome to the Hot Potato Game!")
    print("Reading from:", sys.argv[1])
    
    #Get path of file in the same folder
    path = Path(__file__).parent / sys.argv[1]
    f = open(path, "r")    
    newGame = LinkedList()
    player = f.readline()
    while player != '':
        newGame.append(player.strip())
        player = f.readline()

    print("Using random number generator seed:", sys.argv[2])
    random.seed(int(sys.argv[2]))
    print("Ready to play Hot Potato. Contestants are:")
    print(newGame.get_players(newGame.start()))
    while newGame.size() != 1:
        lstSize = newGame.size()
        music_beats = random.randint(-2*lstSize, 2*lstSize)
        print("The music starts (", music_beats, ")", sep='', end = ': ')
        print(newGame.play_music(music_beats))
        newGame.remove_player(music_beats)
    print(newGame.get_players(newGame.start()), "is the winner!")


if __name__ == "__main__":
    hotpotato()
