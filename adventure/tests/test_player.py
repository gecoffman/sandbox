#!/usr/bin/python

import unittest
from   player import Player

class PlayerTests( unittest.TestCase ):
	def setUp( self ):
		self.player = Player( 'Bob', skill = 10, stamina = 15, luck = 9 )

	def test___repr__( self ):
		self.assertEqual(
			str( self.player ),
			'Player: Bob (Skill: 10, Stamina: 15, Luck: 9, Affiliation: None)\n\nInventory: Contents of Bob\'s Backpack ( capacity: 10 )\n'
		)

if __name__ == '__main__':
    unittest.main()
