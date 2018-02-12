#!/usr/bin/python

import unittest
from   inventory import Item, Inventory

class TestItem( unittest.TestCase ):

    def setUp( self ):
        self.item = Item( 'Rock' )

    def test___repr__( self ):
        self.assertEqual( str( self.item ), 'Rock' )

class TestInventory( unittest.TestCase ):

    def setUp( self ):
        self.inventory = Inventory( 'Rucksack', self, 10, [ Item( 'Rock' ) ] )

    def test___repr__( self ):
        self.assertIn( 'Rock', str( self.inventory ) )

    def test_tooManyItems( self ):
        self.assertRaises( ValueError, Inventory, 'small bag', self, 1, [ Item( 'Rock' ), Item( 'Mirror' ) ] )

if __name__ == '__main__':
    unittest.main()

