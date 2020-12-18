"""
linkedlist.py

A Linked List interface and implementation in Python
This version uses a cursor. Using indices is inherently inefficient and
hides the strengths of the linked list.
Cursors, immutable, are created by list methods.

auteur: James Heliotis
"""

from dlNode import LinkedNode

class LinkedList:

    __slots__ = 'potato'

    def __init__(self):
        """ Create an empty list.
        """
        self.potato = None

    def append(self, player):
        """
        Appends the player
        :param player: player to be added
        :return: None
        """
        node = self.potato
        newNode = LinkedNode(player)
        if node == None:
            self.potato = newNode
            newNode.next_player = newNode
            newNode.prev_player = newNode
        else:
            newNode.next_player = self.potato
            self.potato.prev_player = newNode
            while node.next_player != self.potato:
                node = node.next_player
            node.next_player = newNode
            newNode.prev_player = node

    def start(self):
        """
        Returns the player to start with at each round
        :return: cursor(potato)
        """
        return self.potato

    def size(self):
        """
        Gives size
        :return: None
        """
        return self._size_to_end(self.potato)

    def _size_to_end(self, node):
        """
        Calculates the total players from the node
        :param node: node from where to calculate the size
        :return: size
        """
        if node.next_player == self.potato:
            return 1
        else:
            return 1 + self._size_to_end(node.next_player)

    def get_players(self, node):
        """
        Gets the player at the node
        :param node: the current player
        :return: player name
        """
        if node.next_player == self.potato:
            return node.player_name
        else:
            return node.player_name + ", " + self.get_players(node.next_player)

    def remove_player(self, beats):
        """
        Removes the player
        :param beats: music beats
        :return: None
        """
        self.potato.next_player.prev_player = self.potato.prev_player
        self.potato.prev_player.next_player = self.potato.next_player
        if beats < 0:
            self.potato = self.potato.prev_player
        else:
            self.potato = self.potato.next_player

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
                self.potato = self.potato.prev_player
                return self.potato.next_player.player_name + " -> " + self.play_music(beats + 1)
            else:
                self.potato = self.potato.next_player
                return self.potato.prev_player.player_name + " -> " + self.play_music(beats - 1)

    # def __init__(self):
    #     """ Create an empty list.
    #     """
    #     self.__front = None
    #
    # def append( self, new_value ):
    #     """ Add value to the end of the list.
    #         List is modified.
    #         :param new_value: the value to add
    #         :return: None
    #     """
    #     node = self.__front
    #     newNode = LinkedNode( new_value )
    #     if node == None:
    #         self.__front = newNode
    #     else:
    #         while node.link != None:
    #             node = node.link
    #         node.link = newNode
    #
    # def prepend( self, new_value ):
    #     """ Add value to the beginning of the list.
    #         List is modified.
    #         :param new_value: the value to add
    #         :return: None
    #     """
    #     self.__front = LinkedNode( new_value, self.__front )
    #
    # def start( self ):
    #     """ Generate a cursor that refers to the beginning of the list.
    #         List is unchanged.
    #         :return: a cursor, possibly 'off' if list is empty
    #     """
    #     return self.__front
    #
    # def is_off( self, cursor ):
    #     """ Is the cursor off the list?
    #         :param cursor: the cursor (list position) to be tested
    #         :return: True iff the cursor is not at a valid location in the list.
    #     """
    #     return cursor == None
    #
    # def get_value( self, cursor ):
    #     """ Get the value at the location indicated by the cursor.
    #         List is unchanged.
    #         :pre: not self.is_off( cursor );
    #                         raises ValueError in event of violation
    #         :param cursor: the list position of the desired value
    #         :return: value stored at cursor's location
    #     """
    #     if self.is_off( cursor ):
    #         raise ValueError()
    #     return cursor.value
    #
    # def set_value( self, cursor, new_value ):
    #     """ Change the value at the location indicated by the cursor.
    #         List is modified.
    #         :pre: not self.is_off( cursor )
    #         :param cursor: the list position of the value to be changed
    #         :return: None
    #     """
    #     if self.is_off( cursor ):
    #         raise ValueError()
    #     cursor.value = new_value
    #
    # def next_loc( self, cursor ):
    #     """ Create a new cursor to the next position in the list, or
    #         'off' if cursor is at the last position.
    #         List is unmodified.
    #         :pre: not self.is_off( cursor )
    #                         raises ValueError in event of violation
    #         :param cursor: the list position
    #         :return: the new cursor
    #     """
    #     if self.is_off( cursor ):
    #         raise ValueError()
    #     return cursor.link
    #
    # def insert( self, cursor, new_value ):
    #     """ Place a new value in the list, just before the position
    #         of the cursor. If the cursor is 'off', this method works
    #         just like the append method.
    #         List is modified.
    #         The cursor still refers the location it did in the list
    #             before this method was called.
    #         :param cursor: the list position
    #         :param new_value: the value to be placed before the cursor position
    #         :return: None
    #     """
    #     if cursor == self.__front:
    #         self.prepend( new_value )
    #     else:
    #         node = self.__front
    #         while node.link != cursor:
    #             node = node.link
    #         node.link = LinkedNode( new_value, cursor )
    #
    # def size( self ):
    #     """ Return the number of data elements in this list.
    #         :post: result >= 0
    #     """
    #     return self._size_to_end( self.__front )
    #
    # def _size_to_end( self, node ):
    #     if node == None:
    #         return 0
    #     else:
    #         return 1 + self._size_to_end( node.link )

    # class _Iter:
    #     __slots__ = 'cursor', 'the_list'
    #     def __next__( self ):
    #         if self.the_list.is_off( self.cursor ):
    #             raise StopIteration()
    #         else:
    #             result = self.the_list.get_value( self.cursor )
    #             self.cursor = self.the_list.next_loc( self.cursor )
    #             return result

    # def __iter__( self ):
    #     result = LinkedList._Iter()
    #     result.the_list = self
    #     result.cursor = self.start()
    #     return result
    #
    # def iter2( self ):
    #     cursor = self.start()
    #     while not self.is_off( cursor ):
    #         yield self.get_value( cursor )
    #         cursor = self.next_loc( cursor )
    #
    # def iter3( self, action ):
    #     cursor = self.start()
    #     while not self.is_off( cursor ):
    #         action(  self.get_value( cursor ) )
    #         cursor = self.next_loc( cursor )

