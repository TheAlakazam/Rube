#! /usr/bin/env python3

class Square(object):

    """Docstring for Square.
        Defines each square of the cube
    """
    def __init__(self, color, pos):
        """TODO: to be defined1.
        """
        self.color = color
        self.pos = pos

class Row(object):

    """Docstring for Row. """

    def __init__(self, sqs) :
        """TODO: to be defined1. """
        self.left = Square(sqs[0])
        self.centre = Square(sqs[1])
        self.right = Square(sqs[2])

class Face(object):

    """Docstring for Face. """

    def __init__(self):
        """TODO: to be defined1."""
        self.top = Row()
        self.mid = Row()
        self.bot = Row()
    def rotate()
