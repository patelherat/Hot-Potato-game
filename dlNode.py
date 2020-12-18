__author__ = 'hap', 'aps'

"""
A module that loops through the players circularly.

Author: Herat Alkeshkumar Patel (hp9198@rit.edu) , Ashesh Piyush Sheth (as2462@rit.edu)
"""

class LinkedNode:
    """
    Class: LinkedNode
    Description: Keeps track of the next player and the previous player at current position
    """
    __slots__ = "player_name", "next", "prev"


    def __init__( self, player_name, next_player = None, prev_player = None ):
        """
        Keeps track of the previous, current player name and next player
        :param player_name: the current player
        :param next_player: pointer to the next player
        :param prev_player: pointer to the previous player
        """

        self.player_name = player_name
        self.next = next_player
        self.prev = prev_player


    def __str__( self ):
        """
        Returns string representation of the contents of this node
        :return: Player name
        """
        return str( self.player_name )