# def print_list( seq, msg ):
#     """ Print the contents of a list on a single line, first to last.
#     """
#     print( "%s\n===============\n[%d] " % ( msg, seq.size() ), end="" )
#     cursor = seq.start()
#     while not seq.is_off( cursor ):
#         print( seq.get_value( cursor ), end=" " )
#         cursor = seq.next_loc( cursor )
#     print()
#
#     print( "%s\n===============\n[%d] " % ( msg, seq.size() ), end="" )
#     for element in seq:
#         print( element, end=" " )
#     print()
#
#     print( "%s\n===============\n[%d] " % ( msg, seq.size() ), end="" )
#     for element in seq.iter2():
#         print( element, end=" " )
#     print()
#
#     print( "%s\n===============\n[%d] " % ( msg, seq.size() ), end="" )
#     seq.iter3( lambda element: print( element, end=" " ) )
#     print()


# def test():
#     # Create a list.
#     seq = LinkedList()
#     print_list( seq, "START" )
#
#     # Add values using append.
#     for even in 4, 6:
#         seq.append( even )
#
#     # Prepend a value
#     seq.prepend( 2 )
#     print_list( seq, "EVENS" )
#
#     # Weave additional elements in to the list.
#     odd = 1
#     cursor = seq.start()
#     while not seq.is_off( cursor ):
#         seq.insert( cursor, odd )
#         odd += 2
#         cursor = seq.next_loc( cursor )
#     seq.insert( cursor, odd )
#
#     print_list( seq, "UPTO7" )
#
#     # Test the set_value method.
#     seq.set_value( seq.start(), -1 )
#     print_list( seq, "NEGTV" )
#
# if __name__ == "__main__":
#     test()
