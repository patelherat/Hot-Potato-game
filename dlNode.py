"""
node.py
author: James heliotis
description: A linkable node class for use in stacks, queues, and linked lists
"""
import sys

class LinkedNode:

    __slots__ = "player_name", "prev_player", "next_player"

    def __init__(self, player_name, prev_player = None, next_player = None):
        """ Create a new node and optionally link it to an existing one.
            param value: the value to be stored in the new node
            param link: the node linked to this one
        """
        self.player_name = player_name
        self.prev_player = prev_player
        self.next_player = next_player

    def __str__(self):
        """ Return a string representation of the contents of
            this node. The link is not included.
        """
        return str(self.player_name)

    # def __repr__( self ):
    #     """ Return a string that, if evaluated, would recreate
    #         this node and the node to which it is linked.
    #         This function should not be called for a circular
    #         list.
    #     """
    #     return "LinkedNode(" + repr( self.value ) + "," + \
    #            repr( self.link ) + ")"

# def size_to_end( node ):
#     """ Count how many nodes from this one to a node whose link is None.
#         return: the length of the list starting at node
#     """
#     if node == None:
#         return 0
#     else:
#         return 1 + size_to_end( node.link )

# def test():
#     #count = 0
#     f = open(sys.argv[1], "r")
#
#     while True:
#         line = f.readline().strip()
#         if line == '':
#             break
#         else:
#             #count = count+1
#             nodes = LinkedNode(line, LinkedNode(line, LinkedNode(3.0)))
#             n = nodes
#     while n != None:
#         print( n.value )
#         n = n.link
#     print( "\n" + str( size_to_end( nodes ) ) + " nodes.\n" )
#     print( nodes )
#     print( repr( nodes ) )
#
# if __name__ == "__main__":
#     test()
