#!/usr/bin/python

#
# ID       : Dice.py
# Sensitive: Not :)
#

from random import randint

class Dice( object ):
    def __init__( self, minimum = 1, maximum = 6, sides = 6 ):
        self.minimum = minimum
        self.maximum = maximum
        self.sides   = sides
        self.value   = self.roll()

    def roll( self ):
        self.value = randint( self.minimum, self.maximum )
        return self.value

class D6( Dice ):
    def __init__( self ):
        super( D6, self ).__init__( minimum = 1, maximum =6, sides = 6 )

    def __repr__( self ):
        if   self.value == 1:
            return '\n'.join( [ ' --- ', '|   |', '| o |', '|   |', ' --- ' ] )
        elif self.value == 2:
            return '\n'.join( [ ' --- ', '|  o|', '|   |', '|o  |', ' --- ' ] )
        elif self.value == 3:
            return '\n'.join( [ ' --- ', '|  o|', '| o |', '|o  |', ' --- ' ] )
        elif self.value == 4:
            return '\n'.join( [ ' --- ', '|o o|', '|   |', '|o o|', ' --- ' ] )
        elif self.value == 5:
            return '\n'.join( [ ' --- ', '|o o|', '| o |', '|o o|', ' --- ' ] )
        elif self.value == 6:
            return '\n'.join( [ ' --- ', '|o o|', '|o o|', '|o o|', ' --- ' ] )

def roll( dice = None ):
    if not dice:
        dice = [ D6 ]

    rollResult = 0
    for dieClazz in dice:
        instance = dieClazz()
        rollResult += instance.roll()

    return rollResult