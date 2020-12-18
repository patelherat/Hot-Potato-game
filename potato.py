from dlList import LinkedList
from pathlib import Path

import sys
import random

def main():
    print("Welcome to the Hot Potato Game!")
    print("Reading from:", sys.argv[1])

    # Get path of file in the same folder
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
        music_beats = random.randint(-2 * lstSize, 2 * lstSize)
        print("The music starts (", music_beats, ")", sep='', end=': ')
        print(newGame.play_music(music_beats))
        newGame.remove_player(music_beats)
    print(newGame.get_players(newGame.start()), "is the winner!")
    # print()
    # print("Welcome to the Hot Potato Game!")
    # print("Reading from:", sys.argv[1])
    # print("Using random number generator:", sys.argv[2])
    # print("Ready to play Hot Potato.  Contestants are:")
    # f = open(sys.argv[1], "r")
    # # print(f.read())
    # while True:
    #     line = f.readline().strip()
    #     if line == '':
    #         break
    #     else:
    #         print(line, end=", ")
    # random.seed(int(sys.argv[2]))
    # lstSize = 6                                             #from other file
    # #print(random.randint(-2*lstSize, 2*lstSize))
    # print()
    # print("The music starts (" + str(random.randint(-2*lstSize, 2*lstSize)) + "):")

if __name__ == '__main__':
    main()
