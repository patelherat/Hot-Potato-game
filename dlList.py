__author__ = 'hap', 'aps'

"""
Cursor(potato) based implementation that handles each of the functionality of the Hot Potato game.

Author: Herat Alkeshkumar Patel (hp9198@rit.edu) , Ashesh Piyush Sheth (as2462@rit.edu)
"""

from dlNode import LinkedNode

class LinkedList:
    """
    Class: LinkedList
    Description: Handles functionality like adds a player, removes a player, plays music..
    """
    __slots__ = 'potato'


    def __init__( self ):
        """ Create an empty list.
        """
        self.potato = None

    def append( self, player ): ###############
        """
        Appends the player
        :param player: player to be added
        :return: None
        """
        node = self.potato
        newNode = LinkedNode( player )
        if node == None:
            self.potato = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            newNode.next = self.potato
            self.potato.prev = newNode
            while node.next != self.potato:
                node = node.next
            node.next = newNode
            newNode.prev = node
            

    def start( self ):
        """
        Returns the player to start with at each round
        :return: cursor(potato)
        """
        return self.potato


    def size( self ):
        """
        Gives size
        :return: None
        """
        return self._size_to_end( self.potato )


    def _size_to_end( self, node ):
        """
        Calculates the total players from the node
        :param node: node from where to calculate the size
        :return: size
        """
        if node.next == self.potato:
            return 1
        else:
            return 1 + self._size_to_end( node.next )


    def get_players(self, node):
        """
        Gets the player at the node
        :param node: the current player
        :return: player name
        """
        if node.next == self.potato:
            return node.player_name
        else:
            return node.player_name + ", " + self.get_players(node.next)


    def remove_player(self, beats):
        """
        Removes the player
        :param beats: music beats
        :return: None
        """
        self.potato.next.prev = self.potato.prev
        self.potato.prev.next = self.potato.next
        if beats < 0:
            self.potato = self.potato.prev
        else:
            self.potato = self.potato.next


    def play_music(self, beats):
        """
        Traverses in the list according to the values of the beats
        :param beats: music beats
        :return: player name and beats
        """
        if beats == 0:
            return self.potato.player_name + " is stuck holding the potato!"
        else:
            if beats < 0:
                self.potato = self.potato.prev
                return self.potato.next.player_name + " -> " + self.play_music(beats+1)
            else:
                self.potato = self.potato.next
                return self.potato.prev.player_name + " -> " + self.play_music(beats-1)
