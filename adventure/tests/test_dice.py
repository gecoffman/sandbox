#!/usr/bin/python

import unittest
from   dice import Dice, D6, roll

class ModuleTests( unittest.TestCase ):

    def test_roll( self ):
        rollResult = roll()
        self.assertGreaterEqual( rollResult, 1 )
        self.assertLessEqual( rollResult,    6 )
        
        rollResult = roll( dice = [ D6, D6 ] )
        self.assertGreaterEqual( rollResult, 2 )
        self.assertLessEqual( rollResult,   12 )

class TestDice( unittest.TestCase ):

    def setUp( self ):
        self.dice = Dice()

    def test_roll( self ):
        value = self.dice.roll()
        self.assertGreaterEqual( value, 1 )
        self.assertLessEqual( value, 6 )

class TestD6( unittest.TestCase ):

    def setUp( self ):
        self.d6 = D6()

    def test_roll( self ):
        value = self.d6.roll()
        self.assertGreaterEqual( value, 1 )
        self.assertLessEqual( value, 6 )

    def test___repr__( self ):
        ''' assert that the number of 'o' characters
        that we use to represent a dice 'dot' is equal
        to the die value, for all legal values '''
        def countTheOs( someString ):
            found = 0
            for c in someString:
                if c == 'o':
                    found += 1
            return found

        self.d6.value = 1
        self.assertEqual( countTheOs( str( self.d6 ) ), 1 )
        self.d6.value = 2
        self.assertEqual( countTheOs( str( self.d6 ) ), 2 )
        self.d6.value = 3
        self.assertEqual( countTheOs( str( self.d6 ) ), 3 )
        self.d6.value = 4
        self.assertEqual( countTheOs( str( self.d6 ) ), 4 )
        self.d6.value = 5
        self.assertEqual( countTheOs( str( self.d6 ) ), 5 )
        self.d6.value = 6
        self.assertEqual( countTheOs( str( self.d6 ) ), 6 )

if __name__ == '__main__':
    unittest.main()

